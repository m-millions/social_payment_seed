#
'''
A "Venmo-like" system of payments between users. 

Part I builds the data for a "social" payments feed. 
Part II, implements a method for sending a new payment through the API. 

# >>> >>> >>> * >>> >>> >>> * >>> >>> >>>  WHAT the code DOES  <<< <<< <<< * <<< <<< <<< * <<< <<< <<< 

 (1) Sends requests to API end-points:

 --- To GET a User
 --- To GET all Users
 --- To GET all Accounts
 --- To GET all Transfers
 --- To POST a new Transfer

The code also performs various transformations and checks on the data.  
Those steps are documented in the code and easy to step through. 

Print statements have been left in the files to facilitate steppiing through the code, 
since formal test-cases are not included.  Code has been throughly tested.  

# >>> >>> >>> * >>> >>> >>> * >>> >>> >>>  WHAT the code DOES NOT DO  <<< <<< <<< * <<< <<< <<< * <<< <<< <<<

(1) It does not check to see that the SENDER account ID is the same as the RECEPIENTS account ID
(2) It does not subtract from the SENDER's account balance after a transfer has gone through
(3) It does not handle the concept of PREFERED/DEFAULT account for either SENDER or RECEPIENT
(4) It does not (yet) accept parameters from the command line
(5) It is not integrated with Curl

# >>> >>> >>> * >>> >>> >>> * >>> >>> >>>   SAMPLE DATA  <<< <<< <<< * <<< <<< <<< * <<< <<< <<<

  TRANSFERS: { "status": "Initiated",
               "failedAt": "",
               "originAccount": "1",
               "targetAccount": "6",
               "completedAt": "",
               "amount": "7000",
               "initiatedAt": "00:57:54.663924",
               "id": "1576475875000",
               "description": "Happy Birthday!"
             }
'''

# >>> >>> >>> * >>> >>> >>> * >>> >>> >>>   START CODE   <<< <<< <<< * <<< <<< <<< * <<< <<< <<<
import datetime

import requests
from requests.exceptions import HTTPError
from requests.exceptions import Timeout


# >>> >>> >>> * >>> >>> >>> * >>> >>> >>>  GLOBAL VARIABLES   <<< <<< <<< * <<< <<< <<< * <<< <<< <<<
current_time = datetime.datetime.now().time()
uri = "https://some.glitch.me"
transfer_account_id = ''
recepient_main_account_id = ''


# >>> >>> >>> * >>> >>> >>> * >>> >>> >>>  ALL GETS   <<< <<< <<< * <<< <<< <<< * <<< <<< <<< 
# GET A SPECIFIC ACCOUNT
def get_account(id='1'):
    '''
    GETs All User Accounts Information
    '''
    try:
        request_an_account = uri + "/accounts/" + id
        print(request_an_account)

        print('Initializing call and sending request: ' + request_an_account + ' ...')
        #response = requests.get(request_an_account)

        try:
          response = requests.get(request_an_ccount, timeout=(3,3))
        except Timeout:
          print('The request timed out')
        else:
          print('The request did not time out')

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
        
        account_data = response.json()
    
    except HTTPError as http_err:
        print('HTTP error occurred: ' + {http_err})
    except Exception as err:
        print('Other error occurred: ' + {err}) 
    else:
        print('Success!')
        print( '--- --- ---' )

    return account_data


# GET ALL ACCOUNTS
def get_accounts_all():
    '''
    EXTRACTION
    GETs All User Accounts Information
    TO-DOs: 
    (1) ...  
    '''
    try:
        request_accounts = uri + "/accounts"
        print request_accounts
        #implemented for this example as resonse tends to be consitently slow
        print('Initializing call and sending request: ' + request_accounts + ' ...')
        #response = requests.get(request_accounts)

        try:
          response = requests.get(request_accounts, timeout=(3,3))
        except Timeout:
          print('The request timed out')
        else:
          print('The request did not time out')

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
        
        account_data = response.json()
    
    except HTTPError as http_err:
        print( 'HTTP error occurred: ' + format({http_err}) )
    except Exception as err:
        print( 'Other error occurred: ' + format({err}) ) 
    else:
        print('Success!')
        print( '--- --- ---' )

    return account_data


# GET A SPECIFIC USER
def get_user(user_id):
    '''
    EXTRACTION
    GETs Sending User and Receiving User
    TO-DOs: 
    (1) ...  
    '''
    try:
        request_a_user = uri + "/users/" + user_id
        print(request_a_user)

        print('Initializing call and sending request: ' + request_a_user + ' ...')

        try:
          response = requests.get(request_a_user, timeout=(3,3))
        except Timeout:
          print('The request timed out')
        else:
          print('The request did not time out')

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
        
        user_data = response.json()
    
    except HTTPError as http_err:
        print( 'HTTP error occurred: ' + format({http_err}) )
    except Exception as err:
        print( 'Other error occurred: ' + format({err}) ) 
    else:
        print( 'Success!' )
        print( '--- --- ---' )

    return user_data


