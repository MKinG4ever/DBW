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
        # Assign basic properties
        self.username = username
        self.name = name
        self.email = email
        self.mobile = mobile
        self.birthday = birthday
        self.password = password

        # Initialize dictionary to hold any additional properties
        self.extended_properties = {}

    def __repr__(self):
        """
        Return a string representation of the User object.

        :return: A string with the version and username of the user.
        """
        return f"User Object {self.version} | Username: {self.username}"

    def __str__(self):
        """
        Return a user-friendly string representation of the User object.

        :return: A string with user details.
        """
        return f"User(username={self.username}, name={self.name}, email={self.email})"

    def __eq__(self, other):
        """
        Compare two User objects for equality.

        :param other: The other User object to compare with.
        :return: True if both User objects are equal, False otherwise.
        """
        if isinstance(other, User):
            return self.to_dict() == other.to_dict()
        return False

    def __hash__(self):
        """
        Make the User object hashable.

        :return: An integer hash value of the User object.
        """
        return hash(tuple(sorted(self.to_dict().items())))

    def __len__(self):
        """
        Return the number of attributes in the User object.

        :return: An integer count of the User's attributes.
        """
        return len(self.to_dict())

    def __getitem__(self, key):
        """
        Allow dictionary-like access to the User's properties.

        :param key: The property name to get.
        :return: The value of the specified property.
        """
        return self.to_dict().get(key)

    def __setitem__(self, key, value):
        """
        Allow dictionary-like setting of the User's properties.

        :param key: The property name to set.
        :param value: The value to set for the property.
        """
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            self.extended_properties[key] = value

    @property
    def version(self):
        """
        Get the version of the User class.

        :return: A string representing the version.
        """
        return f"v1.2"  # The current version of the User class

    def to_dict(self):
        """
        Convert the User object to a dictionary.

        :return: A dictionary representation of the User object.
        """
        # Create a dictionary with the basic properties
        user_dict = {
            "username": self.username,
            "name": self.name,
            "email": self.email,
            "mobile": self.mobile,
            "birthday": self.birthday,
            "password": self.password
        }
        # Update the dictionary with any extended properties
        user_dict.update(self.extended_properties)

        # Return the complete dictionary
        return user_dict

    def update_properties(self, **kwargs):
        """
        Update the User object's properties with provided keyword arguments.

        :param kwargs: Dictionary of properties to update.
        """
        # Iterate over the provided properties
        for key, value in kwargs.items():
            # Convert key to lower-case for matching
            key = key.lower()
            if hasattr(self, key):  # Check if the property exists in the class
                setattr(self, key, value)  # Update the property valu

    def extend_properties(self, **kwargs):
        """
        Add new properties to the User object that are not originally defined.

        :param kwargs: Dictionary of new properties to add.
        """
        # Iterate over the provided properties
        for key, value in kwargs.items():
            # Convert key to lower-case for matching
            key = key.lower()
            if not hasattr(self, key):  # Check if the property does not exist in the class
                self.extended_properties[key] = value  # Add the new property to extended_properties
