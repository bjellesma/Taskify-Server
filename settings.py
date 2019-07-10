from dotenv import load_dotenv
import os

load_dotenv()

TEST_VALUE = os.getenv("TEST")
PORT = os.getenv("PORT")