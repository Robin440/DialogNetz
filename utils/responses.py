from rest_framework.response import Response
from rest_framework import status


# Follow the standard when sending response
# Ref: https://medium.com/@bojanmajed/standard-json-api-response-format-c6c1aabcaa6d
# {
#     "success": true,
#     "message": "User logged in successfully",
#     "error_code": 1306,
#     "data": { } / []
# }

# 'addon_res' contains the success, error code and can be message sometimes.


def HTTP_200(data=None, message=None, error={},) -> Response:
    res = {
        "data": data,
        "message": message,
        "error": error,
        "success": True,
        "error_code": None
    }
    return Response(res, status=status.HTTP_200_OK)

def HTTP_204(data=None, message=None, error={},) -> Response:
    res = {
        "data": data,
        "message": message,
        "error": error,
        "success": False,
        "error_code": None
    }
    return Response(res, status=status.HTTP_204_NO_CONTENT)

def HTTP_400(data={}, error={}) -> Response:
    res = {
        "data": data,
        "error": error,
        "success": False,
        "error_code": None
    }
    return Response(res, status=status.HTTP_400_BAD_REQUEST)

def HTTP_403(data={}, error={}) -> Response:
    res = {
        "data": data,
        "error": error,
        "success": False,
        "error_code": None
    }
    return Response(res, status=status.HTTP_403_FORBIDDEN)

def HTTP_404(data={}, error={}) -> Response:
    res = {
        "data": data,
        "error": error,
        "success": False,
        "error_code": None
    }
    return Response(res, status=status.HTTP_404_NOT_FOUND)

def HTTP_201(data=None, message=None, error={},) -> Response:
    res = {
        "data": data,
        "message": message,
        "error": error,
        "success": False,
        "error_code": None
    }
    return Response(res, status=status.HTTP_201_CREATED)



def HTTP_401(data=None, message=None, error={},) -> Response:
    res = {
        "data": data,
        "message": message,
        "error": error,
        "success": False,
        "error_code": None
    }
    return Response(res, status=status.HTTP_401_UNAUTHORIZED)

def HTTP_422(data={}, error={}) -> Response:
    res = {
        "data": data,
        "error": error,
        "success": False,
        "error_code": None
    }
    return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
