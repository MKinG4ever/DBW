class User:
    """
    A class representing a user with various attributes.

    Author: Elmira Pour
    Timestamp: 1717701765.2003505
    """

    def __init__(self, username=None, name=None, email=None, mobile=None, birthday=None, password=None):
        """
        Initialize a new User instance.

        :param username: The username of the user.
        :param name: The full name of the user.
        :param email: The email address of the user.
        :param mobile: The mobile number of the user.
        :param birthday: The birthday of the user in 'YYYY-MM-DD' format.
        :param password: The password for the user.
        """
        # Basic properties
        self.username = username
        self.name = name
        self.email = email
        self.mobile = mobile
        self.birthday = birthday
        self.password = password
        # Dictionary to hold any additional properties
        self.extended_properties = {}

    @property
    def version(self):
        """
        Get the version of the User class.

        :return: A string representing the version.
        """
        return f"v1.1"  # The current version of the User class

    def to_dict(self):
        """
        Convert the User object to a dictionary.

        :return: A dictionary representation of the User object.
        """
        # The basic properties as a dict
        user_dict = {
            "username": self.username,
            "name": self.name,
            "email": self.email,
            "mobile": self.mobile,
            "birthday": self.birthday,
            "password": self.password
        }
        # Add extended properties to the dictionary
        user_dict.update(self.extended_properties)
        # Return the complete dictionary
        return user_dict

    def update_properties(self, **kwargs):
        """
        Update the User object's properties with provided keyword arguments.

        :param kwargs: Dictionary of properties to update.
        """
        # Update existing properties
        for key, value in kwargs.items():
            # Convert key to lower-case for matching
            key = key.lower()
            if hasattr(self, key):  # Check if the property exists in the class
                setattr(self, key, value)  # Update the property value

    def extend_properties(self, **kwargs):
        """
        Add new properties to the User object that are not originally defined.

        :param kwargs: Dictionary of new properties to add.
        """
        # Add new properties not defined in the class
        for key, value in kwargs.items():
            # Convert key to lower-case for matching
            key = key.lower()
            if not hasattr(self, key):  # Check if the property does not exist in the class
                self.extended_properties[key] = value  # Add the new property to extended_properties
