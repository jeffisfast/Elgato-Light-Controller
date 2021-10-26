"""A Python module designed to control the Elgato brand Lights."""

import logging

from .leglight import LegLight
from .discovery import discover

from .__version__ import __title__, __description__, __url__, __version__
from .__version__ import __author__, __author_email__, __license__

# You shouldn't import all, but you can...
__all__ = [
    'discover',
    'LegLight',
]

logging.getLogger(__name__).addHandler(logging.NullHandler())