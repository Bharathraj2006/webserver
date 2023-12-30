from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>My webserver</title>
</head>
<body>
<h1><u>Top five Revenue generating Software Companies</u><h1>
<ul>
<li>Microsoft Corp</li>
<p>Microsoft provides the Windows computer operating systems software, Office applications suite, and the Azure cloud computing service.</p>
<li>Oracle Corp</li>
<p>Oracle supplies cloud infrastructure and enterprise software applications, including the database software that drove its success.</p>
<li>SAP SE</li>
<p>SAP is a Germany-based multinational software company specializing in enterprise applications.</p>
<li>Salesforce</li>
<p>Salesforce is a leading provider of customer relationship management software and services for business clients.</p>
<li>Adobe Inc</li>
<p>Adobe sells the popular Illustrator graphic design software, Acrobat document reader and editor, and Photoshop photo editing tools.</p>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()