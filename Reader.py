import csv


def read_csv(path: str) -> dict:
    """
    Read a CSV file and return its contents as a dictionary.

    # 'utf-8'       encode without BOM
    # 'utf-8-sig'   encode with BOM

    :param path: The path to the CSV file to be read.
    :return: A dictionary containing the name of the file and its data.
    """

    # Extracting the file name from the path
    _name = path.split('/')[-1]  # name.csv

    # List to store the contents of the CSV file
    _loc = []

    # Opening the CSV file for reading
    with open(path, mode='r', encoding='utf-8-sig', errors='replace') as file:
        # Creating a CSV reader object
        csv_file = csv.DictReader(file)

        # Iterating over each line in the CSV file
        for line in csv_file:
            # Appending each line as a dictionary to the list
            _loc.append(line)

    # Returning a dictionary containing the file name and its data
    return {'name': _name, 'location': _loc}
