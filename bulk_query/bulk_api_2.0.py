
# **********************************************************
#  SALESFORCE - BULK API 2.0 FUNCTIONS
# **********************************************************

# Documentation: https://developer.salesforce.com/docs/atlas.en-us.240.0.api_asynch.meta/api_asynch/query_create_job.htm

import os
import requests

INSTANCE    =  'studnet4-dev-ed'                            
DOMAIN_URI  = f"https://{INSTANCE}.develop.my.salesforce.com"
API_VERSION =  'v56.0'

bearer_token = ''


# CREATE A QUERY JOB

def create_query_job(soql_query:str):
    """ """
    uri = f'/services/data/{API_VERSION}/jobs/query'
    query_job_endpoint = os.path.join(DOMAIN_URI, uri)

    header = {
        'Authorization': bearer_token
    }

    request_body = {
        'operation': "query",
        "query":     soql_query
    }

    response = requests.post(query_job_endpoint, header= header, data = request_body)

    response = requests.post()



#  input variables = [ ]

# GET INFORMATION ABOUT A QUERY JOB

# GET RESULTS FOR A QUERY JOB

# ABORT A QUERY JOB

# DELETE A QUERY JOB

# GET INFORMATION ABOUT ALL QUERY JOBS

