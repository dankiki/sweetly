import base64
import math
import redis
import sweetly.settings as settings


def int_to_base64(num):
    """Converts a positive int into a urlsafe base64 representation.

       Keeps it short.
    Args:
        num: a positive int
    Returns:
        A URL safe bas64 representation"""

    bnum = num.to_bytes(math.ceil(num.bit_length()/8), 'big')
    encoded = base64.urlsafe_b64encode(bnum)
    return encoded


def generate_short_url(long_url, base_url):
    """Checks if the link was already shortened, shortens if not.

    Args:
        long_url: The url to be shortened
        base_url: The base part of the short url
    Returns:
        A shortened url
    """

    r = redis.Redis(host=settings.REDIS_HOST)

    # Already shortened?
    already_short = r.get(long_url)

    if already_short:
        return already_short.decode("ascii")

    # Proceed if not.
    new_entry_order = int(r.get('last_entry')) + 1
    short_part = int_to_base64(new_entry_order)
    complete_short_url = base_url + short_part.decode("ascii")
    r.mset({long_url: complete_short_url,
            short_part: long_url,
            'last_entry': new_entry_order})

    return complete_short_url


def long_from_short(short_part):
    """Takes the short part of the shortened url and returns the long url.
    """

    r = redis.Redis(host=settings.REDIS_HOST)
    long_url = r.get(short_part)
    if not long_url:
        return None
    return long_url.decode("ascii")