# GET ALL USERS
def get_users_all():
    '''
    GETs Sending User and Receiving User 
    '''
    try:
        request_users = uri + "/users"

        print('Initializing call and sending request: ' + request_users + ' ...')

        try:
          response = requests.get(request_users, timeout=(3,3))
        except Timeout:
          print('The request timed out')
        else:
          print('The request did not time out')

        # If the response was successful, no Exception will be raised
        response.raise_for_status()        
        
        all_users_data = response.json()
    
    except HTTPError as http_err:
        print( 'HTTP error occurred: ' + format({http_err}) )
    except Exception as err:
        print( 'Other error occurred: ' + format({err}) ) 
    else:
        print('Success!')
        print( '--- --- ---' )

    return all_users_data


# GET ALL TRANSFERS
def get_transfers():
    '''
    Part I: build the data for a "social" payments feed

    Resouce:

    implement a method to build the data for a "social" transfers feed, 
    combining information from whichever API resources are necessary.

    Transfers with a "failed" status should be excluded from the feed. 

    Sample Output:

    [
      {
        "originUserName": "John Smith",         // Full name of User associated with origin Account
        "targetUserName": "Sallie Someone",     // Full name of User associated with target Account
        "amount": 54.99,                        // Amount in dollars
        "description": "For drinks and dinner", // Transfer description
        "likesCount": 2                         // Number of likes for this Transfer
      },
      ...
    ]
    '''
    clean_response = []
    transfers_data = {}
    
    '''
    EXTRACTION
    GETs Latest Transfers via a web REQUEST call
    TO-DOs: 
    (1) Separate request call into it's own class that returns a reponsed object ready for transoformation 
        by another class
    (2) Add a input paramater so that the connect URL can be passed from a config file    
    '''
    try:
        request_transfers = uri + "/transfers"
        print('Initializing call and sending request: ' + request_transfers + ' ...')

        try:
          response = requests.get(request_transfers, timeout=(3,3))
        except Timeout:
          print('The request timed out')
        else:
          print('The request did not time out')

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
        
        transfers_data = response.json()
    except HTTPError as http_err:
        print( 'HTTP error occurred: ' + format({http_err}) )
    except Exception as err:
        print( 'Other error occurred: ' + format({err}) ) 
    else:
        print('Success!')
        print( '--- --- ---' )

    '''
    TRANSFORMATION
    Performs removal of all records with status 'failed'
    '''
    for d in transfers_data:
      new_response = {}
      for k in d:
        if k == 'status' and d[k] != 'failed':
            #print(k, d[k]) #remove at will
            new_response.update(d)
            #print(new_response) #remove at will
            #print( '--- --- --- ') #remove at will  
      clean_response.append(new_response)
    #print(clean_response) #remove at will
    
    return clean_response


# >>> >>> >>> * >>> >>> >>> * >>> >>> >>>  ALL POSTS  <<< <<< <<< * <<< <<< <<< * <<< <<< <<<
# POST A NEW TRANSFER
def post_transfer(transfer_data):
    '''
    Part II: implement a method for sending a new payment through the API.

    Using the API, implement a method to create a new Transfer between two accounts. 
    This method should take arguments corresponding to the attributes of the Transfer resource. 
    Before creating the Transfer, your method should confirm that the funds are available in the origin Account. 
    Assume the API will handle updating related resources or return an error if there was failure. 
    ''' 
    try:
        request_post = uri + "/transfers"
        print( request_post )
        print( ' --- --- ---' )
        print( transfer_data )

        print('Initializing call and sending post: ' + request_post + ' ...')
        print( '--- --- ---')

        try:
          response = requests.post( request_post, data=transfer_data )
        except Timeout:
          print('The request timed out')
        else:
          print('The request did not time out')

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
        
        transfer_success = response.json()
 
    except HTTPError as http_err:
        print( 'HTTP error occurred: ' + format({http_err}) )
    except Exception as err:
        print( 'Other error occurred: ' + format({err}) ) 
    else:
        print('Success!')
        print( '--- --- ---' )

    return transfer_success


# >>> >>> >>> * >>> >>> >>> * >>> >>> >>>  CORE PROCESSING   <<< <<< <<< * <<< <<< <<< * <<< <<< <<<
# GENERATE TRANSFER ID
def set_transfer_id(dt):
    '''
    Sets unique ID
    '''
    return int(datetime.datetime.now().strftime("%s")) * 1000 


