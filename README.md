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



