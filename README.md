# TEST TPAGA

Test to apply as backe in tpaga.

## Getting Started
### Prerequisites

> * Python version: 3.6

### Installing

* Created folder for prokect 
``` bash
mkdir tpaga
```
* Create virtalenv
``` bash
mkvirtualenv tpaga
```

* Go to folder project
``` bash
cd tpaga
```

* Clone the repo
``` bash
git clone https://github.com/DIXMA/test_tpaga.git .
```

* Configure settings.py
``` bash
cp tpaga/settings-dist.py tpaga/settings.py
```

* Run migrations
``` bash
python manage.py migrate
```

## Authors

* **Diego Cortés** - *Backend* - [DIXMA](https://github.com/DIXMA)

## EndPoints
> * ListAccounts
>> #### Route: accounts/:
>> Method: GET
>> Description: List alla ccounts on the store
>> Responses:
>>> * 201: List whit all accounts registers 

> * New Account
>> #### Route: accounts/:
>> Method: POST
>> Description: Create new account on the store
>> Form params:
>>> * number: integer, numer for the new account.
>>> * client: integer, client primare key ientification
>>> * balance: float, initial balance
>> Responses:
>>> * 201: Created success
>>> * 400: Bad request, error to serializer object data
>>> * 500: Internal server error

> Update balance an account
>> #### Route: accounts/update/{pk}/:
>> Method: PUT
>> Description: Update an exist account
>> Params:
>>> * pk: integer, primary key to search account for update balance
>> Form params:
>>> * balance: float, positive or negative data for update balance to an account.
>> Responses:
>>> * 201: Updated success
>>> * 404: Not found account by pk
>>> * 400: Bad request, error while search the account
>>> * 500: Internal server error
