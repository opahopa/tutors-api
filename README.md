### tutors Django Rest Framework API

### urls


**movies**
* `/tutors/ GET`  get the list of tutors
* `/tutors/ POST` create tutor
* `/tutors/<id>/ GET` get tutor details
* `/tutors/<id>/ PUT` update tutor
* `/tutors/<id>/ PATCH` edit tutor
* `/tutors/<id>/ DELETE` delete tutor

### installation
1. `viertualenv -v python3 venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python manage.py makemigrations`
5. `python manage.py migrate`

### populate DB
`python manage.py loaddata tutors.json`

### run app
`python manage.py runserver`

### run tests
`python manage.py test`
