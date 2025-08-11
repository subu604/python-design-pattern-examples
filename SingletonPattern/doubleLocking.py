import threading

class MySingleton:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        if MySingleton._instance is not None:
            raise Exception("This is a singleton! Use get_instance().")
        print("Constructor called...")

    @classmethod
    def get_instance(cls):
        # First check (no locking) — fast path for already created instance
        if cls._instance is None:
            with cls._lock:
                # Second check (with lock) — ensures only one thread creates instance
                if cls._instance is None:
                    cls._instance = MySingleton()
        return cls._instance


# Example usage
obj1 = MySingleton.get_instance()
obj2 = MySingleton.get_instance()

print(obj1 is obj2)  # ✅ True


#this resolves synchornizing issue (expensive of conditional check when tonns of threads comes in)