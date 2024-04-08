class CustomException(Exception):
    def __init__(self, status_code, error_message, stderr):
        self.status_code = status_code
        self.error_message = error_message
        self.stderr = stderr
    
class CompileError(CustomException):
    def __init__(self, stderr):
        super().__init__(400, "Compile Error", stderr)

class exeRuntimeError(CustomException):
    def __init__(self, stderr):
        super().__init__(500, "Runtime Error", stderr)
    
class MemoryLimit(CustomException):
    def __init__(self):
        super().__init__(413, "Memory Limit Exceeded", "")

class Timeout(CustomException):
    def __init__(self):
        super().__init__(408, "Timeout", "")

class RuntimeError(CustomException):
    def __init__(self, error_message):
        super.__init__(500, error_message, "")