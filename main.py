from Server import CustomHTTPServer, CustomHTTPRequestHandler
from Location import Location
from User import User
from Reader import Reader
import os
import time
import platform


# Main Part (Example)
def main():
    """
    Author: Elmira Pour
    Timestamp: 1717701765.2003505
    version: 0.2
    """

    # write Basic locations on js file
    write_locations('./pages/locations.js')

    # starting server
    run_server()


def leaflet_locations(path):
    _n = path.split('/')[-1].split('.')[0]
    _loc = Reader(path)
    # print(_loc.read()['locations'][0])
    _locs = [Location(*i.values()) for i in _loc.read()['locations']]
    _leaf = [_.to_leaflet() for _ in _locs]
    return _n, _leaf


def write_locations(path):
    # add leaflet in scripts
    _locs = [
        leaflet_locations("./csv/Schulen.csv"),
        leaflet_locations("./csv/Schulsozialarbeit.csv"),
        leaflet_locations("./csv/Jugendberufshilfen.csv"),
        leaflet_locations("./csv/Kindertageseinrichtungen.csv"),

    ]
    with open(file=path, mode='w', encoding='utf-8', errors='replace') as file:
        for loc in _locs:
            file.write(f"const {loc[0]} = {loc[1]};\n")


def run_server():
    echo('Preparing Server...', delay=0.1, end='\n')

    # Define the IP address, port, and root directory
    ip = "127.0.0.1"  # All networks | (Default: 127.0.0.1)
    port = 1000

    # Setup root location
    current_location = os.getcwd().split('\\') if platform.system() == 'Windows' else os.getcwd().split('/')
    root_dir = f"{'/'.join(current_location)}/pages"

    # Custom error handler
    handler = CustomHTTPRequestHandler

    # Create an instance of CustomHTTPServer
    server = CustomHTTPServer(ip, port, root_dir, handler)

    # Start the server
    server.start_server()


def echo(msg: str, **kwargs):
    """
    Echoes each character of the input message with a delay of 0.5 seconds between characters.

    :param msg: The input message to echo.
    """
    # Setup delay time
    if 'delay' in kwargs:
        delay = kwargs['delay']
    else:
        delay = 0.5

    # Setup end for print()
    if 'end' in kwargs:
        end = kwargs['end']
    else:
        end = '\n'

    # Message storage
    m = str()

    # Iterate over each character in the input message
    for _ in msg:
        m += _
        print(f"\r{m}", end='')  # Print the echoed message, replacing the previous one
        time.sleep(delay)
    print(end=end)  # Move to the next line after echoing all characters


if __name__ == '__main__':
    main()
