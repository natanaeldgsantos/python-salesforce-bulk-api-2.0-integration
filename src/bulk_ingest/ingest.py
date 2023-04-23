
# **********************************************************
#  SALESFORCE - BULK API 2.0 INGEST
# **********************************************************

# Documentation: https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/datafiles_understanding_bulk2_ingest.htm

import json
import requests
from urllib.parse import urljoin


class BulkIngest:

    def __init__(self, consumer_key: str, consumer_secret: str, instance_url: str, bearer_token: str):

        self.api_version = "v54.0"
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.instance_url = instance_url
        self.bearer_token = bearer_token
 

    def create_injest_job(self, operation: str, external_id_field_name: str = None, object_name: str = None) -> str:
        """ 
            Creates a job representing a bulk operation and its associated data that is sent to Salesforce for asynchronous processing. 
            Provide job data via an Upload Job Data request or as part of a multipart create job request.

            return new JobID
        """

        # Check function parameters
        valid_operations = {'insert', 'delete',
                            'hardDelete', 'update', 'upsert'}
        if operation not in valid_operations:
            raise ValueError("Parameter 'operation' must be one of %r." % valid_operations)

        if operation == 'upsert' and external_id_field_name is None:
            raise ValueError('the field <external_id_field_name> is required for UPSERT operations. Enter the nome of your <external_id_field_name> ')

        if object_name is None:
            raise ValueError('The Object Name cannot be empty. Enter the name of the object. ')

        uri = f"/services/data/{self.api_version}/jobs/ingest"
        endpoint = urljoin(self.instance_url, uri)

        request_header = {
            "Authorization": self.bearer_token,
            "Content-Type": "application/json",
            "Content-Disposition": "form-data; name='job' "
        }

        request_body = {
            "object": object_name,
            "contentType": "CSV",
            "externalIdFieldName": external_id_field_name,
            "operation": operation
        }

        try:
            response = requests.post( endpoint, headers=request_header, data=json.dumps(request_body))
            print('* Salesforce Injest Job Info - Request status', response.status_code)

            if response.status_code >= 200 and response.status_code < 300:
                print(json.dumps(response.json(), indent=4))
                return response.json()['id']
            else:
                print('Something is wrong:')
                return response.json()

        except Exception as e:
            print(e)


    def upload_job_data(self, job_id: str, csv_file_path=str):

        """ """

        uri = f"/services/data/{self.api_version}/ingest/{job_id}/batches"
        endpoint = urljoin(self.instance_url, uri)

        # Check Function parameters

        request_header = {
            "Authorization": self.bearer_token,
            "Content-Type":"text/csv",
            "Accept":"application/json",
            "X-PrettyPrint":"1"

        }
        
        with open( csv_file_path, 'rb') as f:
            data = f.read()

        try:
            response = requests.put(endpoint, headers=request_header, data= data)
            print('* Job upload executed successfully')
        except Exception as e:
            print(e)

        return None


    def close_or_abort_job(self, job_id:str, job_state:str):
        """ Closes or aborts a job. If you close a job, Salesforce queues the job and uploaded data for processing, 
            and you can’t add any more job data. If you abort a job, the job doesn’t get queued or processed.
        """
        
        # Check function parameters
        valid_states = {'UploadComplete':'to close a job', 'Aborted':'to abort a job'}
        if job_state not in valid_states.keys():
            raise ValueError("Parameter 'job_state' must be one of %r." % valid_states)        

        uri = f"/services/data/{self.api_version}/jobs/ingest/{job_id}"
        endpoint = urljoin(self.instance_url, uri)

        request_header = { "Authorization": self.bearer_token }
        request_body =   { "state": job_state}

        try:
            response = requests.patch(endpoint, headers=request_header, data = json.dumps(request_body))
            print('* Salesforce Job Close/Abort - Request status', response.status_code)

            if response.status_code >= 200 and response.status_code < 300:
                print(json.dumps(response.json(), indent=4))                
            else:
                print('Something is wrong:')
                return response.json()
        except Exception as e:
            print(e)


    def delete_job(self, job_id:str):
        """ 
            Deletes a job. 
            * To be deleted, a job must have a state of UploadComplete, JobComplete, Aborted, or Failed
        """

        uri = f"/services/data/{self.api_version}/jobs/ingest/{job_id}"
        endpoint = urljoin(self.instance_url, uri)

        request_header = {"Authorization": self.bearer_token}

        try:
            response = requests.delete(endpoint, headers=request_header)
            print('* Salesforce Delete Job - Request status', response.status_code)

            if response.status_code >= 200 and response.status_code < 300:
                print(json.dumps(response.json(), indent=4))                
            else:
                print('Something is wrong:')
                return response.json()
        except Exception as e:
            print(e)


    def get_all_jobs_info(self) -> dict:
        """ Retrieves all jobs in the org """

        uri = f"/services/data/{self.api_version}/jobs/ingest"
        endpoint = urljoin(self.instance_url, uri)

        request_header = {"Authorization": self.bearer_token}

        try:
            response = requests.get(endpoint, headers=request_header)
            print('* Salesforce Get All Jobs info - Request status', response.status_code)

            if response.status_code >= 200 and response.status_code < 300:
                print(json.dumps(response.json(), indent=4))  
                return response.json()              
            else:
                print('Something is wrong:')
                return response.json()
        except Exception as e:
            print(e)


    def get_job_info(self, job_id:str) -> dict:
        """ Retrieves detailed information about a job """

        uri = f"/services/data/{self.api_version}/jobs/ingest/{job_id}"
        endpoint = urljoin(self.instance_url, uri)

        request_header = {"Authorization": self.bearer_token}

        try:
            response = requests.get(endpoint, headers=request_header)
            print('* Salesforce Get Job info - Request status', response.status_code)

            if response.status_code >= 200 and response.status_code < 300:
                print(json.dumps(response.json(), indent=4))  
                return response.json()              
            else:
                print('Something is wrong:')
                return response.json()
        except Exception as e:
            print(e)
    
    
    def get_job_successful_record_results(self, job_id:str) -> dict:
        """ Retrieves a list of successfully processed records for a completed job """

        uri = f"/services/data/{self.api_version}/jobs/ingest/{job_id}/successfulResults/"
        endpoint = urljoin(self.instance_url, uri)

        request_header = {"Authorization": self.bearer_token}

        try:
            response = requests.get(endpoint, headers=request_header)
            print('* Salesforce Job Successful Records Results - Request status', response.status_code)

            if response.status_code >= 200 and response.status_code < 300:
                print(json.dumps(response.json(), indent=4))  
                return response.json()              
            else:
                print('Something is wrong:')
                return response.json()
        except Exception as e:
            print(e)


    def get_job_failed_record_results(self, job_id:str) -> dict:
        """ Retrieves a list of failed records for a completed insert, delete, update, or upsert job """

        uri = f"/services/data/{self.api_version}/jobs/ingest/{job_id}/failedResults/"
        endpoint = urljoin(self.instance_url, uri)

        request_header = {"Authorization": self.bearer_token}

        try:
            response = requests.get(endpoint, headers=request_header)
            print('* Salesforce Job Failed Records Results - Request status', response.status_code)

            if response.status_code >= 200 and response.status_code < 300:
                print(json.dumps(response.json(), indent=4))  
                return response.json()              
            else:
                print('Something is wrong:')
                return response.json()
        except Exception as e:
            print(e)


    def get_job_unprocessed_record_results(self, job_id:str) -> dict:
        """ Retrieves a list of unprocessed records for failed or aborted jobs """

        uri = f"/services/data/{self.api_version}/jobs/ingest/{job_id}/unprocessedrecords/"
        endpoint = urljoin(self.instance_url, uri)

        request_header = {"Authorization": self.bearer_token}

        try:
            response = requests.get(endpoint, headers=request_header)
            print('* Salesforce Job Unprocessed Records Results - Request status', response.status_code)

            if response.status_code >= 200 and response.status_code < 300:
                print(json.dumps(response.json(), indent=4))  
                return response.json()              
            else:
                print('Something is wrong:')
                return response.json()
        except Exception as e:
            print(e)