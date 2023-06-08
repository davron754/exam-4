import threading
import time
import httpx
import redis
from datetime import timedelta


def get_data(url):
    response = httpx.get(url).read()
    response.decode('utf-8')
    con = redis.Redis(host="localhost", port=6379, decode_responses=True)
    con.set(name=url, value=response, ex=timedelta(60))


sites = [
    "https://www.kun.uz",
    "https://www.daryo.uz",
    "https://www.qalampir.uz",
    "https://www.instagram.com",
    "https://www.pdp.uz"
]

threads = []
for wsite in sites:
    start = time.time()
    thread = threading.Thread(target=get_data, args=(wsite,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
