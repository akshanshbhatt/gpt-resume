from django import http


class CorsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if (
            request.method == "OPTIONS"
            and "HTTP_ACCESS_CONTROL_REQUEST_METHOD" in request.META
        ):
            response = http.HttpResponse()
            response["Content-Length"] = "0"
            response["Access-Control-Max-Age"] = 86400
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = (
            "DELETE, GET, OPTIONS, PATCH, POST, PUT"
        )
        response["Access-Control-Allow-Headers"] = (
            "accept, accept-encoding, authorization, content-type, dnt, origin, user-agent, x-csrftoken, x-requested-with"
        )
        return response
