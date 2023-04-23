
# ZAsset - Api_Name: ZAsset__c
# ************************************************************************************

"""
    SELECT
        ZC_P1_Account__c,
        entity_id__c,
        Subfund_internal_ID__c,
        sample_a__c,
        sample_b__c
    FROM ZAsset__c

"""

# ZAccount - API_Name: ZAccount__c
# ************************************************************************************

"""
    SELECT

        ZC_P1_Xplan_ID__c,
        Account_Record_ID__c

    FROM ZAccount__c

"""


# InvestimentOption - API_Name: InvestimentOption__c
# ************************************************************************************

"""
    SELECT

        Portfolio_Name__c,
        Account__c,
        Account_Number__c,
        XPLAN_Entity_Name__c,
        XPLAN_Entity_ID__c,
        Subfund_Internal_ID__c

    FROM InvestimentOption__c
"""


# Asset_Stagging - API_Name: Asset_Stagging__c
# ************************************************************************************

"""
    SELECT

        sample_b__c,
        sample_a__c,
        Subfund_internal_ID__c,
        ZC_P1_Account__c,
        entity_id__c  

    FROM Asset_Stagging__c
"""


