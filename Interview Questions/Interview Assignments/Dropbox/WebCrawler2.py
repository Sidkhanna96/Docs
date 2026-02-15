"""
Given a URL, crawl that webpage for URLs, and then continue crawling until you've visited all URLs
Assume you have an API with two methods:
get_html_content(url) -> returns html of the webpage of url
get_links_on_page(html) -> returns array of the urls in the html

"""

from collections import deque
import threading
from concurrent.futures import ThreadPoolExecutor, FIRST_COMPLETED


class WebCrawler:
    def __init__(self, root):
        self.queue = deque([root])
        self.visited = set()
        self.lock = threading.Lock()

    def get_html_content(self, url):
        NotImplemented

    def get_links_on_page(self, html):
        NotImplemented

    def process_url(self, url):
        html = None

        try:
            html = self.get_html_content(
                url
            )  # This would be a time sync and slow process down while waiting for external api call to get back
        except Exception as e:
            print(f"Error as {e}")
            raise

        urls = self.get_links_on_page(html)

        return urls

    def crawl(self):
        futures = set()
        with ThreadPoolExecutor(max_workers=20) as executor:
            while self.queue:
                while self.queue:
                    with self.lock:
                        url = self.queue.popleft()

                        if url not in self.visited:
                            futures.add(executor.submit(self.process_url, url))
                            self.visited.add(url)

                    if not futures:
                        continue

                    done, not_done = wait(futures, return_when=FIRST_COMPLETED)
                    futures = not_done

                    for d in done:
                        urls = d.result()

                        with self.lock:
                            self.queue.extend(urls)

        return self.visited


"""
--------------------------------------------------------------------------------------------------------------------------------
"""
from collections import deque
import threading


class WebCrawler:
    def __init__(self, root):
        self.queue = deque(root)
        self.visited = set()
        self.lock = threading.Lock()

    def get_html_content(self, url):
        NotImplemented

    def get_links_on_page(self):
        NotImplemented

    def process_url(self, url):
        html = None
        try:
            html = self.get_html_content(url)
        except Exception as e:
            raise (f"Exception as {e}")

        return self.get_links_on_page(html)

    def crawl(self):
        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = set()
            while self.queue:
                with self.lock:  # Main thread lock and child thread
                    while self.queue:
                        url = self.queue.popleft()

                        if url not in self.visited:
                            self.visited.add(url)
                            futures.add(executor.submit(self.process_url, url))

                done, future = wait(futures, return_when=FIRST_COMPLETED)

                for f in done:
                    urls = f.result

                    with self.lock:
                        self.queue.extend(urls)


"""
------------------------------------------------------------------------------------------------------------------------------
"""

from collections import deque

from collections import deque
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
import threading


class WebCrawler:
    def __init__(self, origin_url):
        self.origin_url = origin_url
        self.queue = deque([origin_url])
        self.visited_urls = set()
        self.active_futures = []
        self.lock = threading.Lock()
        self.max_active_jobs = 50

    def get_html_content(url):
        NotImplemented

    def get_links_on_page(html):
        NotImplemented

    def process_url(self, url):
        html_content = None
        try:
            # This is the bottleneck since - we would need to wait for a response from the API to respond back to us that time the GIL is Idle
            html_content = self.get_html_content(url)
        except Exception as e:
            return ""  # Retry logic here

        urls = self.get_links_on_page(html_content)

        return urls

    def run_crawl_process_thread(self):
        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = set()

            while self.queue or futures:
                with self.lock:  # Only 1 thread can execute this section
                    while self.queue:
                        url = self.queue.popleft()

                        if url not in self.visited_urls:
                            self.visited_urls.add(url)
                            futures.add(executor.submit(self.process_url, url))

                if not futures:
                    continue

                done, futures = wait(
                    futures, return_when=FIRST_COMPLETED
                )  # Done and Not Done processes

                for future in done:
                    urls = future.result()
                    with self.lock:
                        self.queue.extend(urls)

    def run_crawl_process(self):
        while self.queue:
            node_url = self.queue.popleft()

            if node_url not in self.visited_urls:
                self.visited_urls.add(node_url)
                urls = self.process_html(node_url)
                self.queue.extend(urls)

        return list(self.visited_urls)
