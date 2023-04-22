
# IMPORTS AND LIBRARIES 
# ********************************************************

from dotenv import load_dotenv
import os
import requests

load_dotenv() # retorna variáveis de ambiente do arquivo .env


# GLOBAL VARIABLES
# ********************************************************

# Credentials
USERNAME = os.getenv('DEV_USER')
PASSWORD = os.getenv('DEV_PASS')

SECURITY_TOKEN = os.getenv('DEV_SECURITY_TOKEN')

# Create a new App and Get it
CONSUMER_KEY    = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
# CALLBACK_URL    = os.getenv('CALLBACK_URL')

# API
MY_INSTANCE = os.getenv('MY_INSTANCE')  # name of your company, something like https://<my-company>.my.salesforce.com/
DOMAIN      = f'https://{MY_INSTANCE}.my.salesforce.com'

print(DOMAIN)



# GENERATE ACCESS TOKEN
# ********************************************************

def generate_token():
    """ Generate Salesforce Access Token"""

    payload = {

        'grant_type':    'password',
        'client_id':     CONSUMER_KEY, 
        'client_secret': CONSUMER_SECRET,
        'username':      USERNAME,
        'password':      PASSWORD + SECURITY_TOKEN
    }

    print(payload)
    oauth_endpoint = '/services/oauth2/token'
    response = requests.post(DOMAIN + oauth_endpoint, data = payload)
    print('Salesforce Acess token request: Status:',response.status_code)

    print(DOMAIN+oauth_endpoint)

    return response.json()

access_token = generate_token()['access_token']
print(access_token)

print('\n End ***')

soql_query = """

    SELECT
        LastModifiedDate,
        Subfund_internal_ID__c,
        ZC_P1_Account__c,
        entity_id_c,
        sample_a__c,
        sample_b__c 
    FROM ZAsset__c

"""

def query(soql_query):

    headers = { 'Authorization': 'Bearer ' + access_token }

    try:

        endpoint = '/services/data/v56.0/query'
        records = []
        response = requests.get(DOMAIN + endpoint, headers = headers, params = {'q': soql_query})
        print(response.json())
        total_size = response.json()['totalSize']
        records.extend(response.json()['records'])

        while not response.jsoin()['done']:
            response = requests.get(DOMAIN + endpoint + response.json()['nextRecordUrl'], headers= headers)
            records.extend(response.json()['records'])
        return {'record_size': total_size, 'records': records}
    
    except Exception as e:
        print(e)
        return

records = query(soql_query)


#
# 


soql_query = """

    SELECT
        LastModifiedDate,
        Subfund_internal_ID__c,
        ZC_P1_Account__c,
        entity_id_c,
        sample_a__c,
        sample_b__c 
    FROM ZAsset__c

"""

{
  "operation": "query",
  "query":     soql_query
}
