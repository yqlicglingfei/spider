import urllib.request
request = urllib.request.Request('http://python.org/')
request.add_header("User-Agent", "My Python Crawler")
opener = urllib.request.build_opener()
response = opener.open(request)
html = response.read()
print(html)
