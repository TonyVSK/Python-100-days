# Deploying web application

Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud. This means you can publish your applications on the internet without worrying about the underlying infrastructure, such as servers, storage, and network management. It's ideal for projects of all sizes, from small applications to large scalable systems.

Gunicorn, on the other hand, is an HTTP server for WSGI (Web Server Gateway Interface) in Python. It serves to connect your Python web application (such as one developed with Flask or Django) to the internet. Gunicorn is known for being lightweight and offering good performance with minimal configuration effort.

Now, let's go through the step-by-step process to deploy a site using Heroku and Gunicorn:

## Preparation
1. Develop your application: Make sure your application is working locally. Let's assume you already have this ready.

2. Install Git: Heroku uses Git for deployment management. If you haven't already, install Git on your computer.

3. Install the Heroku CLI: Download and install the Heroku Command Line Interface (CLI) from the official Heroku website. This will allow you to create and manage your Heroku applications directly from the terminal.

4. Create a requirements.txt file: This file lists all your project's Python dependencies. You can create this file by running pip freeze > requirements.txt in your development environment (see the requirements.txt at this folder to see what is necessary to upload our previous blog).

5. Create a Procfile: This is a simple text file that tells Heroku how to run your application. For a web application, you'll likely have something like web: gunicorn app:app, where app:app indicates the module and application that Gunicorn should execute.

6. Configure Gunicorn: Add Gunicorn to your requirements.txt if it's not already there. Just add a line with gunicorn followed by the version.


## Deploy on Heroku
1. Initialize a Git repository: If your project isn't already a Git repository, start one with git init.

2. Log in to Heroku: In the terminal, execute heroku login and follow the instructions to log in to your Heroku account.

3. Create a Heroku application: Run heroku create. This creates a new application on Heroku and adds a new remote to your Git repository.

4. Add and commit your changes: Use git add . to add your changes and git commit -m "commit message" to commit them.

5. Deploy: Deploy your application with git push heroku master. Heroku will detect that you are deploying a Python application, install your dependencies from the requirements.txt, and start your application using the command specified in the Procfile.


At this folder, we have our Profile file, where we context the Heroku what file to load, what server to use (Gunicorn), and what app using (Flask)