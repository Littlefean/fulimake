"""
在这个模块中，定义一些自定义的中间件

"""


class Test1Middleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("===")
        response = self.get_response(request)
        print("===")
        return response


class Test2Middleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("+++")
        response = self.get_response(request)
        print("+++")
        return response


class IPLoggingMiddleware:
    """
    实现每过来一个请求就打印一个IP地址的功能
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 在请求处理之前执行的代码
        ip_address = request.META.get('REMOTE_ADDR')
        print(f"Received request from IP: {ip_address}")

        response = self.get_response(request)

        # 在请求处理之后执行的代码
        return response


class CorsMiddleware(object):
    """中间件：跨域访问"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_template_response(self, request, response):
        # 如果view 使用了render渲染response，使用这个中间件
        response["Access-Control-Allow-Origin"] = "*"
        return response

    def process_response(self, request, response):
        # 如果view使用HttpResponse, 将使用这个中间件
        response["Access-Control-Allow-Origin"] = "*"
        return response
