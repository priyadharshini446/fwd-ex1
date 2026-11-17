from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Protocols</title>
</head>
<body>

    <h1>TCP/IP PROTOCOLS</h1>

    <p>
        TCP/IP stands for Transmission Control Protocol
        and Internet Protocol. It is a set of rules used
        for communication between computers over a network.
    </p>

    <h2>Layers of TCP/IP Model</h2>

    <h3>1. Application Layer</h3>
    <p>
        This layer provides services to users and applications.
        It is used to access websites, send emails and transfer files.
    </p>
    <p>Protocols: HTTP, HTTPS, FTP, SMTP, DNS</p>

    <h3>2. Transport Layer</h3>
    <p>
        This layer provides communication between devices.
        It ensures proper data transmission.
    </p>
    <p>Protocols: TCP, UDP</p>

    <h3>3. Internet Layer</h3>
    <p>
        This layer is responsible for sending data packets
        from one network to another using IP addresses.
    </p>
    <p>Protocols: IP, ICMP, IGMP</p>

    <h3>4. Network Access Layer</h3>
    <p>
        This layer is responsible for transferring data
        through physical network connections.
    </p>
    <p>Protocols: Ethernet, Wi-Fi</p>

    <h2>Advantages of TCP/IP</h2>
    <ul>
        <li>Provides communication between computers.</li>
        <li>Supports internet connectivity.</li>
        <li>Allows data sharing between networks.</li>
        <li>Provides reliable data transmission using TCP.</li>
    </ul>

    <h2>Conclusion</h2>
    <p>
        TCP/IP is an important networking model that helps
        computers communicate and share information
        through the Internet.
    </p>

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
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
