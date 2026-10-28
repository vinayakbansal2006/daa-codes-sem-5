url = input("Enter url: ")

protocol = domain = port = path = ""

if("://" in url):
    protocol, url = url.split("://", 1)
if("/" in url):
    url, path = url.split("/", 1)
if(":" in url):
    domain, port = url.split(":", 1)
else:
    domain = url
print("Protocol: ", protocol)
print("Domain: ", domain)
print("Port: ", port)
print("Path: ", path)