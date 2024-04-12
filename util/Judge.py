from flask import Flask, request
from flask_restx import Api, Resource, fields, Namespace
import requests
import runcode.CodeRunner as CodeRunner
import threading
from util.FileUtil import FileHandler, FileChecker, FileReader
import util.ConfigParser as ConfigParser



Judge = Namespace("Judge")
thread_lock = threading.Lock()

file_fields = Judge.model("File", {"filename" : fields.String, "contents" : fields.String})
judge_fields = Judge.model("Judge Input", {"code" : fields.String, "stdin": fields.String, "fileList": fields.List(fields.Nested(file_fields))})

@Judge.route('')
class JudgePost(Resource):
    @Judge.expect(judge_fields)
    def post(self):
        with thread_lock: # Block concurrent requests
            setting = request.json.get('setting')
            code = request.json.get('code')
            stdin = request.json.get('stdin')
            fileList = request.json.get('fileList') # "[{"filename":"f1.txt", contents:"Hello, World!"}, {"filename":"f2.txt", ... }]"
            fileHandlerList = list()

            for file in fileList:
                if file["filetype"] == "output":
                    continue
                filename = file["filename"]
                contents = file["contents"]
                Handler = FileHandler(filename, contents)
                Handler.create()
                fileHandlerList.append(Handler)

            limitTime = setting["limitTime"]
            limitMemory = setting["limitMemory"]

            CodeRunner.compile(code)
            Checker = FileChecker()
            Checker.getFiles()

            try:
                (stdout, stderr, total_time) = CodeRunner.run(stdin, limitTime, limitMemory)
            finally:
                for Handler in fileHandlerList:
                    Handler.remove()
                newFileList = Checker.getNewFiles()
                for newFile in newFileList:
                    Reader = FileReader(newFile)
                    contents = Reader.read()
                    FileList.append({"filename": newFile, "contents": contents})
                    Reader.remove()
            

            FileList = list()

                
            FileList.sort(key=lambda a: a["filename"])

            return {"stdout" : stdout, "stderr": stderr, "runtime": total_time, "fileList": FileList}
