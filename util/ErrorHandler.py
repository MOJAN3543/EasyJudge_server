from util.CustomException import CustomException
def error_handle(app):
    @app.errorhandler(CustomException)
    def handle_error(e):
        return {"message": e.error_message, "stderr": e.stderr}, e.status_code

    @app.errorhandler(Exception)
    def handle_error(e):
        return {"message": type(e).__name__, "stderr": ""}, 500