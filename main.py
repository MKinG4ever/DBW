from Server import CustomHTTPServer, CustomHTTPRequestHandler
from Database import DBManager
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
    version: 0.71
    """

    # write Basic locations on js file
    write_locations('./pages/locations.js')

    # set DataBase and create USER table | Before changing root_dir
    set_database()

    # starting server | Changing root_dir
    run_server(ip="127.0.0.1", port=1000)


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


def set_database():
    dbname = 'database.db'
    password = None  # Optional, set to None if no password

    # Connect & Disconnect
    with DBManager(dbname) as db:
        # favorite
        db.create_favorite_table()
        db.db_save_favorite_location('root', 'home', 50.826, 12.950)
        db.db_save_favorite_location('root', 'Park', 50.832, 12.960)
        db.db_save_favorite_location('root', 'Workplace', 50.825, 12.945)
        db.db_save_favorite_location('root', 'new1', 50.835, 12.955)
        db.db_save_favorite_location('root', 'new2', 50.839, 12.969)
        db.db_save_favorite_location('root', 'new3', 50.820, 12.940)
        # users
        db.create_user_table()  # create USER table
        db.db_save_user('root', 'root', None, None, None, None)  # save 'root'
        ul = db.get_user_locations('root')
        print(ul)
        db.write_user_locations('root','./pages/fav.js')


def run_server(ip="127.0.0.1", port=1000):
    echo('Preparing Server...', delay=0.1, end='\n')

    # Setup root location
    current_location = os.getcwd().split('\\') if platform.system() == 'Windows' else os.getcwd().split('/')
    root_dir = f"{'/'.join(current_location)}/pages"

    # Custom error handler
    handler = lambda *args, **kwargs: CustomHTTPRequestHandler(*args, **kwargs, server_instance=server)

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
