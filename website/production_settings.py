import dj_database_url

DATABASES['default'] =  dj_database_url.config()

DEBUG = True # For now very insecure for prod TODO: Make False