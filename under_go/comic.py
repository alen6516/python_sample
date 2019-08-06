#!/usr/bin/python
# -*- coding: utf-8 -*-
#####
# File Name: comic.py
# Author: alen6516
# Created Time: 2019-05-11
#####



class Data(object):
    _LIST = []
    _TAGS = []
    _ATTR_LIST = []

    """
    @classmethod
    def search_by_attribute(cls, attr):
        if attr not in cls._ATTR_LIST:
            print("no such attribute")
        
        result = {}
        '''
        {
            "attribute": ATTRIBUTE
            "content": [ obj1.name, obj2.name, ...]
        }
        '''
    """

    @classmethod
    def get_list(cls):
        return cls._LIST

    @classmethod
    def get_tags(cls):
        return cls._TAGS

    @classmethod
    def get_attributes(cls):
        return cls._ATTR_LIST

    '''
    @classmethod
    def dump_to_json(cls):
        pass
    '''

    def __init__(self, name, score, tags, note):

        self.name = name
        self.score = score
        self.tags = [tags] if type(tags) != type([]) else tags
        self.note = note

        # add to class
        for tag in self.tags:
            if tag not in self._TAGS:
                self._TAGS.append(tag)

        self._LIST.append(self)
        self._ATTR_LIST.extend(["name", "score", "tags", "note"])

    def show(self):
        print("name: %s\tscore: %s\ttags: %s" % (self.name, self.score, self.tags))




class Option(object):

    '''
    ops = {
        0: {
            "titile": TITLE,
            "function": FUNCTION
        }
    }
    '''

    @classmethod
    def show(cls, ops):
        result = "op:\n"
        _len = len(ops.items())
        _numbers = ops.keys()
        _titles = [ _["title"] for _ in ops.values() ]

        for i in range(_len):
            result += str(_numbers[i]) + ". " + _titles[i] + "\n"
        
        return result

    @classmethod
    def do(cls, ops, op):

        if op not in ops.keys():
            print("unknown, try again")
        else:
            ops[op]["function"]()




class Worker(object):
    _instance = None
    _data_class = Data


    # internal function

    def _if_no_input(self, _input):
        return ( _input == "" )
        
    def _if_confirm(self):
        _input = raw_input("confirm? [y/N]")
        return ( _input in ('y', 'Y') )

    def _to_continue(self):
        raw_input("press any key to continue...")

    def __new__(self):
        if not self._instance:
            self._instance = super(Backend, self).__new__(self)
        return self._instance


    # APIs
    
    def quit(self):
        print("bye")
        exit(0)

    def add(self):
        def name_exist(_name):
            return ( _name in [obj.name for obj in self._data_class.get_list()] )


        while True:
            name = raw_input("name: ")
            if _if_no_input(name):
                print("nothing to add")
                return

            if name_exist(name):
                print("name duplicate, data with name \"%s\" already exist" % name )
                print("please try again")


        score = raw_input("score: ")
        tag = raw_input("tag: ")
       
        if _if_confirm():
            data = self._data_class(name, score, tag)
            print("==== store data! ====")
            data.show()
            print("=====================")
        

    def show_list(self):
        for data in self._data_class.get_list():
            print("=============")
            data.show()
            print("=============")

    def show_tags(self):
        print(self._data_class.get_tags())

    def search_by_tags(self):
        tags = raw_input("give tags (seprate by ,): ")
        tags.replace(" ", "")
        tags = tags.split(",")
        
        for tag in tags:
            if tag not in self._data_class.get_tags():
                print("no such tag: %s" % tag)
                return
            
        result = []
        for data in self._data_class.get_list():
            flag = 1
            for tag in tags:
                if tag not in data.tags:
                    flag = 0
                    break
            if flag:
                result.append(data)
        
        print([_.name for _ in result])

    def get_by_name(self):
        result = []
        candidate_list = self._data_class.get_list()

        while(len(candidate_list) > 1):
            name = raw_input("give name: ")
        
            if _if_no_input(name):
                print("canceled")
                return

            for obj in candidate_list:
                if name in obj.name:
                    result.append(obj)

            if not result:
                print("no such name \"%s\"" % name)
                return

            elif len(result) == 1:
                print("result: %s" % result[0].name)
                self._get_by_name_next()

            else:
                print("current result: %s" % result)
                self._to_continue()
                candidate_list = result
            
    def _get_by_name_next(self):
        ops = {
            0: {
                "title":
            }
        }


    def main_loop(self):
        ops = {
                0: {
                    "title": "quit",
                    "function": _backend.quit
                },
                1: {
                    "title": "add",
                    "function": _backend.add
                },
                2: {
                    "title": "show list",
                    "function": _backend.show_list
                },
                3: {
                    "title": "show tags",
                    "function": _backend.show_tags
                },
                4: {
                    "title": "search by tags",
                    "function": _backend.search_by_tags
                },
                5: {
                    "title": "get by name",
                    "function": _backend.get_by_name
                }
        }

        while(1):
            op = raw_input(Option.show(ops))
            Option.do(ops, int(op))



Worker().main_loop()
