from django.db import models

# Create your models here.

class BitcoinData(object):
    """docstring for BitcoinData."""
    id = str
    name = str
    high_24 = float
    low_23 = float
    market_cap = float
