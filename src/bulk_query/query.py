

# **********************************************************
#  SALESFORCE - BULK API 2.0 QUERY
# **********************************************************

# Documentation: https://developer.salesforce.com/docs/atlas.en-us.240.0.api_asynch.meta/api_asynch/query_bulk_api_2_0.htm


# Imports, Libraries and Packages

import requests
import json
from urllib.parse import urljoin



class BulkQuery:

    def __init__(self, consumer_key:str, consumer_secret:str, instance_url:str, bearer_token:str):

        self.api_version     = "v56.0"
        self.consumer_key    = consumer_key
        self.consumer_secret = consumer_secret
        self.instance_url    = instance_url
        self.bearer_token    = bearer_token


    def create_query_job(self, soql_query:str) -> dict :
        """ Create a new Query Job """

        print('\n *** CREATING NEW QUERY JOB *** ')
        uri = f'/services/data/{self.api_version}/jobs/query'
        endpoint = urljoin(self.instance_url, uri)
        
        request_header = {
            "Authorization": self.bearer_token,
            "Accept":        "application/json",
            "Content-Type":  "application/json"
        }

        request_body = {
            "operation": "query",
            "query":     soql_query
        }
        
        try:
            response = requests.post(endpoint, headers= request_header, data = json.dumps(request_body))
            print('* Salesforce Query Job - Request status', response.status_code)

            if response.status_code >= 200 and response.status_code < 300:
                return response.json()
            else:
                print('Somethin is wrong:')
                return response.json()

        except Exception as e:            
            print(e)

               
    def get_info_about_all_query_jobs(self) -> list:
        """ Gets information about all query jobs in the org """

        records = []
        done    = "false"

        uri = f'/services/data/{self.api_version}/jobs/query?jobType=V2Query'
        endpoint = urljoin(self.instance_url, uri)

        request_header = { "Authorization": self.bearer_token }   

        while done == "false":
            try:
                response = requests.get(endpoint, headers=request_header)
                print('* Salesforce All Jobs Info - Request status', response.status_code)

                if response.status_code >= 200 and response.status_code < 300:                    
                    for record in response.json()['records']:
                        records.append(record)
                    if response.json()['done'] == 'false':
                        endpoint = urljoin(self.instance_url, response.json()['nextRecordsUrl'])
                    else:
                        done = "true"
                else:
                    print('Something is wrong:')
                    print(response.json())
            except Exception as e:
                print(e)
        
        return records
    
    
    def get_info_about_query_job(self, job_id:str):
        """ Gets information about one query job """

        uri = f'/services/data/{self.api_version}/jobs/query/{job_id}'
        endpoint = urljoin(self.instance_url, uri)

        request_header = { "Authorization": self.bearer_token }        

        try:
            response = requests.get(endpoint, headers= request_header)
            print('* Salesforce Query Job Info - Request status', response.status_code)

            if response.status_code >= 200 and response.status_code < 300:
                return response.json()
            else:
                print('Somethin is wrong:')
                return response.json()

        except Exception as e:            
            print(e)
    

    def get_query_job_results(self, job_id:str):
        """ Get the results for a query job """

        uri = f'/services/data/{self.api_version}/jobs/query/{job_id}/results?maxRecords=50000'
        endpoint = urljoin(self.instance_url, uri)

        request_header = {
            "Authorization": self.bearer_token,
            "Accept":        "text/csv"            
        }

        try:
            response = requests.get(endpoint, headers= request_header)
            print('* Salesforce Query Job Results - Request status', response.status_code)                      

            if response.status_code >= 200 and response.status_code < 300:
                return response
            else:
                print('Somethin is wrong:')
                return response.json()

        except Exception as e:            
            print(e)
        
    
    def abort_query_job(self, job_id:str):
        """ Aborts a query job 
            * You can only abort jobs that are in the following states:
               - UploadComplete
               - InProgres
        
        """
        uri = f'/services/data/{self.api_version}/jobs/query/{job_id}'
        endpoint = urljoin(self.instance_url, uri)

        request_header = {
            "Authorization": self.bearer_token,            
            "Content-Type":  "application/json"
        }

        request_body = {"state": "Aborted" }

        try:
            response = requests.patch(endpoint, headers= request_header, data = request_body)
            print('* Salesforce Query Job - Request status', response.status_code)

            if response.status_code >= 200 and response.status_code < 300:
                return response.json()
            else:
                print('Somethin is wrong:')
                return response.json()

        except Exception as e:            
            print(e)
        
    
    def delete_query_job(self, job_id:str):
        """ Deletes a query job """
        uri = f'/services/data/{self.api_version}/jobs/query/{job_id}'
        endpoint = urljoin(self.instance_url, uri)

        request_header = {
            "Authorization": self.bearer_token,            
            "Content-Type":  ""
        }

        try:
            response = requests.delete(endpoint, headers= request_header)
            print('* Salesforce Query Job - Request status', response.status_code)

            if response.status_code >= 200 and response.status_code < 300:
                return response.json()
            else:
                print('Somethin is wrong:')
                return response.json()

        except Exception as e:            
            print(e)
       
    

    
# def query(soql_query):

#     headers = { 'Authorization': 'Bearer ' + access_token }

#     try:

#         endpoint = '/services/data/v56.0/query'
#         records = []
#         response = requests.get(DOMAIN + endpoint, headers = headers, params = {'q': soql_query})
#         print(response.json())
#         total_size = response.json()['totalSize']
#         records.extend(response.json()['records'])

#         while not response.jsoin()['done']:
#             response = requests.get(DOMAIN + endpoint + response.json()['nextRecordUrl'], headers= headers)
#             records.extend(response.json()['records'])
#         return {'record_size': total_size, 'records': records}
    
#     except Exception as e:
#         print(e)
#         return

# records = query(soql_query)