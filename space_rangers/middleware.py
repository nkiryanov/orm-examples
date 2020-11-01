import logging

logger = logging.getLogger('requests')


class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        logger.info('request logged')

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        logger.info('response logged')

        return response