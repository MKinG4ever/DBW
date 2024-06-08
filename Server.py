import http.server  # Import the HTTP server module
import socketserver  # Import the socket server module
import os  # Import the os module for interacting with the operating system
from urllib.parse import parse_qs  # Import to parse POST data


class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """
    Custom HTTP request handler to serve custom error pages and handle form submissions.

    Author: Elmira Pour
    Timestamp: 1717701765.2003505
    """

    @property
    def version(self):
        """
        Get the version of the CustomHTTPRequestHandler class.

        :return: A string representing the version.
        """
        return f"v1.2"  # The current version of the CustomHTTPRequestHandler class

    def send_error(self, code, message=None, **kwargs):
        """
        Override the send_error method to serve custom error pages.

        :param code: HTTP status code
        :param message: Optional error message
        """

        # Paths to custom error pages
        error_pages = {
            404: "404.html",  # Replace with the path to your 404 error page
            403: "403.html",  # Replace with the path to your 403 error page
            302: "302.html",  # Replace with the path to your 302 error page
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
            # Handle exceptions by sending a 302 error page and printing the error
            self.send_response(302)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            print(e)  # print error in console
            # Show The 302 Error page
            with open(error_pages[302], 'rb') as file:
                self.wfile.write(file.read())

    def check_pass(self):
        """
        Handle a POST request to check the login credentials.

        :param self: Instance of the class containing request data and methods to respond.
        """
        content_length = int(self.headers['Content-Length'])  # Get the length of the POST data
        post_data = self.rfile.read(content_length).decode('utf-8')  # Read and decode the POST data
        post_params = parse_qs(post_data)  # Parse the POST data

        # Extract username and password from the parsed data
        username = post_params.get('username', [''])[0]
        password = post_params.get('password', [''])[0]

        # Process the login (placeholder logic)
        if username == 'root' and password == 'root':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open('./Home.html', 'rb') as file:
                self.wfile.write(file.read())
        # Send custom error
        else:
            self.send_error(500)

    def do_POST(self):
        """
        Handle POST requests to process form submissions.
        """
        # Check Username and Password
        self.check_pass()


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

    @property
    def version(self):
        """
        Get the version of the CustomHTTPServer class.

        :return: A string representing the version.
        """
        return f"v1.2"  # The current version of the CustomHTTPServer class

    def start_server(self):
        """
        Start the HTTP server.
        """
        os.chdir(self.root_dir)  # Change the current working directory (maybe causing error)
        with socketserver.TCPServer((self.ip, self.port), self.handler_class) as httpd:
            print(f"[Server] http://{self.ip}:{self.port} |  {self.root_dir} ")
            # Serve the content until interrupted
            httpd.serve_forever()
