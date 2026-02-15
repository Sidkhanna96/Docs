"""
Given a URL, crawl that webpage for URLs, and then continue crawling until you've visited all URLs
Assume you have an API with two methods:
get_html_content(url) -> returns html of the webpage of url
get_links_on_page(html) -> returns array of the urls in the html
"""

from collections import deque


class Web_Crawler:
    def __init__(self):
        pass

    def get_html_content(self, url):
        NotImplemented

    def get_links_on_page(self, html):
        NotImplemented

    def crawl(self, url):
        queue = deque(url)

        while queue:
            node = queue.popleft()

            urls = self.get_links_on_page(self.get_html_content(node))


### AYNCIO VERSION

import asyncio
import httpx  # Standard async HTTP client in 2026
from bs4 import BeautifulSoup


class AsyncWebCrawler:
    def __init__(self, start_url, max_concurrency=50):
        self.start_url = start_url
        self.visited_urls = set()
        self.url_queue = asyncio.Queue()
        self.semaphore = asyncio.Semaphore(
            max_concurrency
        )  # Limits concurrent requests

    async def get_links_on_page(self, html):
        # Parsing is usually fast, but can be moved to a thread if CPU-heavy
        soup = BeautifulSoup(html, "html.parser")
        return [a["href"] for a in soup.find_all("a", href=True)]

    async def process_url(self, client, url):
        """Fetches a single URL and adds new links to the queue."""
        if url in self.visited_urls:
            return

        async with self.semaphore:  # Ensures we don't overwhelm the server
            try:
                self.visited_urls.add(url)
                response = await client.get(url, timeout=10.0)
                response.raise_for_status()

                links = await self.get_links_on_page(response.text)
                for link in links:
                    if link not in self.visited_urls:
                        await self.url_queue.put(link)
            except Exception as e:
                print(f"Failed to crawl {url}: {e}")

    async def worker(self, client):
        """Worker loop that processes URLs from the queue."""
        while True:
            current_url = await self.url_queue.get()
            try:
                await self.process_url(client, current_url)
            finally:
                self.url_queue.task_done()

    async def run(self):
        # Initialize queue with starting URL
        await self.url_queue.put(self.start_url)

        async with httpx.AsyncClient() as client:
            # Create a pool of worker tasks
            workers = [asyncio.create_task(self.worker(client)) for _ in range(10)]

            # Wait until the queue is fully processed
            await self.url_queue.join()

            # Cancel workers once the queue is empty
            for w in workers:
                w.cancel()

        return list(self.visited_urls)


# To run the crawler
# asyncio.run(AsyncWebCrawler("https://example.com").run())
