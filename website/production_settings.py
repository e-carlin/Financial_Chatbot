import dj_database_url

DATABASES = {'default': dj_database_url.config(default="postgres://horppihyabccmv:914fa0a2e87471f9b408799f0432a6a96d532d8eea8a15fe3e957f62b65fd61b@ec2-54-225-68-71.compute-1.amazonaws.com:5432/d112fanfi0cnrf")}

DEBUG = False