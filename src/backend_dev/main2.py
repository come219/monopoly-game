import http.server
import socketserver
import time
import json

# Define your grid map here
grid_map = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0]
]

def print_grid_map():
    # Print the grid map
    print(grid_map)

    # Schedule the next print after 1 minute
    time.sleep(60)
    print_grid_map()

# Start printing the grid map every minute
print_grid_map()

class MyHttpRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Return the grid map as a string in HTML format
            response = "<html><body><table>"
            for row in grid_map:
                response += "<tr>"
                for cell in row:
                    if cell == 0:
                        response += "<td> </td>"
                    else:
                        response += "<td>X</td>"
                response += "</tr>"
            response += "</table></body></html>"
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.send_header("Content-length", len(response))
            self.end_headers()
            self.wfile.write(response.encode())
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == '/update':
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = json.loads(body)
            x = data.get('x')
            y = data.get('y')
            value = data.get('value')
            if x is not None and y is not None and value is not None:
                grid_map[y][x] = value
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'OK')
            else:
                self.send_error(400)
        else:
            self.send_error(404)

# Start the web server
PORT = 8000
handler = MyHttpRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
