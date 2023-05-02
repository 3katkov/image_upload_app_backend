Image Upload API Project
========================

This project provides a simple Django REST API to allow users to upload images and retrieve thumbnails based on their account type. 
Users can have one of three account types: Basic, Premium, and Enterprise, each with different access levels to image thumbnails and expiring links.

Requirements:
-------------

Naviagte to requirments.txt 

Installation:
-------------

1. Set up a virtual environment for the project:
``` 
$ python -m venv venv
$ source venv/bin/activate
```

2. Install the required packages:
``` 
$ pip install -r requirements.txt
``` 

3. Copy enviroment veriable file and fill in the SECRET_KEY
```
cp env.template .env
```

4. Create a superuser for the Django admin:
``` 
$ python manage.py createsuperuser
``` 

5. Set up new Postgres database called and configurate the DATABASES in imagine_project/settings.py.

6. Load initial data to created database 
``` 
$ python3 manage.py loaddata initial_data.json
``` 

7. Run migrations to set up the database:
``` 
$ python manage.py migrate
``` 

8. Start Docker
9. Build docker image using 

``` 
docker build -t your_image_name .
``` 

10. Run the Docker container:

``` 
docker run -d --name your_container_name -p 8000:8000 your_image_name
``` 

11. Run the development server:
``` 
$ python manage.py runserver
``` 


Usage:
------

1. Visit the Django admin site at http://localhost:8000/admin/ and log in with your superuser credentials.

2. Users can be created at http://127.0.0.1:8000/admin/auth/user/ 

3. Each user, upon registration will automaticaly be assigned to 'Basic' plan. Plans can be changed by visiting http://127.0.0.1:8000/admin/imagine_api/userprofile/<Prodile.ID>/change/ 

4. Logged in Admins are able to create custom plans at http://127.0.0.1:8000/plans/

5. Logged in Admins are ble to see all user profiles (user id and plans) and change the plans for exisiting users at http://127.0.0.1:8000/api/user_profiles/

6. Logged in Users are able to uplad and list their images via HTTP requests via http://127.0.0.1:8000/upload-and-view-images/



Testing:
--------

To run tests, use the following command:
``` 
$ python manage.py test
``` 

This command will execute the test suite and display the results.

Notes:
------

- The API supports Python 3.6 or later.
- Validation, error handling, and performance optimizations are to be considered in the second half of the task. 
















