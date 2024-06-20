import http.server  # Import the HTTP server module
import socketserver  # Import the socket server module
import os  # Import the os module for interacting with the operating system
from urllib.parse import parse_qs  # Import to parse POST data
from Database import DBManager


class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """
    Custom HTTP request handler to serve custom error pages and handle form submissions.

    1xx: Informational responses indicating that the request was received and understood.
    2xx: Success codes indicating that the request was successfully received, understood, and accepted.
    3xx: Redirection codes indicating further action needs to be taken to complete the request.
    4xx: Client error codes indicating that there was an issue with the request (e.g., 404 for Not Found, 403 for Forbidden).
    5xx: Server error codes indicating that there was a problem with the server processing the request (e.g., 500 for Internal Server Error).

    Author: Elmira Pour
    Timestamp: 1717701765.2003505
    """

    def __init__(self, *args, server_instance=None, **kwargs):
        self.server_instance = server_instance
        super().__init__(*args, **kwargs)

    @property
    def version(self):
        """
        Get the version of the CustomHTTPRequestHandler class.

        :return: A string representing the version.
        """
        return f"v1.61"  # The current version of the CustomHTTPRequestHandler class

    @staticmethod
    def save_user_data(username: str, password: str, name: str, email: str, mobile: str, birthday: str) -> None:
        """
        Save user data to a database.

        :param username: Username provided by the user
        :param password: Password provided by the user
        :param name: Name of the user
        :param email: Email address of the user
        :param mobile: Mobile number of the user
        :param birthday: Birthday of the user
        """

        with DBManager('../database.db') as db:
            # Create if not exist
            db.create_user_table()
            # Save user data
            db.db_save_user(username, password, name, email, mobile, birthday)

    @staticmethod
    def authenticate_user(username: str, password: str) -> bool:
        """
        Authenticate the user by checking credentials against a database file.

        :param username: Username provided by the user
        :param password: Password provided by the user
        :return: True if authentication is successful, False otherwise
        """

        with DBManager('../database.db') as db:
            # Authenticate user
            authenticated = db.db_authenticate_user(username, password)
            print(f"Authentication result: {authenticated}")
            return authenticated

    @staticmethod
    def save_favorite(username, loc_name, lat, lng):
        """
        Save favorite location to a database.
        """
        try:
            # Connect to the database and save the location
            with DBManager('../database.db') as db:
                db.create_favorite_table()
                db.db_save_favorite_location(username, loc_name, lat, lng)
                print('Debuger:save_favorite')
        except Exception as e:
            print(f"Error saving favorite location: {e}")

    def secure(self):
        """
        Handle secure requests.
        """
        content_length = int(self.headers['Content-Length'])  # Get the length of the POST data
        post_data = self.rfile.read(content_length).decode('utf-8')  # Read and decode the POST data
        post_params = parse_qs(post_data)  # Parse the POST data

        # Extract the parsed data
        _u = post_params.get('u', [''])[0]
        _p = post_params.get('p', [''])[0]

        # Handle response
        self.send_response(302)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        # Show the 302 Response Page in Browser
        with open('./302.html', 'rb') as file:
            self.wfile.write(file.read())

        self.server_instance.stop_server()

    def send_error(self, code, message=None, **kwargs):
        """
        Override the send_error method to serve custom error pages.

        :param code: HTTP status code
        :param message: Optional error message
        :param kwargs: Additional keyword arguments
        """

        # Paths to custom error pages
        error_pages = {
            404: "404.html",  # Replace with the path to your 404 error page
            403: "403.html",  # Replace with the path to your 403 error page
            'default': "500.html"  # Replace with the path to your default error page
        }

        try:
            # Determine the error page based on the code
            error_page = error_pages.get(code, error_pages['default'])

            # Send response and headers
            self.send_response(code)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            # Open and send the corresponding error page
            with open(error_page, 'rb') as file:
                self.wfile.write(file.read())

        except Exception as e:
            # Handle exceptions by sending a 500 error page and printing the error
            self.log_error(f"Error handling error page: {e}")
            self.send_response(500)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            print(e)  # print error in console
            # Show The 500 Error page
            with open(error_pages['default'], 'rb') as file:
                self.wfile.write(file.read())

    def handle_login(self):
        """
        Handle a POST request of user Login (./pages/login.html).
        """
        content_length = int(self.headers['Content-Length'])  # Get the length of the POST data
        post_data = self.rfile.read(content_length).decode('utf-8')  # Read and decode the POST data
        post_params = parse_qs(post_data)  # Parse the POST data

        # Extract username and password from the parsed data
        username = post_params.get('username', [''])[0]
        password = post_params.get('password', [''])[0]

        # Sanitize inputs and process the login (placeholder logic)
        if self.authenticate_user(username, password):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            # Inject the username into Home.html
            with open('./Home.html', 'r') as file:
                home_content = file.read()
                home_content = home_content.replace('{{username}}', username)  # Replace placeholder with username
                self.wfile.write(home_content.encode('utf-8'))
        # Send custom error
        else:
            self.send_error(403)  # Unauthorized access error

    def handle_signin(self):
        """
        Handle a POST request of user SignIn (./pages/signin.html).
        """
        content_length = int(self.headers['Content-Length'])  # Get the length of the POST data
        post_data = self.rfile.read(content_length).decode('utf-8')  # Read and decode the POST data
        post_params = parse_qs(post_data)  # Parse the POST data

        # Extract user information from the parsed data
        username = post_params.get('username', [''])[0]
        password = post_params.get('password', [''])[0]
        name = post_params.get('name', [''])[0]
        email = post_params.get('email', [''])[0]
        mobile = post_params.get('mobile', [''])[0]
        birthday = post_params.get('birthday', [''])[0]

        # Sanitize inputs and save user data to a file (replace with database storage or other secure method)
        self.save_user_data(username, password, name, email, mobile, birthday)

        # Redirect or respond with a success message
        self.send_response(200)  # Send OK status
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open('./index.html', 'rb') as file:  # Path to success page after signup
            self.wfile.write(file.read())

    def handle_favorites(self):
        """
        Handle the addition of favorite locations.
        """
        print('Debuger:handle_favorites')

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        post_params = parse_qs(post_data)

        # Extract form data
        loc_name = post_params.get('locName', [''])[0]
        lat = float(post_params.get('lat', [''])[0])
        lng = float(post_params.get('lng', [''])[0])
        username = post_params.get('username', [''])[0]

        # Save to database or perform other actions
        self.save_favorite(username, loc_name, lat, lng)

        # Respond with a success message
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Favorite location added successfully')

    def do_POST(self):
        """
        Handle POST requests to process form submissions.
        """
        if self.path == '/secure':
            self.secure()
        elif self.path == '/SignIn':
            self.handle_signin()
        elif self.path == '/Login':
            self.handle_login()
        elif self.path == '/Home':
            self.handle_favorites()
        else:
            self.send_error(404)  # Page not found error


