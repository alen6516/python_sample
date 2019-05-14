class Singleton(object):
    
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def foo(self):
        print("foo")

singleton1 = Singleton()
singleton2 = Singleton()

print("id of singleton1 is %s" % id(singleton1))
print("id of singleton2 is %s" % id(singleton2))
