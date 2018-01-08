import requests

urls = ('http://codingpy.com/page/{}'.format(i) for i in range(1, 100))
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}


def crawl_article():
    for url in urls:
        requests.get(url)
        print(url)

# crawl_article()

response = requests.get(urls.__next__(), headers=headers)
with open('page1.html', 'w') as f:
    f.write(response.text)