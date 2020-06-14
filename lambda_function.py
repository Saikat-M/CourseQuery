import json
import os
import time
import logging

import random
import requests
# from botocore.vendored import requests

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

""" --- Helpers to build responses which match the structure of the necessary dialog actions --- """


def get_slots(intent_request):
    # logger.debug(intent_request);
    return intent_request['currentIntent']['slots']


def close(session_attributes, fulfillment_state, message):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }

    return response


""" --- Functions that control the bot's behavior --- """


def search_mooc(intent_request):
    """
    Performs dialog management and fulfillment for ordering flowers.
    Beyond fulfillment, the implementation of this intent demonstrates the use of the elicitSlot dialog action
    in slot validation and re-prompting.
    """

    # logger.debug(intent_request)
    topics = get_slots(intent_request)["Topics"]
    source = intent_request['invocationSource']
    msgs=[]
    
    if source == 'DialogCodeHook':
        slots = get_slots(intent_request)
        
    # defining a params dict for the parameters to be sent to the API
    """
    It's a recommened coding practice not to write any credentials in the code directly. For that, below the code console 
    there is a section called 'Environment variables'. There two key-value pair have been created,
    one for the API key another one for the Custom Engine ID. and value for each of the variables can be accessed through 
    this command os.environ['KEY_NAME'].
    """     
    key = os.environ['key']
    cx = os.environ['cx']
    q = topics+" courses"
    
    #Creating the URL
    url = f'https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={q}'
    
    # sending get request and saving the response as response object
    response = requests.get(url)
    # logger.debug(response);

    # extracting data in json format 
    results = (response.json()).get('items')
    # logger.debug(results[1]['link']);
    for i in results:
        # logger.debug(i['link'])
        msgs.append(i['link'])
    # logger.debug(len(msgs))
    # logger.debug(msgs)
    n = random.randint(0,5)

    return close(intent_request['sessionAttributes'],
                        'Fulfilled',
                        {'contentType': 'CustomPayload',
                        'content': "Result :\n"+msgs[n]
                        }
                )

""" --- Intents --- """


def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """
    logger.debug('dispatch userId={}, intentName={}'.format(intent_request['userId'], intent_request['currentIntent']['name']))
    intent_name = intent_request['currentIntent']['name']

    # Dispatch to your bot's intent handlers
    if intent_name == 'SearchMOOC':
        return search_mooc(intent_request)

    raise Exception('Intent with name ' + intent_name + ' not supported')
    
    
""" --- Main handler --- """
    
def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
    # By default, treat the user request as coming from the America/New_York time zone.
    os.environ['TZ'] = 'America/New_York'
    time.tzset()
    logger.debug('event.bot.name={}'.format(event['bot']['name']))
    # logger.debug(event)
    return dispatch(event)
