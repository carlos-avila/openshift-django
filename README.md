Django on OpenShift
===================

This git repository helps you get up and running quickly w/ a Django
installation on OpenShift.  The Django project name used in this repo
is 'myproject' but you can feel free to change it.  Right now the
backend is sqlite3 and the database runtime is found in
`$OPENSHIFT_DATA_DIR/db.sqlite3`.

Before you push this app for the first time, you will need to change
the [Django admin password](#admin-user-name-and-password).
Then, when you first push this
application to the cloud instance, the sqlite database is copied from
`wsgi/myproject/db.sqlite3` with your newly changed login
credentials. Other than the password change, this is the stock
database that is created when `python manage.py syncdb` is run with
only the admin app installed.

On subsequent pushes, a `python manage.py syncdb` is executed to make
sure that any models you added are created in the DB.  If you do
anything that requires an alter table, you could add the alter
statements in `GIT_ROOT/.openshift/action_hooks/alter.sql` and then use
`GIT_ROOT/.openshift/action_hooks/deploy` to execute that script (make
sure to back up your database w/ `rhc app snapshot save` first :) )

You can also turn on the DEBUG mode for Django application using the
`rhc env set DEBUG=True --app APP_NAME`. If you do this, you'll get
nicely formatted error pages in browser for HTTP 500 errors.

Do not forget to turn this environment variable off and fully restart
the application when you finish:

```
$ rhc env unset DEBUG
$ rhc app stop && rhc app start
```

Running on OpenShift
--------------------

Create an account at https://www.openshift.com

Install the RHC client tools if you have not already done so:
    
    sudo gem install rhc
    rhc setup

Select the version of python (2.7 or 3.3) and create a application

    rhc app create django python-$VERSION

Add this upstream repo

    cd django
    git remote add upstream -m master git://github.com/openshift/django-example.git
    git pull -s recursive -X theirs upstream master

Then push the repo upstream

    git push

Now, you have to create [admin account](#admin-user-name-and-password), so you 
can setup your Django instance.
	
That's it. You can now checkout your application at:

    http://django-$yournamespace.rhcloud.com

Admin user name and password
----------------------------
Use `rhc ssh` to log into python gear and run this command:

	python $OPENSHIFT_REPO_DIR/wsgi/myproject/manage.py createsuperuser

You should be now able to login at:

	http://django-$yournamespace.rhcloud.com/admin/

Environment Variables
---------------------
OpenShift builds the execution environment which is made available
to application scripts and other code. The environment contains a
variety of variables related to OpenShift and the application itself
which can only be determined at runtime. In addition to the standard
environment variables exposed to the application, cartridges may also
expose custom variables for the application to consume; consult the
specific cartridge documentation for more information about what the
cartridge makes available.

Standard OpenShift Environment Variables
----------------------------------------

* HOME alias for OPENSHIFT_HOMEDIR
* HISTFILE bash history file
* OPENSHIFT_APP_DNS the application’s fully qualified domain name that your cartridge is a part of
* OPENSHIFT_APP_NAME the validated user assigned name for the application. Black list is system dependent.
* OPENSHIFT_APP_UUID OpenShift assigned UUID for the application
* OPENSHIFT_DATA_DIR the directory where your cartridge may store data
* OPENSHIFT_GEAR_DNS the gear’s fully qualified domain name that your cartridge is a part of. May or may not be equal to OPENSHIFT_APP_DNS
* OPENSHIFT_GEAR_NAME OpenShift assigned name for the gear. May or may not be equal to OPENSHIFT_APP_NAME
* OPENSHIFT_GEAR_UUID OpenShift assigned UUID for the gear
* OPENSHIFT_HOMEDIR OpenShift assigned directory for the gear
* OPENSHIFT_REPO_DIR the directory where the developer’s application is "archived" to and will be run from.
* OPENSHIFT_TMP_DIR the directory where your cartridge may store temporary data
* TMPDIR alias for OPENSHIFT_TMP_DIR
* TMP alias for OPENSHIFT_TMP_DIR


Python Environment Variables
----------------------------

* OPENSHIFT_PYTHON_WSGI_APPLICATION Set custom path to the WSGI entry-point, eg. using the ``rhc env set OPENSHIFT_PYTHON_WSGI_APPLICATION=app/altenative-wsgi.py`` command.
* OPENSHIFT_PYTHON_REQUIREMENTS_PATH Set custom path to the pip requirements file, eg. using the ``rhc env set OPENSHIFT_PYTHON_REQUIREMENTS_PATH=requirements/production.txt`` command.