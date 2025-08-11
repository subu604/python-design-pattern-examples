import threading

class MySingleton:
    _instance = None
    _lock = threading.Lock()  # Lock for synchronizing threads

    def __init__(self):
        if MySingleton._instance is not None:
            raise Exception("This is a singleton! Use get_instance().")
        print("Constructor called...")

    @classmethod
    def get_instance(cls):
        # Synchronize access to instance creation
        with cls._lock:
            if cls._instance is None:
                cls._instance = MySingleton()
        return cls._instance


# Example usage
obj1 = MySingleton.get_instance()
obj2 = MySingleton.get_instance()

print(obj1 is obj2)  # ✅ True


#This resolves the multiple threaded locking behaviour but it is expencsive when execeive threads comes in it will be 
# much into the condition checking