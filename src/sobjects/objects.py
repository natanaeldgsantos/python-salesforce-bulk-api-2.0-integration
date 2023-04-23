
import requests
import json
from urllib.parse import urljoin


class Objects:

    def __init__(self, instance_url: str, bearer_token: str):
        self.api_version = 'v57.0'
        self.instance_url = instance_url
        self.bearer_token = bearer_token

    def get_list_of_available_objects(self):
        """ Get a List of the available objects """

        print('*** GET LIST OF AVAILABLE OBJECTS ***')

        uri = f"/services/data/{self.api_version}/sobjects"
        endpoint = urljoin(self.instance_url, uri)
        
        request_header = { "Authorization": self.bearer_token}

        try:
            response = requests.get(endpoint, headers= request_header)
            print('* Salesforce Get List of Available Objects - Request status', response.status_code)

            if response.status_code >= 200 and response.status_code < 300:
                return response.json()
            else:
                print('Something is wrong:')
                return response.json()

        except Exception as e:            
            print(e)


    def get_basic_object_info(self, object_name:str):
        """  Retrieves basic metadata for a specified object, including:
                - some object properties
                - recent items
                - URIs for other resources related to the object
        """

        print('*** GET BASIC INFO ABOUT OBJECT ***')

        uri = f"/services/data/{self.api_version}/sobjects/{object_name}"
        endpoint = urljoin(self.instance_url, uri)
        
        request_header = { "Authorization": self.bearer_token}

        try:
            response = requests.get(endpoint, headers= request_header)
            print('* Salesforce Get List of Available Objects - Request status', response.status_code)

            if response.status_code >= 200 and response.status_code < 300:
                return response.json()
            else:
                print('Something is wrong:')
                return response.json()

        except Exception as e:            
            print(e)


    def get_fields_from_object(self, object_name:str):    
        """  Retrieve each field from Object """

        print('*** GET FIELDS FROM A OBJECT ***')

        uri = f"/services/data/{self.api_version}/sobjects/{object_name}/describe"
        endpoint = urljoin(self.instance_url, uri)
        
        request_header = { "Authorization": self.bearer_token}

        try:
            response = requests.get(endpoint, headers= request_header)
            print('* Salesforce Get fields from a Object - Request status', response.status_code)

            if response.status_code >= 200 and response.status_code < 300:
                return response.json()['fields']
            else:
                print('Something is wrong:')
                return response.json()

        except Exception as e:            
            print(e)


    def get_metadata_from_object(self, object_name:str):    
        """  Retrieve each field from Object """

        print('*** GET FIELDS FROM A OBJECT ***')

        uri = f"/services/data/{self.api_version}/sobjects/{object_name}/describe"
        endpoint = urljoin(self.instance_url, uri)
        
        request_header = { "Authorization": self.bearer_token}

        try:
            response = requests.get(endpoint, headers= request_header)
            print('* Salesforce Get fields from a Object - Request status', response.status_code)

            if response.status_code >= 200 and response.status_code < 300:
                return response.json()
            else:
                print('Something is wrong:')
                return response.json()

        except Exception as e:            
            print(e)























