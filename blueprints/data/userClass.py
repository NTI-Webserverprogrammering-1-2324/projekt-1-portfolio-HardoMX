"""
This module contains the User class for representing a user in the system.
"""
from flask_login import UserMixin

class User(UserMixin):
    """Represents a user in the system.

    Attributes:
        id (str): The unique identifier for the user.
    """
    id = ""
