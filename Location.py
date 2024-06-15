class Location:
    """
    A class representing a geographical location with various attributes.

    Author: Elmira Pour
    Timestamp: 1717701765.2003505
    """

    def __init__(self, x=None, y=None, objectid=None, id=None, typ=None, art=None, standorttyp=None, bezeichnung=None,
                 bezeichnungzusatz=None, kurzbezeichnung=None, strasse=None, plz=None, ort=None, telefon=None, fax=None,
                 email=None, profile=None, sprachen=None, www=None, traeger=None, traegertyp=None, bezugnr=None,
                 gebietsartnummer=None, snummer=None, nummer=None, globalid=None, creationdate=None, creator=None,
                 editdate=None, editor=None):
        """
        Initialize a new Location instance.

        :param x: The X coordinate of the location.
        :param y: The Y coordinate of the location.
        :param objectid: The object ID of the location.
        :param id: The ID of the location.
        :param typ: The type of the location.
        :param art: The art of the location.
        :param standorttyp: The standorttyp of the location.
        :param bezeichnung: The bezeichnung of the location.
        :param bezeichnungzusatz: The bezeichnungzusatz of the location.
        :param kurzbezeichnung: The kurzbezeichnung of the location.
        :param strasse: The street address of the location.
        :param plz: The postal code of the location.
        :param ort: The city of the location.
        :param telefon: The telephone number of the location.
        :param fax: The fax number of the location.
        :param email: The email address of the location.
        :param profile: The profile of the location.
        :param sprachen: The languages spoken at the location.
        :param www: The website of the location.
        :param traeger: The traeger of the location.
        :param traegertyp: The traegertyp of the location.
        :param bezugnr: The reference number of the location.
        :param gebietsartnummer: The area type number of the location.
        :param snummer: The serial number of the location.
        :param nummer: The number of the location.
        :param globalid: The global ID of the location.
        :param creationdate: The creation date of the location.
        :param creator: The creator of the location.
        :param editdate: The edit date of the location.
        :param editor: The editor of the location.
        """

        # Basic properties
        self.x = x
        self.y = y
        self.objectid = objectid
        self.id = id
        self.typ = typ
        self.art = art
        self.standorttyp = standorttyp
        self.bezeichnung = bezeichnung
        self.bezeichnungzusatz = bezeichnungzusatz
        self.kurzbezeichnung = kurzbezeichnung
        self.strasse = strasse
        self.plz = plz
        self.ort = ort
        self.telefon = telefon
        self.fax = fax
        self.email = email
        self.profile = profile
        self.sprachen = sprachen
        self.www = www
        self.traeger = traeger
        self.traegertyp = traegertyp
        self.bezugnr = bezugnr
        self.gebietsartnummer = gebietsartnummer
        self.snummer = snummer
        self.nummer = nummer
        self.globalid = globalid
        self.creationdate = creationdate
        self.creator = creator
        self.editdate = editdate
        self.editor = editor

        # Dictionary to hold any additional properties
        self.extended_properties = {}  # Additional properties not defined in the class

    def __repr__(self):
        """
        Return a string representation of the Location object.

        :return: A string with the version and ID of the location.
        """
        return f"Location Object {self.version} | {self.__str__()}"

    def __str__(self):
        """
        Return a user-friendly string representation of the Location object.

        :return: A string with location details.
        """
        return f"X: {self.x}, Y: {self.y}"

    def __eq__(self, other):
        """
        Compare two Location objects for equality.

        :param other: The other Location object to compare with.
        :return: True if both Location objects are equal, False otherwise.
        """
        if isinstance(other, Location):
            return self.to_dict() == other.to_dict()
        return False

    def __hash__(self):
        """
        Make the Location object hashable.

        :return: An integer hash value of the Location object.
        """
        return hash(tuple(sorted(self.to_dict().items())))

    def __len__(self):
        """
        Return the number of attributes in the Location object.

        :return: An integer count of the Location's attributes.
        """
        return len(self.to_dict())

    def __getitem__(self, key):
        """
        Allow dictionary-like access to the Location's properties.

        :param key: The property name to get.
        :return: The value of the specified property.
        """
        return self.to_dict().get(key)

    def __setitem__(self, key, value):
        """
        Allow dictionary-like setting of the Location's properties.

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
        Get the version of the Location class.

        :return: A string representing the version.
        """
        return f"v1.5"  # The current version of the Location class

    def to_dict(self):
        """
        Convert the Location object to a dictionary.

        :return: A dictionary representation of the Location object.
        """

        location_dict = {
            "x": self.x,  # The X coordinate of the location
            "y": self.y,  # The Y coordinate of the location
            "objectid": self.objectid,
            "id": self.id,
            "typ": self.typ,
            "art": self.art,
            "standorttyp": self.standorttyp,
            "bezeichnung": self.bezeichnung,
            "bezeichnungzusatz": self.bezeichnungzusatz,
            "kurzbezeichnung": self.kurzbezeichnung,
            "strasse": self.strasse,
            "plz": self.plz,
            "ort": self.ort,
            "telefon": self.telefon,
            "fax": self.fax,
            "email": self.email,
            "profile": self.profile,
            "sprachen": self.sprachen,
            "www": self.www,
            "traeger": self.traeger,
            "traegertyp": self.traegertyp,
            "bezugnr": self.bezugnr,
            "gebietsartnummer": self.gebietsartnummer,
            "snummer": self.snummer,
            "nummer": self.nummer,
            "globalid": self.globalid,
            "creationdate": self.creationdate,
            "creator": self.creator,
            "editdate": self.editdate,
            "editor": self.editor
        }

        # Add extended properties to the dictionary
        location_dict.update(self.extended_properties)
        # Return the complete dictionary
        return location_dict

    def to_leaflet(self):
        """
        Convert the Location object to a leaflet JSON(dict).

        :return: A dictionary representation of the JSON leaflet.
        """

        location_dict = {
            "lng": self.x,  # The X coordinate of the location
            "lat": self.y,  # The Y coordinate of the location
            "carrier": self.traeger if self.traeger else '',
            "locName": self.bezeichnungzusatz if self.bezeichnungzusatz else '',
            "shortName": self.kurzbezeichnung if self.kurzbezeichnung else '',
            "street": self.strasse if self.strasse else '',
            "postcode": self.plz if self.plz else '',
            "number": self.telefon if self.telefon else '',
        }

        # Return the complete dictionary
        return location_dict

    def update_properties(self, **kwargs):
        """
        Update the Location object's properties with provided keyword arguments.

        :param kwargs: Dictionary of properties to update.
        """
        # Iterate over the provided properties
        for key, value in kwargs.items():
            # Convert keys to lower-case for Matching
            key = key.strip().lower()
            if hasattr(self, key):  # Check if the property exists in the class
                setattr(self, key, value)  # Update the property value

    def extend_properties(self, **kwargs):
        """
        Add new properties to the Location object that are not originally defined.

        :param kwargs: Dictionary of new properties to add.
        """
        # Iterate over the provided properties
        for key, value in kwargs.items():
            # Convert keys to lower-case for Matching
            key = key.strip().lower()
            if not hasattr(self, key):  # Check if the property does not exist in the class
                self.extended_properties[key] = value  # Add the new property to extended_properties
