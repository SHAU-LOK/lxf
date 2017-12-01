import requests
from pymongo import MongoClient
import gevent
import urllib3
from gevent import monkey
import random
# 豆瓣hot电影
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# monkey.patch_all()
MONGO_URL = 'mongodb://shau-lok:123456@localhost:27017/test?authMechanism=SCRAM-SHA-1'
douban_movie = None
from time import sleep

tags = ['热门',
        '最新',
        '经典',
        '可播放',
        '豆瓣高分',
        '冷门佳片',
        '华语',
        '欧美',
        '韩国',
        '日本',
        '动作',
        '喜剧',
        '爱情',
        '科幻',
        '悬疑',
        '恐怖',
        '成长']

headers = {
    'Host': 'movie.douban.com',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/62.0.3202.94 Safari/537.36'),
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6'
}

# proxies = {
#     'all': 'http://:@127.0.0.1:8888'
# }

proxies = None


def search_subject(tag, page_start=0):

    url = 'https://movie.douban.com/j/search_subjects'

    params = {
        'type': 'movie',
        'tag': tag,
        'sort': 'recommend',
        'page_limit': '60',
        'page_start': page_start
    }

    response = requests.get(url, headers=headers,
                            params=params, verify=False, proxies=proxies).json()

    return response


def parse_search_subject(response):

    subjects = []

    for subject in response.get('subjects'):

        rate = subject.get('rate')
        title = subject.get('title')
        url = subject.get('url')
        playable = subject.get('playable')
        cover = subject.get('cover')
        movie_id = subject.get('id')
        is_new = subject.get('is_new')

        _abstract = abstract_subject(movie_id).get('subject')
        full_title = _abstract.get('title')
        sub_type = _abstract.get('subtype')
        directors = _abstract.get('directors')
        actors = _abstract.get('actors')
        duration = _abstract.get('duration')
        region = _abstract.get('region')
        release_year = _abstract.get('release_year')
        types = _abstract.get('types')

        subjects.append({
            'rate': rate,
            'title': title,
            'url': url,
            'playable': playable,
            'cover': cover,
            'movie_id': int(movie_id),
            'is_new': is_new,
            'full_title': full_title,
            'sub_type': sub_type,
            'directors': directors,
            'actors': actors,
            'duration': duration,
            'region': region,
            'release_year': release_year,
            'types': types
        })
    if subjects:
        try:
            douban_movie.insert_many(subjects)
        except Exception as e:
            pass

    return subjects


def abstract_subject(subject_id):

    url = 'https://movie.douban.com/j/subject_abstract'

    params = {
        'subject_id': subject_id
    }

    response = requests.get(url, headers=headers,
                            params=params, verify=False, proxies=proxies).json()
    return response


def coroutine_grap(tag):

    index = 0
    while True:

        try:
            movies = search_subject(tag, index)
            print(f'[{tag}]解析到第{index}页')
            # sleep(5)
            movies = parse_search_subject(movies)
            if not movies:
                return
            index += 60
        except Exception:
            print(f'[{tag}]第{index}页码解析失败，请重试')


if __name__ == '__main__':

    client = MongoClient(MONGO_URL)
    db = client.test
    douban_movie = db.douban_movie

    jobs = [gevent.spawn(coroutine_grap, tag) for tag in tags]
    gevent.joinall(jobs)
    # gevent.wait(jobs)

    # coroutine_grap(tags[0])
