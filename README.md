# Contact-App
Zoho Test


# Contact App

Foobar is a Python library for dealing with word pluralization.

## Installation

### Download here [project](https://github.com/Madishetty-Neeraj/Contact-App/archive/refs/heads/main.zip) to run locally

```bash
unzip Contact-App-main.zip -d
```
### Create Virtual Enviornment
```bash
python3 -m venv con_ENV

### Activate virtual enviornment by
```bash
source con_ENV/bin/activate
```

### move to directory `Contact-App-main-master`
```bash
cd Content-App-main-master
```
### Install required modules from `requriments.txt`

```bash
pip install -r requirements.txt
```

Run the application by following command
```bash
python main.py
```
1.### ***GET REQUEST ***
  1. Get 'Login' at
[http://localhost:5000/login]
(http://localhost:5000/login)
  2. Get 'Register' at
 [http://localhost:5000/signUp]
 (http://localhost:5000/signUp)
   2. Get 'Account' at
 [http://localhost:5000/account]
 (http://localhost:5000/account)
   2. Get 'AddContact' at
[http://localhost:5000/addcontact] (http://localhost:5000/addcontact)
    2. Get 'Logout' at
 [http://localhost:5000/logout]
 (http://localhost:5000/logout)

#### Json Schemas for
1.  User Registration

       ```json
       {
           "username" : "String: email",
           "password" : "String: password",
           "Confirm_password" :"String: confirm_password",
           "secret" :"String: secret",
       }
      ```

2.Update user details

       ```json
       {
           "username" :"String :name",
           "email" :"String :email",
       }
       ```

3.  Adding new Contacts

        ```json
            {
                 "name" :"String :name",
                 "pnumber" :"String :Phone Number",
                 "email" : "email",
            }
            ```
    
