import pymongo
import settings 
from settings import ColorMessages

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
# We try to connect to the database
database_client = pymongo.MongoClient(connect_string, serverSelectionTimeoutMS=3000)
try:
    # an error will be thrown if we can't get the server info
    database_client.server_info()
    print(f'{ColorMessages.OKGREEN}The database connection was successful{ColorMessages.ENDC}')
except Exception as error:
    print(f'{ColorMessages.FAIL}An error occured making a connection to the host\nError: {error}{ColorMessages.ENDC}')

try:
    taskify = database_client[database_name]
except Exception as error:
    print(f'{ColorMessages.FAIL}The database {database_name} was unable to be reached\nError: {error}{ColorMessages.ENDC}')