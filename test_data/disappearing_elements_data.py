# Disappearing Elements Test Data

# The page has 5 links, but one disappears on each page load
EXPECTED_LINKS = [
    'Home',
    'About',
    'Contact Us',
    'Portfolio',
    'Gallery',  # This one disappears randomly
]

# Total number of links that should always be present
MIN_EXPECTED_LINKS = 4

# Maximum number of links
MAX_EXPECTED_LINKS = 5

# Timeout for waiting for elements (in milliseconds)
ELEMENT_TIMEOUT = 5000

