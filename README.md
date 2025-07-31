# Assignment Junior Integration Engineer

# Prerequisites
## Create a .env file with the following secrets
| BASE_URL      | The URL of the service               |
|---------------|--------------------------------------|
| MASTER_CLIENT | The client id of the master data     |
| MASTER_SECRET | The secret of the master data        |
| TARGET_CLIENT | The client id of the target platform |
| TARGET_SECRET | The secret of the target platform    |
| CRON          | cron format of the scheduler         |

# Install the packages

```sh
pip install -r requirements.txt
```

## How to run this script
```sh
python ./src/main.py
```

## Design pattern
The configuration class is an example of a class that only needs 1 instance
of this application.

I've chosen the Singleton pattern because this creational pattern solves this problem in an easy elegant way.

I did not choose DI or dependency injection. For me it would be way to overkill for a project of this size. Complex mutable state that is hidden by a singleton is often something that you don't want but  this is not the case.

I made this implementation in a more 'Pythonic' way than a classic Singleton.
