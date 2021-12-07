import gevent
from urllib.request import urlopen

URLS = ['http://127.0.0.1:8000/product/1/', 'http://127.0.0.1:8000/product/2/']


def get_data(URL):
    data = urlopen(URL).read()
    file = open("otus.txt", "w")
    file.write(f'{data}')
    file.close()
    print(f'resp:{len(data)}')


prod = [gevent.spawn(get_data, u) for u in URLS]
gevent.wait(prod)