class CustomHTTPServer:
    """
    Custom HTTP server class to initiate the server.

    Author: Elmira Pour
    Timestamp: 1717701765.2003505
    """

    def __init__(self, ip, port, root_dir, handler_class):
        """
        Initialize the CustomHTTPServer.

        :param ip: IP address to serve content
        :param port: Port number to serve content
        :param root_dir: Root directory to serve files from
        :param handler_class: Custom request handler class
        """
        self.ip = ip
        self.port = port
        self.root_dir = root_dir
        self.handler_class = handler_class
        self.httpd = None  # To hold the TCPServer instance

    @property
    def version(self):
        """
        Get the version of the CustomHTTPServer class.

        :return: A string representing the version.
        """
        return f"v1.41"  # The current version of the CustomHTTPServer class

    def start_server(self):
        """
        Start the HTTP server.

        This method initializes a TCP server using the provided IP address and port number,
        and serves content from the specified root directory using the custom request handler class.
        """
        os.chdir(self.root_dir)  # Go to root
        print(f"[Server] http://{self.ip}:{self.port} |  {self.root_dir} ")  # Present
        self.httpd = socketserver.TCPServer((self.ip, self.port), self.handler_class)  # Set a socketserver
        self.httpd.serve_forever()  # execute the server

    def stop_server(self):
        """
        Stop the HTTP server.
        """
        if hasattr(self, 'httpd') and self.httpd:
            self.httpd.shutdown()
