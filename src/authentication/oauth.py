
import os
import requests
from urllib.parse import urljoin

def generate_token( domain_uri: str, consumer_key:str, consumer_secret:str, username:str, password:str, security_token:str) -> str:
    """ Generate Salesforce Access Token"""

    print('\n***** CREATING ACCESS TOKEN *****')
    endpoint = urljoin(domain_uri, '/services/oauth2/token') 
    
    payload = {

        'grant_type':   'password',
        'client_id':     consumer_key, 
        'client_secret': consumer_secret,
        'username':      username,
        'password':      password + security_token
    }
    
    try:
        response = requests.post( endpoint, data = payload)
        print('* Salesforce Access token request: Status:',response.status_code)
        
        if response.status_code == 200:
            return "Bearer {}".format(response.json()['access_token'])
        else:
            print('Something is wrong:')
            return response.json()
    except Exception as e:
        print(e)


def refresh_token(domain_uri:str, consumer_key:str, consumer_secret:str, access_token:str) -> str:
    """ After a receives an access token, it can use a refresh token to get a new session when its current session expires """

    print('\n***** REFRESH ACCESS TOKEN *****')
    endpoint = urljoin(domain_uri, '/services/oauth2/token' )
    
    request_header = { 'Authorization': 'Basic' }

    payload = {

        'grant_type':   'refresh_token',
        'client_id':     consumer_key, 
        'client_secret': consumer_secret,
        'refresh_token': access_token
    }

    try:
        response = requests.post( endpoint, headers= request_header, data = payload)
        print('Salesforce Refresh token request: Status:',response.status_code)
        
        if response.status_code == 200:
            return response.json()['refresh_token']
        else:
            print('Something is wrong:')
            return response.json()
    except Exception as e:
        print(e)

    



    

   


