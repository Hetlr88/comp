import logging
import os
import time
from io import BytesIO, StringIO
from logging.handlers import RotatingFileHandler

from dotenv import load_dotenv
from pyrogram import Client

botStartTime = time.time()

if os.path.exists('BindhuEncoder/config.env'):
    load_dotenv('BindhuEncoder/config.env')

# Variables

