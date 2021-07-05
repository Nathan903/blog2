import http.server
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        if self.path == '/en/':
            self.path = 'en/index.html'
        elif (not '.' in self.path):
            if self.path[-1] =="/":
                self.path = self.path[0:-1]+'.html'
            else:
                self.path+='.html'
        print(self.path)
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 31
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
import webbrowser
webbrowser.open("http://localhost:"+str(PORT))
my_server.serve_forever()
