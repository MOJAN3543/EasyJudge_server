import os
from subprocess import Popen, PIPE, TimeoutExpired, call
import time
import resource
import util.CustomException as CustomException
import util.ConfigParser as ConfigParser
from util.FileUtil import FileHandler

def limit_memory(limitMemory):
    resource.setrlimit(resource.RLIMIT_AS, (limitMemory, limitMemory))

def compile(code: str): # Only gcc!
    parser = ConfigParser.read()

    code = code.replace('�', '?') # EUC-KR -> UTF-8시 인코딩 누락된 한글을 대체하여 사용
    src_file = './' + parser['compile']['src_file']
    exe_file = './' + parser['compile']['exe_file']

    Handler = FileHandler(src_file, code)
    Handler.create() # Make source file

    compile_option = parser['compile']['compile_option'].split(' ')
    
    complie_cmd = ['gcc', src_file, '-o', exe_file] + compile_option
    complie_proc = Popen(complie_cmd, stderr=PIPE)
    error = complie_proc.communicate()[1]
    complie_proc.wait()

    Handler.remove()

    err_output = error.decode('utf-8')
    if "error:" in err_output:
        raise CustomException.CompileError(err_output)

def run(stdin: str, limitTime, limitMemory):
    parser = ConfigParser.read()
    exe_file = './' + parser['compile']['exe_file']
    run_code_cmd = [exe_file]

    Handler = FileHandler(exe_file, "")

    limitTime = min(limitTime, int(parser['run']['MAX_RUNTIME']))
    limitMemory = min(limitMemory, int(parser['run']['MAX_MEMORY'])) * 1024 * 1024

    stdin_byte = bytes(stdin, "utf-8")
    child_process = Popen(run_code_cmd, shell=True ,stdin=PIPE, stdout=PIPE, stderr=PIPE, preexec_fn=lambda:limit_memory(limitMemory))

    start_time = time.time()
    try:
        (stdout_bstr, stderr_bstr) = child_process.communicate(input=stdin_byte, timeout=limitTime)
    except:
        child_process.kill()
        raise CustomException.Timeout()
    finally:
        Handler.remove()

    end_time = time.time()

    total_time = end_time - start_time

    stdout_str = stdout_bstr.decode('utf-8')
    stderr_str = stderr_bstr.decode('utf-8')

    stdout = stdout_str
    stderr = stderr_str

    if(stderr != ""):
        raise CustomException.exeRuntimeError(stderr)
    
    return (stdout, stderr, total_time)
