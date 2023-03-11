import http.server
import socketserver
import time

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

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
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

# Start the web server
PORT = 8000
handler = MyHttpRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
