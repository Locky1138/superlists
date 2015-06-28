# superlists
tdd_python superlists

Project from Test-Driven Development with Python (http://www.amazon.com/Test-Driven-Development-Python-Harry-Percival/dp/1449364829/ref=tmm_pap_title_0?ie=UTF8&qid=1433777033&sr=8-2)

to-do:
* resolve confusion between sitename (url) and application name (superlists).
    ex: in gunicorn-SITENAME.conf we have to --bind unix:/tmp/URL.socket to superlists.wsgi:application
* add provisioning:
+ create application user
+ install git and nginx
* additional deployment
+ configure nginx and gunicorn
+ start nginx and gunicorn services

Server-Side Python Path:
/home/site_user/miniconda3/envs/superlists/bin/python
