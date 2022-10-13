import urllib.request
import logging
fp = urllib.request.urlopen('http://127.0.0.1:5000/todo/weather/now')
encodedContent = fp.read()
decodedContent = encodedContent.decode("utf8")
print(decodedContent)
def test():
    logging.basicConfig(filename='test.log', level=logging.INFO, format = "%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")
    a = logging.getLogger(__name__)
    logging.info(decodedContent)
test()