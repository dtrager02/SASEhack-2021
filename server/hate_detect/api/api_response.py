from typing import Type
from flask import jsonify

class Serializable:
    
    def serialize(self) -> dict:
        raise NotImplementedError()

class APIResponse:

    def __init__(self, is_error: bool, error_message: str, status_code: int, 
                        response_body: Type[Serializable]) -> None:
        self.is_error = is_error
        self.error_message = error_message
        self.status_code = status_code
        self.response_body = response_body

    def serialize_response_body(self):
        if (self.response_body):
            return self.response_body.serialize()
        return None

    def make(self):
        return jsonify({
            "isError": self.is_error,
            "errorMessage": self.error_message,
            "response": self.serialize_response_body()
        })

    @staticmethod
    def error(message, status_code):
        return APIResponse(True, message, status_code, None)

    @staticmethod
    def success(response_body):
        return APIResponse(False, "Operation completed successfully", 200,
            response_body)

class AddData(Serializable):

    def __init__(self, success) -> None:
        self.success = success

    def serialize(self) -> dict:
        return {
            "success": self.success
        }

class DetectSpeech(Serializable):

    def __init__(self, success, score) -> None:
        self.success = success
        self.score = score
    
    def serialize(self) -> dict:
        return {
            "success": self.success,
            "score": self.score
        }
