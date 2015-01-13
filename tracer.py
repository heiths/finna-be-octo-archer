import functools

class Trace(object):
    def __init__(self):
        self.enabled = True

    def __call__(self, f):

        @functools.wraps(f)
        def wrap(*args, **kwargs):
            if self.enabled:
                print("calling {}".format(f))
            return f(*args, **kwargs)
        return wrap