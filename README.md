# DRF_api_example
REST API example for Pizza Order Demo.

Requirements
===================================
1. [Python v2.7.10](https://www.python.org/downloads/)
2. [postgreSQL](https://www.postgresql.org/download/)
3. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)

Running locally
===================================

In order to run DRF_api_example, please install postgreSQL and both the Python runtime and development environments. GraphSpace code, and set up and start the server.  The following instructions should apply to computers running a version of the Linux or OS X operating systems.

1. Download the DRF_api_example code by running `git clone https://github.com/jahandaniyal/DRF_api_example.git`
2. Visit the DRF_api_example directory: `cd DRF_api_example`
3. Create a virtual environment for the project: `virtualenv venv`
4. Start using the virtual environment: `source venv/bin/activate`
5. In `/api_example/settings.py` file, change the postgres user credentials:
 ```
  DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': 'api_example_db',
      'USER': 'postgres',
      'PASSWORD': '123',
      'HOST': 'localhost',
      'PORT': '5432'
    }
  }
```
6. Install all requirements: `pip install -r requirements.txt`
7. Finally, start the Django server: `python manage.py runserver 127.0.0.1:8080`
8. Visit `http://127.0.0.1:8080/orders/`

### REST API Details
The following operations are supported -
- Create a new Order
- Get all orders made by the customers
- Get a specific order
- Update an Order
- Delete an Order
### [Click here to view API Description](https://3x5c8j0mdqavudhhb7owqg-on.drv.tw/api_order.html)

### [Click here to view Video Demonstration](https://www.useloom.com/share/adc43054bcf54f2c80d30fae32b1722a)
