from dotenv import load_dotenv
import os

load_dotenv()

TEST_VALUE = os.getenv("TEST")
PORT = os.getenv("PORT")
DBTYPE = os.environ["DBTYPE"]
DBUSER = os.getenv("DBUSER")
DBPASSWORD = os.getenv("DBPASSWORD")
DBHOST = os.getenv("DBHOST")
DBPORT = os.getenv("DBPORT")
DBNAME = os.getenv("DBNAME")

class ColorMessages:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'