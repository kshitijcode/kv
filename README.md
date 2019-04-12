# kv
Key Value Store  Web Service

This is a simple web service which uses Flask and in a in Memory Key Value Store.
It can set,update, get and watch for values in realtime.
This also uses socket.io for watching instant changes to the datastore.


CI/CD Source Code : https://github.com/kshitijcode/kv-ci

Jenkins Server : http://134.209.10.141:8080


This project contains three sections: 

service


client - All the client code resides in the client folder



tests - Consists of all Test code 




**Steps to build the project**

 Clone the project
  
 Navigate to the Project Directory

 Execute the following commands:
 
 `pip install virtualenv`
 
 `virtualenv env`
 
 `source env/bin/activate`
 
 `pip install -r requirements.txt`




**Start the web service** 



`./app.py
`



**Perform Actions on the KV Store through WebService**


Set a value : 


 `client/client.py set --key 3 --value B`
 
 
 
Get a Value : 



    client/client.py get --key 3
    

Watch Key Store for Changes



    client/client.py watch

    
