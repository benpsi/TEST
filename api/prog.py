from http.server import BaseHTTPRequestHandler
from datetime import datetime
class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    self.wfile.write('<img src="data:image/jpeg;base64,https://www.denofgeek.com/wp-content/uploads/2020/09/Sacha-Baron-Cohen-as-Borat.jpg?fit=1200%2C804"/>'.encode())
    return