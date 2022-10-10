import urllib.request
fp = urllib.request.urlopen('http://127.0.0.1:5000/todo/weather/now')
encodedContent = fp.read()
decodedContent = encodedContent.decode("utf8")


print(fp)
