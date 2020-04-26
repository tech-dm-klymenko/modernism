# Modernism in Architecture

## Setup the project

The project is build with [Wagtail](https://wagtail.io/), a CMS powered by [Django](https://www.djangoproject.com/).


### Prerequisites
- Python version >= 3.6

To check the Python version on your system, run
```bash
$ python --version
Python 3.7.2
```
or 
```bash
$ python3 --version
Python 3.7.2
```

If an older version than 3.6 or nothing is found you will need to [update or install Python](https://realpython.com/installing-python/) first. 

### Install the project on your machine

#### Get the repository

```bash
$ git clone git@github.com:normade/modernism.git 
```

#### Setup a virtual environment and activate it

```bash
$ python -m venv env
$ source env/bin/activate
```

#### Install requirements
```bash
$(env) python -r requirements.txt
```

#### Run migrations to setup the database 
```bash
$(env) cd modernism/
$(env) python manage.py migrate
```

#### Insert testdata
```bash
$(env) python manage.py add_testdata
```

#### Run the development server
```bash
$(env) python manage.py runserver
```

#### Admin login
You can login into the project's admin with your created superuser at `http://127.0.0.1:8000/admin`.



