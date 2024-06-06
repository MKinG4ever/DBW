import csv
from typing import Dict, Any


class Reader:
    """
    Class to read various file types (CSV, KML, GeoJSON, Shapefile) and return their contents.

    Author: Elmira Pour
    Timestamp: 1717701765.2003505
    """

    def __init__(self, path: str):
        """
        Initialize the Reader with the path to the file.

        :param path: The path to the file to be read.
        """
        self.path = path
        self.extension = path.split('.')[-1]

    @property
    def version(self):
        """
        Get the version of the Reader class.

        :return: A string representing the version.
        """
        return f"v1.2"  # The current version of the Reader class

    def read(self) -> Dict[str, Any]:
        """
        Read the file based on its extension and return its contents.

        :return: A dictionary containing the name of the file and its data.
        """
        if self.extension == 'csv':
            return self._read_csv()
        elif self.extension == 'kml':
            return self._read_kml()
        elif self.extension == 'geojson':
            return self._read_geojson()
        elif self.extension == 'shp':
            return self._read_shapefile()
        else:
            raise ValueError(f"Unsupported file extension: {self.extension}")

    def _read_csv(self) -> Dict[str, Any]:
        """
        Read a CSV file and return its contents as a dictionary.

        :return: A dictionary containing the name of the file and its data.
        """
        _name = self.path.split('/')[-1]  # Extract file name
        _loc = []

        with open(self.path, mode='r', encoding='utf-8-sig', errors='replace') as file:
            csv_file = csv.DictReader(file)  # Use DictReader to read CSV
            for line in csv_file:
                _loc.append(line)

        # Return dictionary with file name and data
        return {'name': _name, 'locations': _loc}

    def _read_kml(self) -> Dict[str, Any]:
        """
        Read a KML file and return its contents as a dictionary. (Not available for this version)

        :return: A dictionary containing the name of the file and its data.
        """
        pass

    def _read_geojson(self) -> Dict[str, Any]:
        """
        Read a GeoJSON file and return its contents as a dictionary. (Not available for this version)

        :return: A dictionary containing the name of the file and its data.
        """
        pass

    def _read_shapefile(self) -> Dict[str, Any]:
        """
        Read a Shapefile and return its contents as a dictionary. (Not available for this version)

        :return: A dictionary containing the name of the file and its data.
        """
        pass
