"""Get media assets from the offical Formula 1 site (formula1.com)"""

import re
import unicodedata

import requests

# driver photo      -- drivers/daniel-ricciardo/_jcr_content/image.img.jpg
# driver helmet     -- drivers/marcus-ericsson/_jcr_content/helmet.img.png/1490887879419.png
# team car diagram  -- teams/Ferrari/_jcr_content/teamCar.img.jpg
# team car photo    -- teams/Mercedes/_jcr_content/image16x9.img.1920.medium.jpg/1490512766389.jpg
# team country flag -- teams/Mercedes/_jcr_content/countryFlag.img.png/1421365183951.png
# team logo         -- teams/Mercedes/_jcr_content/logo.img.jpg/1486740329957.jpg

base_url = 'https://www.formula1.com/content/fom-website/en/championship'

def sanitize(text):
    """Remove accented or otherwise special characters from a string

    Example: Räikkönen -> Raikkonen"""
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode('utf-8')
    text = re.sub(r'\W+', '-', text)
    text = text.lower()
    return text

def driver_profile_image(name):
    return '{}/drivers/{}/_jcr_content/image.img.1024.medium.jpg'.format(base_url, sanitize(name))

def driver_flag_image(name):
    return '{}/drivers/{}/_jcr_content/countryFlag.img.png'.format(base_url, sanitize(name))