# PROCESS TRANSFER
def process_transfer(sender_id='1', 
                     recepient_id ='4', 
                     transfer_ammount = 5000,
                     #transfer_ammount = 50000000, #Uncomment to test FUNDING FAILURE
                     description = "Happy Birthday!"):
    '''
    Attempst to create a FUNDS Transfer Record and POST it via the API end-point 
    '''
    recepient_accounts_ids = [] # stores the values of ALL the IDs of every account associated with the RECEPIENT
    recepient_accounts = [] # stores a list of dicts of all the accounts associated with RECEPIENT
    recepient_main_account = {} # stores a dict of the RECEPIENT account, which will receive the transfer funds

    sender_accounts_ids = [] # stores the values of ALL the IDs of every account associated with the SENDER
    sender_accounts = [] # stores a list of dicts of all the accounts associated with SENDER

    transfer_account = [] # stores the accounts with enought funds to make the transfer

    '''
    (1) GET USERs and ACCOUNTs INFORMATION:
        Deny transaction if there are not enough funds
    '''
    #get user ids for SENDER and associated account ids
    sender = get_user(sender_id)
    sender_accounts_ids = sender['accounts']
    sender_accounts = []

    #get user ids for RECEPIENT and associated account ids
    recepient = get_user(recepient_id)
    recepient_accounts_ids = recepient['accounts']
    #print(recepient_accounts_ids)
    recepient_accounts = []

    #get a list of all accounts in system
    all_accounts = get_accounts_all()

    
    '''
    (2) SELECT JUST ONE ACCOUNT ASSOCIATED WITH THE RECEPIENT
    '''  
    # Iterate through all the accounts and select the FIRST one associated 
    # with the RECEPIENT's id
    for d in all_accounts:
        for k in d:
            if k == 'id' and d[k] in recepient_accounts_ids:
                #print(d[k])
                recepient_accounts.append(d)
                # remove and save the first time from the list
                recepient_main_account = recepient_accounts.pop(0)  

    # If we found an account with enough funds for the transfer
    if recepient_main_account:
        print('RECEPIENT MAIN ACCOUNT')
        print(recepient_main_account)
        print('--- --- ---')
        recepient_main_account_id = recepient_main_account.get('id')
        print(recepient_main_account_id)
    elif not recepient_main_account:
        print("There are currenlty no available accounts to send this transaction to!")
        exit()


    '''
    (3) SELECT ALL ACCOUNTS ASSOCIATED WITH THE SENDER
    '''   
    # Iterate through all the accounts and select only the ones associated 
    # with the SENDER's id
    for d in all_accounts:
        for k in d:
            #print(k)
            if k == 'id' and d[k] in sender_accounts_ids:
                sender_accounts.append(d)
    #print(k)
    print('SENDER ACCOUNTS')
    print(sender_accounts)
    print('--- --- ---')
    

    '''
    (4) VALIDATE FUNDS ARE AVAILABLE - Select a SENDER account to fund the transfer:
        *** Deny transaction if there are not enough funds
    '''    
    for d in sender_accounts:
        for k in d:
            # stores the first SENDER account with enough funds available to complete transter
            if k == 'balance' and d[k] >= transfer_ammount:
                #print(d[k])
                transfer_account.append(d)
                break
    # If we found an account with enough funds for the transfer
    if transfer_account:
        print( 'TRANSFER ACCOUNT:' )
        print( transfer_account )
        print( ' --- --- --- ')
        for i in transfer_account:
            transfer_account_id = i.get('id')
            print(transfer_account_id)
    elif not transfer_account:
        print("There are currenlty no available accounts to fund this transaction!")
        exit()

 
    '''
    (5) BUILD THE TRANSFER OBJECT:
    '''
    # stores all the information needed to complete the transfere ( USER and SENDER )
    transfer_data =  {"id": set_transfer_id(datetime.datetime.now()),
                      "status": 'Initiated',
                      "originAccount": transfer_account_id, #identified SENDER ACCOUNT
                      "targetAccount": recepient_main_account_id,
                      "amount": transfer_ammount,
                      "description": description,
                      "initiatedAt": current_time,
                      "completedAt": '',
                      "failedAt": ''} 

    transfer_success = post_transfer(transfer_data)

    return transfer_data, transfer_success


# >>> >>> >>> * >>> >>> >>> * >>> >>> >>>   END CODE   <<< <<< <<< * <<< <<< <<< * <<< <<< <<<


# >>> >>> >>> * >>> >>> >>> * >>> >>> >>>   TEST SCENARIOS   <<< <<< <<< * <<< <<< <<< * <<< <<< <<<
# Sets up a transfer_data object for testing, if needed.
transfer_data =  {"id": set_transfer_id(datetime.datetime.now()),
                  "status": 'Initiated',
                  "originAccount": transfer_account_id,
                  "targetAccount": recepient_main_account_id,
                  "amount": 5000,
                  "description": 'Happy Birthday!',
                  "initiatedAt": datetime.datetime.now(),
                  "completedAt": '',
                  "failedAt": ''}


# TEST 1: Create a TRANSFER object and attempt to POST it
transfer = process_transfer()
#print( ' --- --- --- ')
#print('TRANSFER DATA:') 
#print(transfer)


# TEST 2: POST a TRANSFER object
#transfer = post_transfer(transfer_data)
#print('TRANSFER DATA:') 
#print(transfer)


# TEST 3: GET all TRANSFERS
#transfers_final = get_transfers()
#print( transfers_final )


# TEST 4: GET all USERS
#all_users = get_users()
#print( all_users )


# TEST 5: GET all ACCOUNTS
#all_accounts = get_accounts()
#print( all_accounts )


# TEST 6: Create a UNIQUE ID for each TRANSFER Object
#t_id = set_transfer_id(datetime.datetime.now())
#print('UNIQUE ID:') 
#print(t_id)

