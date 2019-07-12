import pymongo
import settings 

# NOTE testing
import pprint

database_type = settings.DBTYPE
database_user = settings.DBUSER
database_password = settings.DBPASSWORD
database_host = settings.DBHOST
database_port = settings.DBPORT
database_name = settings.DBNAME
# Connect to database
connect_string = f'{database_type}://{database_user}:{database_password}@{database_host}:{database_port}/{database_name}'
try:
    database_client = pymongo.MongoClient(connect_string)
    print(f'A successful database connection\nstring: {connect_string}\ndb: {database_client}')
except Exception as error:
    print(f'An error occured making a connection to the host\nError: {error}')

lists = database_client['taskify']

pprint.pprint(lists['list'].find_one())