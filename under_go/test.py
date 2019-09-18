# only 2 kinds of class: object and worker
# can dump to json

class Tag(object):
    _LIST = []

    @classmethod
    def get_list(cls):
        return _LIST

    def __init__(self, name):
        self.name = name
        self._LIST.append(name)
    


class Comic(object):
    _LIST = []
    _TAGS = []
   

    @classmethod
    def get_list(cls):
        return cls._LIST
    
    @classmethod
    def get_tags(cls):
        return cls._TAGS


    def __init__(self, name, score, tags, note):
        self.name = name
        self.score = score
        self.tags = [tags] if type(tags) != type([]) else tags
        self.note = note

        self._LIST.append(self)

        for tag in self.tags:
            if tag not in self.get_tags():
                self._TAGS.append(tag)
        


class Worker(object):
    
    _INST = None

    @classmethod
    def get_inst(cls):
        return cls._INST

    def __init__(self):
        assert self._INST, "%s can only have 1 instance" % self.__class__.__name__
        _INST = self


