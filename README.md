# Django-Task-Management-AI47labs
A task given by AI47 labs

# Objective
Create a task management web app where users can manage personal tasks after logging in with their google account.

# Requirements
- Google Authentication
- Users should be able to create, view, edit and delete tasks
- Each task should have title and description
- Admin Panel, Allow admin to store and manage google OAuth keys for the app
- Enable admin to invite new users by sending an email with a registration link

# Creating the Django project
### Creating and enabling the Virtual Environment and installing requirements
```
python -m venv env
.\env\Scripts\activate
pip install requirements.txt
```
### Making the task project and creating taskmanagement(taskm) app
```
django-admin startproject task
cd task/
python manage.py startapp taskm 
```
### Creating urls.py, forms.py for taskm
![image](https://github.com/user-attachments/assets/5b921869-f7eb-410b-8688-f18d30a1edd9)

### Configuring settings.py and changing different variables
```
SITE_ID=2

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com' 
EMAIL_PORT = 587 
EMAIL_USE_TLS = True 
EMAIL_HOST_USER = 'example@gmail.com' 
EMAIL_HOST_PASSWORD = 'google app access code'

INSTALLED_APPS = [
    ...
    'taskm',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google'
]

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile", 
            "email"
        ],
        "AUTH_PARAMS": {"access_type": "online"}
    }
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)
 
LOGIN_REDIRECT_URL = '/taskm/'
LOGOUT_REDIRECT_URL = "/"
```

## Creating Models, Views, forms and configuring urlpatterns
- Created different models so that user can perform create, view, edit and delete operations
- Created a foreign key relationship such that only one task is associated with one user and in combination with filter provides access to specific user
- filter views so that each users can only perform operations based on their account login with ```@login_required``` decorator for each function
- Configured the urlpatterns so that it routes the user in a proper way to those views
- passing primary key with update and delete operations so that only those users can be updated and deleted
- Created forms for taking user's title and description using django modelforms

## Enabling admin to manage Oauth keys and Enabling invitation via email
- Modifying the base_site.html in django templates to provide custom admin site
  ![Screenshot 2024-11-23 113641](https://github.com/user-attachments/assets/72cc9f8d-3812-40ab-bc82-cce7a0461dc2)




