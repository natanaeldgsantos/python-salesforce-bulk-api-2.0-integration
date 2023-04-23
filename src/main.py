
# IMPORTS
# ********************************************************

import os
import json
import time
import requests
from dotenv import load_dotenv
from urllib.parse import urljoin

# Libraries and packages
from  authentication import oauth

from bulk_query.query import BulkQuery
from bulk_ingest.ingest import BulkIngest

from sobjects.objects import Objects

load_dotenv() # retorna variáveis de ambiente do arquivo .env

 # GLOBAL VARIABLES
 # ********************************************************

class Params:

    
    API_VERSION =  'v56.0'

    # Credentials
    USERNAME = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    
    SECURITY_TOKEN = os.getenv('SECURITY_TOKEN')

    CONSUMER_KEY    = os.getenv('CONSUMER_KEY')
    CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
    
    MY_INSTANCE = os.getenv('MY_INSTANCE')

    DOMAIN_URI  = f'https://{MY_INSTANCE}.develop.my.salesforce.com'



# 01. Generate a new Token
# ***********************************************************

bearer_acces_token = oauth.generate_token(
                            consumer_key=     Params.CONSUMER_KEY, 
                            consumer_secret=  Params.CONSUMER_SECRET, 
                            domain_uri=       Params.DOMAIN_URI,
                            username=         Params.USERNAME,
                            password=         Params.PASSWORD,
                            security_token=   Params.SECURITY_TOKEN
    
                    )

# refresh_token = oauth.refresh_token(
#                             consumer_key=      Params.CONSUMER_KEY,
#                             consumer_secret=   Params.CONSUMER_SECRET,
#                             domain_uri=        Params.DOMAIN_URI,
#                             access_token=      access_token 

#                     )

# print(refresh_token)


# 02. Creating a new Query Job
# ***********************************************************

# query = BulkQuery(

#     bearer_token=      bearer_acces_token,
#     consumer_key=      Params.CONSUMER_KEY,
#     consumer_secret=   Params.CONSUMER_SECRET,
#     instance_url=      Params.DOMAIN_URI, 
    
# )

# soql_query= """ 
#     SELECT 
#             Name,
#             Account_Record_ID__c,
#             ZC_P1_Xplan_ID__c
#     FROM ZAccount__c"""

# query_job = query.create_query_job(soql_query=soql_query)

# print(json.dumps(query_job, indent=4))

# job_id = query_job['id']

# time.sleep(5)



# 03. Info about All query Jobs
# ***********************************************************

# records = query.get_info_about_all_query_jobs()

# import pandas as pd

# df = pd.DataFrame(records)
# print(df.head())

# 04. Get Info about Query Job
# ***********************************************************

# job_info = query.get_info_about_query_job(job_id=job_id)
# print(job_info)


# # 05. Get Query Job Results
# # ***********************************************************

# response = query.get_query_job_results(job_id=job_id)

# print('* Results\n')
# print(response.headers)
# print("* type: ", type( response.content))
# print(response.content)


# ingest = BulkIngest(

#     bearer_token=      bearer_acces_token,
#     consumer_key=      Params.CONSUMER_KEY,
#     consumer_secret=   Params.CONSUMER_SECRET,
#     instance_url=      Params.DOMAIN_URI    
# )


# job_id = ingest.create_injest_job(operation="insert", object_name="Account")


# dirname = os.path.dirname(__file__)
# IN_DATA_DIR = os.path.join(dirname, 'data','input')


# csv_path = os.path.join(IN_DATA_DIR, 'insert_accounts.csv')


# ingest.upload_job_data(csv_file_path=csv_path,job_id=job_id)


object = Objects(
    bearer_token= bearer_acces_token,
    instance_url= Params.DOMAIN_URI
)

# objects = object.get_list_of_available_objects()
# print(json.dumps(objects, indent=4))