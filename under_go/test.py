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


        


class Worker(object):
