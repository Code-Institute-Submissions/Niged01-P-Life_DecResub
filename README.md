# P-Life

[To view live site click here](https://p-life-01.herokuapp.com/)

## Introduction
P-life is a forum that has been created for Pilots to get togehter and discuss everything piloting.
Being a pilot out on the road can get lonely, creating this community in theory should make it easier for 
Pilots to get information easier and gain friendships along the way. It is a forum for newby Pilots and those more experienced.

insert responsive image here later-----

## Contents



## The User Experience 
- The approach I have taken to the design of this forum, is clear simplicity with image detail for reference and easy navigation.
- The progress of The User Experienve stories can be viewd [here.](tba)

### Admin

- As Site Admin, I can approve or disapprove forum posts and comments so that I can filter out objectionable Content.
- As Site Admin I can create, post, edit or delete forum posts so that I can share and manage my forum posts.
- As Site Admin I can have all the functionality of a member user so that I can be involved with the forum site.

### General User

- As a general user, I can view a list of forum topics so that I can select one to read.
- As a general user, I can click on a post so that I can read the enitre post.
- As a general user, I can view the number of likes on a posts, to see which is most popular.
- As a general user, I can view comments on individual posts enabling viewing of the full conversation.
- As a general user, I can register for an account to take full contributor site usage.

### Contributor user

- As a contributor user, I can create, posts and add an image.
- As a contributor user, I can like/unlike blogs so that I can interact with the content.
- As a contributor user, I can leave comments on forum posts, so that the user can be involved with the conversation.

### Colour Scheme
I instantly had an idea of sky and aviation colors for the forum site palette. With that in mind I reseached images online
and came accross this palette that fits perfectly with what I had envisioned. I have used this accross the Typography aswell.

![Colour scheme used for site](./assets/documentation/colorpalette.webp)


### Typography

- I used sans-serif for it's simplicity clean lines and legiability.

## Technologies used
- HTML
- CSS
- JavaScript
- Python/Django
    - The below modules were used for the development of the project.
        *   asgiref==3.5.2
        *   asgiref==3.5.2
        *   cloudinary==1.29.0
        *   dj-database-url==0.5.0
        *   dj3-cloudinary-storage==0.0.6
        *   Django==3.2.14
        *   django-allauth==0.51.0
        *   django-crispy-forms==1.14.0
        *   django-etc==1.3.1
        *   django-hitcount==1.3.5
        *   django-resized==1.0.1
        *   django-summernote==0.8.20.0
        *   django-taggit==3.0.0
        *   django-tinymce==3.4.0
        *   gunicorn==20.1.0
        *   oauthlib==3.2.0
        *   Pillow==9.2.0
        *   psycopg2==2.9.3
        *   PyJWT==2.4.0
        *   python3-openid==3.2.0
        *   pytz==2022.1
        *   requests-oauthlib==1.3.1
        *   sqlparse==0.4.2







## Deployment

- Initial deployment was made early on in the process of making this project to avoid any unforseen errors when deploying and causing stress if time was limited.

### Deployment through Heroku
1. Sign up / Log in to Heroku

2. From the main Heroku Dashboard page select 'New' and then 'Create New App'

3. Give the project a name and select a suitable region, then select create app. The name for the app must be unique. This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the resources tab.

4. Add the database to the app, in the add-ons section search for 'Heroku Postgres', select the package that appears and add 'Heroku Postgres' as the database

5. Navigate to the setting tab, within the config vars section copy the DATABASE_URL to the clipboard for use in the Django configuration.

6. Within the django app repository create a new file called env.py - within this file import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from Heroku. The line should appear as os.environ["DATABASE_URL"]= "Paste the link in here"

7. Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here"
Add the secret key just created to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value you created as the VALUE

8. In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
insert the line if os.path.isfile("env.py"): import env
remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} ensure the correct indentation for python is used.

9. In the terminal migrate the models over to the new database connection
Navigate in a browser to cloudinary, log in, or create an account and log in.

10. From the dashboard - copy the CLOUDINARY_URL to the clipboard
in the env.py file created earlier - add os.environ["CLOUDINARY_URL"] = "paste in the Url copied to the clipboard here"

11. In Heroku, add the CLOUDINARY_URL and value copied to the clipboard to the config vars
Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
this key value pair must be removed prior to final deployment

12. Add the cloudinary libraries to the list of installed apps, the order they are inserted is important, 'cloudinary_storage' goes above 'django.contrib.staticfiles' and 'cloudinary' goes below it.

13. In the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

14. Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]

15. Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com

16. In your code editor, create three new top level folders, media, static, templates

17. Create a new file on the top level directory - Procfile

18. Within the Procfile add the code - web: guincorn PROJECT_NAME.wsgi

19. In the terminal, add the changed files, commit and push to GitHub

20. In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.

Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

### Forking the Gihub Repository

1. By forking the GitHub Repository, you will be able to make a copy of the original repository on your own GitHub account, allowing you to view and/or make changes without affecting the original repository by using the following steps:

2. Log in to GitHub and locate the GitHub Repository At the top of the Repository (not top of page), just above the "Settings" button on the menu, locate the "Fork" button. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the GitHub Repository Under the repository name.

2. Click "Clone or download". 

3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link. 

4. Open Git Bash.  

5. Change the current working directory to the location where you want the cloned directory to be made. 

6. Type git clone, and then paste the URL you copied in Step 3.

## Credits
- Code institute's Django blog walkthrough, was my initial confidence booster as that was the first time I had encountered the Django framework, so the walkthrough was used to  help guide me through the initial setup.
- Youtube forum tutorial found [here](https://www.youtube.com/watch?v=YXmsi13cMhw)
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/configuration.html) configuration of the email in the registration form.
- iColorPalette for the color [Palette](./assets/documentation/colorpalette.webp)

### Acknowledgements
- Code institute for course material and content.
- The slack community for their help and support.
- My mentor for advise and assistance on planning and submission feedback.