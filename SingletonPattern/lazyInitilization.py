class MySingleton:
    _instance = None

    def __init__(self):
        if MySingleton._instance is not None:
            raise Exception("This is a singleton! Use get_instance().")
        print("Constructor called...")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            print('here-------')
            cls._instance = MySingleton()
        return cls._instance


# # 

obj1 = MySingleton.get_instance()
obj2 = MySingleton.get_instance()

#Disadvantages using this lazyinitialization is when multiple threads comes then it will be a lock situation