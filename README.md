# Write It
NaNoWriMo app

Deployed to render: [Write It](https://writeit.onrender.com/)


## Deployment:

Install gunicorn, dj_database_url and psycopg2

Create Procfile
  ```
  web: gunicorn appname.wsgi:application
  ```

Create postgresql db on render [official docs](https://render.com/docs/databases)
Create new webservice
- link github repo
- will autocomplete some settings after detecting type of app
- In settings:
  - enter NAame
  - enter Region
  - select Branch ('main')
  - Root Dir can be blank - default is set to top-level dir
  - Build Command autocompleted, but if not
  ```
  pip install -r requirements.txt
  ```
  - Start Command will be autocompleted but may be wrong, so check Procfile
  ```
  gunicorn appname.wsgi:application
  ```

Set Environment Variables
- Create "DATABASE_URL" variable to link the __internal database url__ from the postgresql
  - Don't forget to migrate
- Add "SECRET_KEY" var
- Add "WEB_CONCURRENCY" var with val 4

Don't forget DEBUG = False