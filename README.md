# Django-Task-Management-AI47labs
A task given by AI47 labs

https://github.com/user-attachments/assets/55d54743-11d9-47f3-a84b-3f04c5241947



## Home Page
![image](https://github.com/user-attachments/assets/13f1ee61-ef16-4c17-9a9f-8ea03fb702f0)

## Task List Page
![image](https://github.com/user-attachments/assets/f7edcadf-1afb-4824-8ac6-238183214442)

## Create Task Page
![image](https://github.com/user-attachments/assets/f6a98e9c-edc2-4872-93b4-9ec249911dd1)

## Update Task Page
![image](https://github.com/user-attachments/assets/041140fe-dd50-4584-b380-472dc07d1310)

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

## Getting Google secret Key and Client
- [Go to Google Console and get the secret and client key](https://console.cloud.google.com/apis/credentials/oauthclient)
- Create New OAuth project
![Screenshot 2024-11-22 231248](https://github.com/user-attachments/assets/9f24a07b-80e0-4d51-b141-32a5800a7847)

- Go to credentials and create Authorized redirect URIs
![Screenshot 2024-11-22 231346](https://github.com/user-attachments/assets/88841332-c632-4b6a-87d3-decc307c8952)

## Enabling admin to manage Oauth keys and Enabling invitation via email
- Modifying the base_site.html in django templates to provide custom admin site
![Screenshot 2024-11-23 135517](https://github.com/user-attachments/assets/bfc49a67-c167-408b-9fd7-92008dfcb312)
![image](https://github.com/user-attachments/assets/e0a02618-502d-4c43-8d01-cfef87849f67)
![image](https://github.com/user-attachments/assets/b2f3d1ef-3170-4891-8809-fccae3459592)

![image](https://github.com/user-attachments/assets/2a064fa3-5b35-40cd-ba5e-a6ef1c2dc53f)







