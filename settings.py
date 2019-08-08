from dotenv import load_dotenv
import os

load_dotenv()

TEST_VALUE = os.environ["TEST"]
PORT = os.environ["PORT"]
DBTYPE = os.environ["DBTYPE"]
DBUSER = os.environ["DBUSER"]
DBPASSWORD = os.environ["DBPASSWORD"]
DBHOST = os.environ["DBHOST"]
DBPORT = os.environ["DBPORT"]
DBNAME = os.environ["DBNAME"]

class ColorMessages:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'