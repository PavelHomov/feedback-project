### 📒API doc:

[Examples](https://github.com/PavelHomov/feedback-project/blob/master/api_yamdb/static/redoc.yaml) 👈

### About:
The feedback-project is a review-aggregation project for film, television, book, music. The YaMDb collect online reviews from users. The users upload their reviews to the movie(TV-show,book,music) page on the website.The YaMDb keeps track of all the reviews counted for each film. An average score on a 0 to 10 scale is also calculated.
### Developers:
- [Iskander Ryskulov](https://github.com/IskanderRRR)
- [Pavel Homov](https://github.com/PavelHomov)
- [Georgy Popov](https://github.com/Georrgeee)

### Applied technologies:
- Python
- Django
- Django Rest Framework
- Simple-JWT
- Git

### User Roles
- Anonymous - can view descriptions of works, read reviews and comments.

- Authenticated user (user) - can read everything, like Anonymous, can additionally publish reviews and rate works (films / books / songs), can comment on other people's reviews and rate them; can edit and delete their reviews and comments.

- Moderator - the same rights as an Authenticated User plus the right to delete and edit any reviews and comments.

- Administrator (admin) - full rights to manage the project and all its contents. Can create and delete works, categories and genres. Can assign roles to users.

- Django Administrator - Same rights as the Administrator role.

### Template for filling an env file:

1. Specify the secret key for settings.py:
```
SECRET_KEY=default-key
```
2. We indicate that we are working with postgresql:
```
DB_ENGINE=django.db.backends.postgresql
```
3. Specify the name of the database:
```
DB_NAME=postgres
```
4. Specify the login to connect to the database:
```
POSTGRES_USER=login
```
5. Specify the password to connect to the database:
```
POSTGRES_PASSWORD=password
```
6. Specify the name of the service (container):
```
DB_HOST=db
```
7. Specify the port to connect to the database:
```
DB_PORT=5432
```
8. NGINX:
```
HOST=<server_name>
PORT=<port>
UPSTREAM=<proxy_pass>
```

To launch the application, follow these steps:

1. Clone the repository.
2. Go to the infra folder and run docker-compose.yaml (with Docker installed and running)
```
docker-compose up
```
3. To reassemble containers, run the command:
```
docker-compose up -d --build
```
4. In the web container, perform migrations:
```
docker-compose exec web python manage.py migrate
```
5. Create a superuser:
```
docker-compose exec web python manage.py createsuperuser
```
6. Collect static:
```
docker-compose exec web python manage.py collectstatic --no-input
```
The project has been launched: [localhost](http://localhost/admin/)

## Loading test values into the database

To upload test values to the database, go to the project directory and copy the database file to the application container:
```
docker cp <DATA BASE> <CONTAINER ID>:/app/<DATA BASE>
```
Go to the application container and upload the data to the database:
```
docker container exec -it <CONTAINER ID> bash
python manage.py loaddata <DATA BASE>
```
