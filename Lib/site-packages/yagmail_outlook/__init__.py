__project__ = 'yagmail_outlook'
__version__ = "0.9.177"

from yagmail_outlook.error import YagConnectionClosed
from yagmail_outlook.error import YagAddressError
from yagmail_outlook.__main__ import register
from yagmail_outlook.sender import SMTP
from yagmail_outlook.sender import logging
from yagmail_outlook.sender import raw
from yagmail_outlook.sender import inline
from yagmail_outlook.sender import html
