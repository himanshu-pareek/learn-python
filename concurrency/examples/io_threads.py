import threading
import time
from concurrent.futures import ThreadPoolExecutor

import requests

thread_local = threading.local()

def main():
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.perf_counter()
    download_all_sites(sites)
    duration = time.perf_counter() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")

def download_all_sites(sites):
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} bytes from {url}")

if __name__ == "__main__":
    main()
