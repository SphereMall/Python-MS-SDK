import requests
import urllib
import urllib.parse

from .AuthToken import AuthToken
from .Response import Response

class Request:

    def __init__(self, client, resource):
        self.client = client
        self.resource = resource


    def handle(self, method, body = False, uriAppend = False,  queryParams = []):
        _async = self.client.getAsync()
        options = []

        # Set user authorization
        # if not _async:
            # options = self.setAuthorization()

        # Generate request URL
        url = self.client.getGatewayUrl() + '/' + self.client.getVersion() + '/' + self.resource.getURI()
        
        # Base url should end without slash
        url = url.replace('?', '')
        url = url.rstrip('/')

        # Append additional data to url
        if uriAppend:
            url += '/' + str(uriAppend)
        print(uriAppend)
        print(url)
        # Add query params
        if queryParams:
            url += '?' + urllib.parse.unquote(urllib.parse.urlencode(queryParams))

        if body:
            if method.lower() == 'put':
                options['body'] = urllib.parse.urlencode(queryParams)
            elif method.lower() == 'post':
                options['content-type'] = 'application/x-www-form-urlencoded'
                options['form_params'] = body
            elif method.lower() == 'delete':
                options['body'] = urllib.parse.urlencode(queryParams)



        self.client.setCallStatistic({'method':method, 'url':url, 'options':options})

        if _async:
            return {'method':method, 'url':url, 'options':options}
        
        if method.lower() == 'get':
            # print(requests.get(url, options).text['data'])
            return Response(requests.get(url, options))

    
    # def setAuthorization():
        # authToken = AuthToken(self.client)