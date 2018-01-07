from urllib.request import urlopen

url = "http://www.skysports.com/premier-league-table"


def get_webpage(url):
    response = urlopen(url)
    data = response.read()
    text = data.decode("utf-8")
    return text

text = get_webpage(url)
with open('html_text.txt', 'w') as f:
    f.write(text)
