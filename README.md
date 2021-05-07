# OSA IIITD Backend

OSA IIITD Backend serves as the authentication backend for the main OSA app as well as other child apps that fall under OSA. This is based on Django Rest Framework: JWT Authentication. Below are the main end points that it offers:

- `/token-auth/` - POST (username, password in body)
- `/core/current_user/` - GET (token in headers)
- `/core/reset_password/` - POST (username in body)
- `/core/verify_email/` - POST (username, token in body)
- `/core/resend_email/` - POST (username in body)
- `/core/change_password/` - POST (username, password in body)
- `/core/edit_profile/` - POST (username, first_name, last_name in body and token in headers)

## Technologies

OSA Backend is powered by a number of technologies:

- [Django] - high-level Python Web framework
- [PostgreSQL] - a powerful, open source object-relational database system
- [DjangoRestFramework] - a powerful and flexible toolkit for building Web APIs

And some simple add ons like django-cors, django-djangorestframework-jwt etc.

## Setup

1. To clone and run OSA Backend, you'll need Git, [Python] v3.0+ and [PostgreSQL] v9+ installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/avisionx/osaiiitd-backend.git

# Go into the repository
$ cd osa-backend

# Install dependencies in a virtualenv
$ pip install -r requirements.txt
```

2. For environment variables check out `.env.examples` in backend folder and create .env file for your own variables

```bash
# Create .env file
$ vim ./backend/.env
```

If you are using gmail smtp server provide email and password in the environment variables.

3. You are good to go just start the server after making migrations.

```bash
# Make migrations
$ python manage.py makemigrations

# Migrate the changes
$ python manage.py migrate

# Start the server
$ python manage.py runserver
```

Server by default starts in development mode at http://127.0.0.1:8000/

## Development

Great setting it all up! Let's contribute now. You'll need to learn Django basics to work on the app. We are using Django Restframework for Api's and JWT token based authentication.

1. Make sure to start from the master branch and update your local repositories.

```bash
# Start from master
$ git checkout master

# Stay updated
$ git pull
```

2. Create a new branch for each bug fix or issue. Rest is basic.

```bash
# Create new branch keep qoutes
$ git checkout -b "YOUR_NEW_BRANCH"
```

## Deployment

Once the code is on the server we can use nginx with gunicorn to host the app. Refer [here](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04) for more information.

## License

MIT

---

[django]: https://docs.djangoproject.com/
[postgresql]: https://www.postgresql.org/
[djangorestframework]: https://www.django-rest-framework.org/
