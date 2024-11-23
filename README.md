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
### Making the task project
```
django-admin startproject task
cd task/
python manage.py startapp taskm #task management app
```

