from models.mongobase import taskify
import pprint
# Note: security modules are used to help validate users for logging in
from werkzeug.security import generate_password_hash, check_password_hash

class UsersModel():

    users_collection = taskify['users']

    @classmethod
    def check_user(cls, email):
        """
        Check if the user's email already exists in the database
        return true if there is no user
        return false if there is an existing user
        """
        user = cls.users_collection.find_one(
            {
                'email':email
            }
        )
        if not user:
            return True
        return False

    @classmethod
    def register(cls, **kwargs):
        """
        Register user and insert into database
        """
        username = kwargs.get('username')
        email = kwargs.get('email')
        password = kwargs.get('password')
        # Create password hash
        password = generate_password_hash(password, method='sha256')
        lists_collection = taskify['lists']
        new_user = {
            "username": username,
            "email": email,
            "password": password
        }
        # seperate user object so that we don't expose the password
        user = {
            "username": username,
            "email": email
        }
        user_id = cls.users_collection.insert_one(new_user).inserted_id
        return user, user_id

    @classmethod
    def authenticate(cls, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')
        
        # if one of email or password is not filled in, return a null object
        if not email or not password:
            return None

        # Find user to authenticate by email
        
        user = cls.users_collection.find_one(
            {
                'email':email
            }
        )

        # if no user was found or the passwords don't match, return a null object
        if not user or not check_password_hash(user["password"], password):
            return None

        # if all of our tests passes, return the proper user object
        return user

    def to_dict(self):
        return dict(id=self.id, email=self.email)