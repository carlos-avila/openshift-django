Running on OpenShift
--------------------

Create an account at https://www.openshift.com

Install the RHC client tools if you have not already done so:
    
    sudo gem install rhc
    rhc setup

Select the version of python (2.7 or 3.3) and create a application:

    rhc app create mydjangoproject python-$VERSION

OpenShift will clone a git repo:

    cd mydjangoproject

Remove unused files:

    rm requirements.txt setup.py wsgi.py

Add this upstream repo:

    git remote add upstream -m master https://github.com/Mandelbrew/openshift-django.git
    git pull -s recursive -X theirs upstream master

Create your Django project:

    django-admin startproject mydjangoproject .

Create a superuser:

    python manage.py createsuperuser

Add STATIC_ROOT to your django settings.py

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

Set the necessary OpenShift environment variables:

    rhc env set DJANGO_MANAGE_PATH=manage.py
    rhc env set OPENSHIFT_PYTHON_WSGI_APPLICATION=mydjangoproject/wsgi.py
    rhc env set OPENSHIFT_PYTHON_REQUIREMENTS_PATH=requirements/development.txt

Update setup with your information:

    vim setup.py

Then push the repo upstream

    git push
	
That's it. You can now checkout your application at:

    http://django-mydjangoproject.rhcloud.com

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