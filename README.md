README

There are two main files in this project:
 (1) they both run on Python 2.7, and 
 
 (2) to run the code, you must have requests installed on you virtual environment ( or which ever environment you run the code )

 If you wish to integrate the code into your code base, please use file "ellevest_class.py". ( Ideally this file should be called "transfer_class.py". )

 It is recommended that you run this code for this walk-through, the fastes way, and that is by running manual commands using file "ellevest_script.py".  

 The code is well-documented, self-descriptive, and easy to test and step through via the command line.

 WHAT the code DOES:

 (1) Sends requests to API end-points:

 --- To GET a User
 
 --- To GET all Users
 
 --- To GET all Accounts
 
 --- To GET all Transfers
 
 --- To POST a new Transfer


The code also performs various transformations and checks on the data.  Those steps are documented in the code and easy to step through. 

Print statements have been left in the files to facilitate steppiing through the code, since formal test-cases are not included.  Code has been throughly tested.  


WHAT the code DOES NOT DO:

(1) It does not check to see that the SENDER account ID is the same as the RECEPIENTS account ID
(2) It does not subtract from the SENDER's account balance after a transfer has gone through
(3) It does not handle the concept of PREFERED/DEFAULT account for either SENDER or RECEPIENT


SAMPLE API RESONPONSES, abbreviated PAYLOADS:

USERS
```
[
{
	"id": 1,
	"firstName": "Jane",
	"lastName": "Doe",
	"accounts": [
	   4,
	   9
	],
	"transfers": [
	   23,
	   67,
	   103
	],
	"likes": [
	   53
	],
},
...
]
```

ACCOUNTS
```
[
{
	"id": 1,
	"user_Id": 1,
	"accountNumber": "123456789",
	"balance": 3500
},
...
]
```

TRANSFERS
```
[
{
	"status": "Initiated",
	"failedAt": "",
	"originAccount": "2",
	"targetAccount": "6",
	"completedAt": "",
	"amount": "5000",
	"iniatedAt": "12:11:53.345967"
	"id": "1576516310000"
	"description": "Happy Birthday!"
},
...
]
```
