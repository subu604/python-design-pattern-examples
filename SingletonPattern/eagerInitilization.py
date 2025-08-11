class EagerSingleton:
    # Create instance eagerly when class is defined
    _instance = None  

    def __init__(self):
        if EagerSingleton._instance is not None:
            raise Exception("This class is a singleton! Use get_instance() instead.")
        print("Initializing the singleton instance...")

    @classmethod
    def get_instance(cls):
        return cls._instance


# Eagerly create the instance at class load time
EagerSingleton._instance = EagerSingleton()

# Usage
if __name__ == "__main__":
    s1 = EagerSingleton.get_instance()
    s2 = EagerSingleton.get_instance()

    print(s1 is s2)  # True → Same instance

# example -2
# class MySingleton:
#     _instance = None

#     def __init__(self):
#         if MySingleton._instance is not None:
#             raise Exception("This is a singleton! Use get_instance().")
#         print("Constructor called...")

#     @classmethod
#     def get_instance(cls):
#         if cls._instance is None:
#             print('here-------')
#             cls._instance = MySingleton()
#         return cls._instance


# # # 

# obj1 = MySingleton.get_instance()
# obj2 = MySingleton.get_instance()
# obj3 = MySingleton()  # ❌ Raises Exception


# example 3:
# class MySingleton:
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls._instance is not None:
#             raise Exception("Use get_instance(), not constructor!")
#         cls._instance = super().__new__(cls)
#         return cls._instance

#     @classmethod
#     def get_instance(cls):
#         if cls._instance is None:
#             cls()
#         return cls._instance


# # Usage
# obj1 = MySingleton.get_instance()
# obj2 = MySingleton()  # ❌ Raises Exception
