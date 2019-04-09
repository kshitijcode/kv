# kv
Web Service Based KV Store

This is a simple web service for In Memory Key Value Store.


**Steps to build the project **

Clone the project 
Navigate to the Project Directory

```pip install virtualenv
virtualenv env
source env/bin/activate`
pip install -r requirements.txt``



**Start the web service** 


`./web-service.py
`


**Perform Actions on the KV Store through WebService**


Set a value : 

 `   client/client.py set --key 3 --value B`
 
 
Get a Value : 
    `client/client.py get --key 3`
    

Watch Key Store for Changes

    ` client/client.py watch
   
     `

    
