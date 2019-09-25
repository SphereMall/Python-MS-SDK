import json

import requests
import urllib
import urllib.parse
from ms_sdk.Lib.Http.Response import Response


class Request:

    def __init__(self, client, resource):
        """
        RequestHandler initializer.
        :param client:
        :param resource:
        """
        self.client = client
        self.resource = resource

    def handle(self, method: str, body: bool = False, uriAppend: str = '', queryParams: dict = {}):
        """
        :param method:
        :param body:
        :param uriAppend:
        :param queryParams:
        :return: Promise|Response
        """
        headers = {}
        _async = self.client.getAsync()

        url = self.client.getGatewayUrl() + '/' + self.client.getVersion() + \
            '/' + self.resource.getURI()

        # Base url should end without slash
        url = url.replace('?', '')
        url = url.rstrip('/')
        # url = url[:-1]

        # Append additional data to url
        if uriAppend:
            url += '/' + str(uriAppend)

        # Add query params
        if queryParams and method.lower() != 'post':
            url += '?' + \
                urllib.parse.unquote(urllib.parse.urlencode(queryParams))

        if body:
            if method.lower() == 'put':
                headers['body'] = urllib.parse.urlencode(queryParams)
            elif method.lower() == 'post':
                headers['Content-Type'] = 'application/x-www-form-urlencoded'
            elif method.lower() == 'delete':
                headers['body'] = urllib.parse.urlencode(queryParams)

        self.client.setCallStatistic(
            {'method': method, 'url': url, 'headers': headers})

        if _async:
            return {'method': method, 'url': url, 'headers': headers}

        Response(requests.request(method, url, headers=headers, data=body))
