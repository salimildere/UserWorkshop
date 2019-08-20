import logging
import functools
import requests

def client_method (func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs): # args ve kwargs parametrelere gelmesi halinde sorun yaratmamasi icin kullanilmistir.
        request = func(*args,**kwargs)
        if request.status_code == 200:
            logging.info("Status code 200")
            return request.json()
        else:
            logging.basicConfig(level=logging.ERROR)
            logging.error('Status code is different than 200')
    return wrapper

@client_method
def make_requests (base_url):
    logging.info('make_requests is running')
    return requests.get(base_url)
