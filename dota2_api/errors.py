#!/usr/bin/env python


class BaseError(Exception):
    """
    Generic error wrapper.
    """
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return repr(self._msg)


class APIInsufficientArguments(BaseError):
    def __init__(self, query = None, params = None):
        self._msg = "HTTP 400: Insufficient arguments for \"{0}\". Parameters provided: {1}".format(query, params)


class APIAuthenticationError(BaseError):
    def __init__(self, api_key = None):
        self._msg = "HTTP 403: Authentication error caused by API key \"{}\".".format(api_key)


class APIMethodUnavailable(BaseError):
    def __init__(self, method_url = None):
        self._msg = "HTTP 404: \"{}\" is an unsupported/discontinued API method.".format(method_url)


class APITimeoutError(BaseError):
    def __init__(self):
        self._msg = "HTTP 503: Timeout error."
