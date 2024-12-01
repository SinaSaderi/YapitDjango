# second_server

Welcome to **second_server**, a Django project generated with **Yapit**. This README provides an overview of the project and guides you through the process of deploying it to a server. Yapit is an AI-powered platform for building scalable and production-ready projects with Django and other modern frameworks.

[![Yapit](https://custom-icon-badges.demolab.com/badge/Generated_by-Yapit-blue.svg?logo=yapit)](https://yapit.ai)
[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## Table of Contents

- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running Locally](#running-locally)
- [Deployment Guide](#deployment-guide)
  - [Step 1: Clone the Repository](#step-1-clone-the-repository)
  - [Step 2: Install Dependencies](#step-2-install-dependencies)
  - [Step 3: Configure Environment Variables](#step-3-configure-environment-variables)
  - [Step 4: Set Up Database](#step-4-set-up-database)
  - [Step 5: Configure Gunicorn and Nginx](#step-5-configure-gunicorn-and-nginx)
  - [Step 6: Run Migrations and Collect Static Files](#step-6-run-migrations-and-collect-static-files)
  - [Step 7: Start the Server](#step-7-start-the-server)

## Getting Started

### Project Structure

The generated project contains the following structure:

```
project_name/
|-- manage.py
|-- project_name/
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- app_name/
|-- static/
|-- templates/
```

### Requirements

- Python 3.8+
- Django 3.2+
- Git
- PostgreSQL (optional, but recommended for production)
- Nginx (for serving static files)
- Gunicorn (for running the Django application)

## Installation

### Running Locally

1. Clone the repository:

   ```sh
   git clone https://github.com/username/repository.git
   cd repository
   ```

2. Create and activate a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Set up environment variables and run migrations:

   ```sh
   cp .env.example .env
   python manage.py migrate
   ```

5. Run the local development server:

   ```sh
   python manage.py runserver
   ```

## Deployment Guide

### Step 1: Clone the Repository

First, log into your server and clone the project repository from GitHub:

```sh
git clone https://github.com/username/repository.git
cd repository
```

### Step 2: Install Dependencies

1. Install system-level dependencies:

   ```sh
   sudo apt update
   sudo apt install python3-pip python3-venv nginx
   ```

2. Create a virtual environment and install Python dependencies:

   ```sh
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

### Step 3: Configure Environment Variables

Create a `.env` file in the root directory of your project, or edit the existing `.env.example` file:

```sh
cp .env.example .env
nano .env  # Edit the environment variables such as DATABASE_URL, SECRET_KEY, etc.
```

### Step 4: Set Up Database

Ensure your database (e.g., PostgreSQL) is installed and running. Update the `.env` file with your database settings, and apply the migrations:

```sh
python manage.py migrate
```

### Step 5: Configure Gunicorn and Nginx

1. Install Gunicorn in your virtual environment:

   ```sh
   pip install gunicorn
   ```

2. Create a Gunicorn systemd service file to manage the Django application:

   ```sh
   sudo nano /etc/systemd/system/project_name.service
   ```

   Add the following configuration:

   ```ini
   [Unit]
   Description=gunicorn daemon for project_name
   After=network.target

   [Service]
   User=your_user
   Group=www-data
   WorkingDirectory=/path/to/your/repository
   ExecStart=/path/to/your/repository/venv/bin/gunicorn --workers 3 --bind unix:/path/to/your/repository/project_name.sock project_name.wsgi:application

   [Install]
   WantedBy=multi-user.target
   ```

3. Start and enable the Gunicorn service:

   ```sh
   sudo systemctl start project_name
   sudo systemctl enable project_name
   ```

4. Configure Nginx to act as a reverse proxy for your application:

   ```sh
   sudo nano /etc/nginx/sites-available/project_name
   ```

   Add the following configuration:

   ```nginx
   server {
       listen 80;
       server_name your_domain.com;

       location = /favicon.ico { access_log off; log_not_found off; }
       location /static/ {
           root /path/to/your/repository;
       }

       location / {
           include proxy_params;
           proxy_pass http://unix:/path/to/your/repository/project_name.sock;
       }
   }
   ```

5. Enable the Nginx configuration and restart:

   ```sh
   sudo ln -s /etc/nginx/sites-available/project_name /etc/nginx/sites-enabled
   sudo nginx -t  # Check for syntax errors
   sudo systemctl restart nginx
   ```

### Step 6: Run Migrations and Collect Static Files

Run database migrations and collect static files for production:

```sh
python manage.py migrate
python manage.py collectstatic
```

### Step 7: Start the Server

Ensure that everything is running as expected:

```sh
sudo systemctl restart project_name
sudo systemctl restart nginx
```

You should now be able to access your Django project at `http://your_domain.com`.

## Additional Notes

- Make sure to configure SSL using [Let's Encrypt](https://letsencrypt.org/) for production deployments.
- Adjust the number of Gunicorn workers based on your server's CPU capacity.
- Regularly monitor the server logs (`/var/log/nginx/` and `/var/log/syslog`) for troubleshooting.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Happy coding!** 🎉 Feel free to contribute or report any issues.

