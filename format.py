import requests
from settings import *
from urllib.parse import urlparse, urlunparse
import json

def format_url(new_path, url, verbose = True):
    new_path = new_path.strip('/')
    url_parsed = urlparse(url)
    url_components = list(url_parsed)
    url_components[2] = new_path
    url_updated = urlunparse(tuple(url_components))
    if verbose:
        print('Original url: %s'%url)
        print('Original path: %s'%url_parsed.path)
        print('Updated path: %s'%new_path)
        print(url_updated)
    return url_updated

def get_labels(url):
    labels = requests.get(url)
    return labels.json()

def create_label(url, label):
    r = requests.post(url, json = label)
    print('Status Code: %i'%r.status_code)


if __name__ == '__main__':
    verbose = True
    labels_path = '/'.join(['repos', OWNER, REPO, 'labels'])
    url_labels = format_url(labels_path, URL)

    label = {"name": "foo", "color": "f29513"}
    create_label(url_labels, label)

    labels = get_labels(url_labels)
    if verbose:
        print(json.dumps(labels, indent = 2))



