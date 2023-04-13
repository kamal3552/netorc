
class AcquireLockError(Exception):
    """Exception raised for lock unable to be acquired"""
    def __init__(self):
        self.message = "Unable to acquire task lock, a task using the same key is already running. Please try again."
        super().__init__(self.message)