import time
import threading

class Context:
    def __init__(self, text, finish_text):
        self._flag = True
        self._text = text
        self._finish_text = finish_text
        self._spinner = ['-', '/', '|', '\\']

    def __enter__(self):
        t1 = threading.Thread(target=self._start)
        t1.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._stop()

    def _start(self):
        count = 0
        while self._flag:
            count = count % len(self._spinner)
            time.sleep(0.25)
            print("\r"+self._text+self._spinner[count], end=" ")
            count += 1
        print("\r"+self._finish_text)

    def _stop(self):
        self._flag = False

