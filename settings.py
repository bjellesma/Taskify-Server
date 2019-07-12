from dotenv import load_dotenv
import os

load_dotenv()

TEST_VALUE = os.getenv("TEST")
PORT = os.getenv("PORT")
DBTYPE = os.getenv("DBTYPE")
DBUSER = os.getenv("DBUSER")
DBPASSWORD = os.getenv("DBPASSWORD")
DBHOST = os.getenv("DBHOST")
DBPORT = os.getenv("DBPORT")
DBNAME = os.getenv("DBNAME")