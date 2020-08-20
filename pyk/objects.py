from .keywords import PYK_KEYWORDS

PYK_NONE = None

class PYKObject:
    __static = False
    def __init__(self, *args, **kwargs):
        self.init(*args, **kwargs)
    
    def init(self, *args, **kwargs):
        pass


class _PYK_NULL(PYKObject):
    __slots__ = tuple()
    def __new__(cls):
        global PYK_NONE
        if PYK_NONE is not None:
            return PYK_NONE
        
        PYK_NONE = object.__new__(cls)
        return PYK_NONE
    
    def __str__(self):
        return "null"
    
    __repr__ = __str__

_PYK_NULL()


class PYK_Error(Exception):
    def __init__(self, *args, **kwargs):
        self.init(*args, **kwargs)
        super().__init__(*args)

    def init(self, msg=None):
        self.file = None
        self.line = None
        self.msg = msg
        self.stack = []
        self.message = msg if isinstance(msg, str) else repr(msg)

    def __str__(self):
        return self.format_stack()

    def format_stack(self):
        resp = ""
        for frame in reversed(self.stack):
            resp += f"\nFile {frame[2]}, {'in function '+frame[0].name if frame[0] else 'top-level'}:\n    {frame[1].strip()}"

        resp += "\n\n"

        resp += self.message

        return resp.strip()


class PYK_LIST(PYKObject):
    pass

class PyPYK_Model:
    def __dir__(self):
        dirs = super(PyPYK_Model, self).__dir__()
        dirs = [d for d in dirs if not d.startswith("_")]
        return dirs