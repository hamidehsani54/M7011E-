#Your Personal Trainer

## Get Django Ready
Install and set up virt. env. with django.<br>
<a href="https://realpython.com/django-setup/">HOW TO INSTALL AND SET UP DJANGO</a><br><br>

start the server by typing:<br>
  python manage.py runserver <specify_port><br>
from the project dir<br>
To use the admin pages you need to create a super-user, do this by running this command<br>
  python manage.py createsuperuser<br><br>

You might have to run these commands to init all the db files (you probobly dont have to do this)<br>
  python manage.py makemigrations<br>
  python manage.py migrate<br><br>

Then you should be able to access the site on<br>
  http://127.0.0.1:<your_selected_port>/<br><br>
  

## Required Packages
    <li>authenApp</li>
    <li>embed_video</li>
    <li>django.contrib.admin</li>
    <li>django.contrib.auth</li>
    <li>django.contrib.contenttypes</li>
    <li>django.contrib.sessions</li>
    <li>django.contrib.messages</li>
    <li>django.contrib.staticfiles</li>
    <li>widget_tweaks</li>
    <li>django_htmx</li>
 
<h4>Install easely with "pip install <PackageName>"</h4>

## Grade 3 requrements (our target)

<h1>Front end</h1>
<li>At least 5 pages that are "responsive in design"</li>
<li>Must contain at least 1 image across all pages</li>
see any of the exercise pages<br><br>
<li>Must contain at least 1 video across all pages</li>
see videos page under exercise menue<br><br>
<li>Must contain at least 1 table across all pages</li>
see exercise pages<br><br>
<li>Must contain at least 1 collapsable "div" element</li>
see about page<br><br>
<li>Must contain at least 1 drop-down list</li>
see trainerSite<br><br>
<li>At least 1 page that shows the use of authentication</li>
see reset email<br><br>
<li>At least 2 pages that show the use of authorization</li>
see views, some pages require you to be logged in<br><br>
<li>Must show CRUD Links to an external site.operations</li>
<li>At least one form submission that shows the authorization</li>
see trainerSite<br><br>
<li>Must have at least 1 navigation menu</li>
see nav bar<br><br>
<li>It must have at least 1 sub-menu inside one of the main navigation menu</li>
see nav bar<br><br>
<li>Client-side rendering</li>
<li>Must have at least 5 calls to the back end that are done asynchronously to an external site.</li>
checking if usernames are taken asynchronously for example and password match<br><br>
<li>Out of these 5, at least 2 calls are "protected" (authentication and/or authorization required)</li>
this might be a missing requirement<br><br>
<h1>Back end</h1>
<li>Database</li>
<li>Must use a database with at least 5 tables</li>
see models.py<br><br>
<li>Must have the following relations</li>
<li>one to one</li>
Profile table has this<br>
<li>one to many</li>
TrainingPrograms used to have this with a foreign key, but in a last minute change we decided that a many to many would be more fitting, therefore we dont currently have a one to many. If you are intrested in the one to many implementation you can check previous commits.<br><br>
<li>many to many</li>
TrainingPrograms has this<br><br>
<li>(if using a relational database) Must be a 3NF compliantLinks to an external site.</li>
<li>Authentication</li>
<li>Support the creation of users, using email and password</li>
<li>Ability to log in, log out, and reset passwords</li>
<li>Authorization</li>
<li>Use Access control with at least three different roles</li>
trainer, superuser, user<br><br>
<li>Ex: Regular User, Admin, Super User</li>
<li>Deployment</li>
<li>Deploy to a web server</li>
we did not have to do this, it is run localy<br><br>
<li>Use Git</li>
you are here :)<br><br>
<li>Must use Git, and must show gradual progress</li>
<li>Performance evaluation</li>
look at the end of views.py, I also did a performance check with google lightHouse first one with filtering query, then one where i queried all and then filtered. The one where i filtered directly in the query is faster as it doesn't have to get all the entries, only the matching ones.<br><br>
<li>Must do at least two performance evaluations</li>
<li>Ex 1: show page load loads across two different implementations, explain why 1 is better than the other</li>
<li>Ex 2: show database query results or query forming that shows which is better, and explain why so</li>

i did one quering all then filter vs filter query and one where i compared django ORM with SQL here ORM was faster<br><br>
