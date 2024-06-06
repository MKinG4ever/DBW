import http.server  # Import the HTTP server module
import socketserver  # Import the socket server module
import os  # Import the os module for interacting with the operating system


class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """
    Custom HTTP request handler to serve custom error pages.

    Author: Elmira Pour
    Timestamp: 1717701765.2003505
    """

    @property
    def version(self):
        """
        Get the version of the CustomHTTPRequestHandler class.

        :return: A string representing the version.
        """
        return f"v1.1"  # The current version of the CustomHTTPRequestHandler class

    def send_error(self, code, message=None, **kwargs):
        """
        Override the send_error method to serve custom error pages.

        :param code: HTTP status code
        :param message: Optional error message
        """

        # Paths to custom error pages
        error_404_page = "404.html"  # Replace with the path to your 404 error page
        error_403_page = "403.html"  # Replace with the path to your 403 error page
        default_error_page = "500.html"  # Replace with the path to your default error page

        try:
            if code == 404:
                self.send_response(code)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                # Show The 404 Error page
                with open(error_404_page, 'rb') as file:
                    self.wfile.write(file.read())
            elif code == 403:
                self.send_response(code)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                # Show The 403 Error page
                with open(error_403_page, 'rb') as file:
                    self.wfile.write(file.read())
            else:
                self.send_response(code)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                # Show The 500 Error page (as default Error page)
                with open(default_error_page, 'rb') as file:
                    self.wfile.write(file.read())
        except Exception as e:
            self.send_response(500)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            print(e)  # print error in console
            # Show The 500 Error page
            with open(default_error_page, 'rb') as file:
                self.wfile.write(file.read())


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
        return f"v1.1"  # The current version of the CustomHTTPServer class

    def start_server(self):
        """
        Start the HTTP server.
        """
        os.chdir(self.root_dir)  # Change the current working directory
        with socketserver.TCPServer((self.ip, self.port), self.handler_class) as httpd:
            print(f"[Server] http://{self.ip}:{self.port} |  {self.root_dir} ")
            # Serve the content until interrupted
            httpd.serve_forever()
