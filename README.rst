
1- pip install -r requirements.txt 
2- create a database in postgresql name it 'villasdb'
3- update the password you've chosen in settings.py /(database setting)
in cmd or git shell (cd path/to/projectroot)
4-python manage.py syncdb   // create supersuer and password 
5-python manage.py schemamigration vills --initial
6-python manage.py migrate villas
7-python manage.py runserver
8- open localhost/admin (username and password u create with syncdb) and add  villas (name and area) 
9- add residents to some villas (not all)
10- add users ( choose username to be equal to an available resident name) and fill user first and last name 
11- open localhost in your browser
