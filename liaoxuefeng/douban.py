import requests
from bs4 import BeautifulSoup
import urllib3
import arrow
import gevent
from gevent import monkey
from pymongo import MongoClient
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://movie.douban.com/top250'

top250 = None
result = []

MONGO_URL = 'mongodb://shau-lok:123456@localhost:27017/test?authMechanism=SCRAM-SHA-1'


def fetch_page(url):
    response = requests.get(url, verify=False)
    return response.text


def parse_page(soup):
    items = soup.find(class_='grid_view').find_all('li')
    movies = []
    for item in items:
        image_url = item.img.get('src')
        _pic = item.find(class_='pic')
        movie_url = _pic.a.get('href')
        rank = _pic.em.text
        _info = item.find(class_='info')
        movie_titles = _info.find_all(class_='title')
        movie_tile = ''
        for title in movie_titles:
            movie_tile += title.text.strip()

        rating_num = _info.find(class_='rating_num').text

        movies.append({
            'rank': rank,
            'image_url': image_url,
            'movie_url': movie_url,
            'movie_title': movie_tile,
            'rating_num': rating_num
        })

    top250.insert_many(movies)
    return movies


def coroutine(url):
    page = fetch_page(url)
    soup = BeautifulSoup(page, 'lxml')
    return parse_page(soup)


def parse(url):

    page = fetch_page(url)
    soup = BeautifulSoup(page, 'lxml')
    result.extend(parse_page(soup))

    next_page = soup.find(attrs={'rel': 'next'})

    # while next_page:
    #     href = next_page.get('href').strip()
    #     page = fetch_page(f'{url}{href}')
    #     soup = BeautifulSoup(page, 'lxml')
    #     result.extend(parse_page(soup))
    #     next_page = soup.find(attrs={'rel': 'next'})

    page_indicator = soup.find(class_='paginator')
    page_indicator.find(class_='next').extract()
    fetch_urls = page_indicator.find_all('a')
    fetch_urls = [f'{url}{query.get("href")}' for query in fetch_urls]

    jobs = [gevent.spawn(coroutine, fetch_url) for fetch_url in fetch_urls]
    gevent.joinall(jobs)
    for movie in [job.value for job in jobs]:
        result.extend(movie)

    # for fetch_url in fetch_urls:
    #     result.extend(coroutine(fetch_url))


if __name__ == '__main__':

    client = MongoClient(MONGO_URL)
    db = client.test
    top250 = db.douban_top250

    start = arrow.now()

    parse(url)
    end = arrow.now()
    print(f'Cost Times {(end-start).seconds}s')

    # with open('../data/douban.txt', 'w') as f:
    #     for movie in result:
    #         f.writelines(str(movie) + '\n')
