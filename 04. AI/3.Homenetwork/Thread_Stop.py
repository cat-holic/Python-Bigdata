import threading

import time
import ctypes


def terminate_thread(thread: threading.Thread):
    """ Terminates a python thread from another thread.

    : param thread : a threading.Thread instance
    """

    if not thread.isAlive():
        return

    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        """if it returns a number greater than one, you're in trouble,
        and you should call it again with exc=Null to revert the effect"""
        ctypes.pythonapi.PythreadState_SetAsyncExc(thread.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def print_hello():
    debug_index = 0
    while True:
        print("Thread 동작중 %d" % debug_index)
        time.sleep(1)
        debug_index += 1


t = threading.Thread(target=print_hello)
t.daemon = True
t.start()


def my_thread_terminate():
    while t.is_alive():
        try:
            terminate_thread(t)
        except:
            pass

while True:
    a=input()
    my_thread_terminate()
    if not t.is_alive():
        print("Thread가 종료되었습니다.")
        print("a = ", a)
        input("main 프로그램을 종료하시겠습니까? 아무값 입력")
        break
