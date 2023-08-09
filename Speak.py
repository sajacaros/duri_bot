import contextlib
import pyttsx3


@contextlib.contextmanager
def tts_engine():
    engine = pyttsx3.init()
    engine.setProperty('rate', 240)
    yield engine  # __enter__
    engine.stop()  # __exit__


def print_and_tts(msg):
    print(msg)
    tts_say(msg)


def tts_say(msg):
    with tts_engine() as engine:
        engine.say(msg)
        engine.runAndWait()


def say_ret(func):
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        if ret is not None:
            tts_say(ret)
        return ret

    return wrapper
