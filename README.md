###### Deployment Commands (Heroku & Git)

```
heroku login
```
```
heroku create your_app_name
```
```
heroku addons:create heroku-postgresql:hobby-dev
```
```
git add .
```
```
git commit -m "first commit"
```
```
git remote -v
```
```
git push origin main
```
```
git push heroku main
```
```
git log
```

###### Collecting Static Assets 

* From Local
```
python manage.py collectstatic
```
* From Heroku (No need if collected from locally)
```
heroku run python manage.py collectstatic
```

###### Django Commands 

```
heroku run python manage.py migrate
```
```
heroku run python manage.py createsuperuser
```

###### Access Heroku Bash

```
heroku run bash
```
```
ls
```
```
cd /
```
```
ls
```
```
exit
```

###### Access Heroku PostgreSQL Database

```
heroku pg:credentials:url --app your_app_name
```
