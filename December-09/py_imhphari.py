from urllib.parse import urlparse

def is_url(url):
    return bool(urlparse(url).netloc)
