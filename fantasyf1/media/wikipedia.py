"""Get media assets from Wikipedia"""

import requests
from bs4 import BeautifulSoup

def infobox_image(url):
    """Get URL of an image from a Wikipedia page's infobox

    The infobox is the grey rectangle at the top-right of many Wikipedia pages.
    This function will parse the infobox HTML and return the src of its primary
    image (currently defined as the tallest image)."""
    r = requests.get(url)
    r.raise_for_status()
    bs = BeautifulSoup(r.content, 'html.parser')
    infobox_imgs = bs.select('#bodyContent .infobox img')
    if infobox_imgs:
        # If there are multiple images we return the tallest one.
        img = max(infobox_imgs, key=lambda img: int(img['height']))
        return img['src']
    return None
