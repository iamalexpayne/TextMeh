import requests

class ArgumentOutOfRangeException(Exception):
    def __init__(self, message):
        self.message = message.replace('ArgumentOutOfRangeException: ', '')
        super(ArgumentOutOfRangeException, self).__init__(self.message)


class TranslateApiException(Exception):
    def __init__(self, message, *args):
        self.message = message.replace('TranslateApiException: ', '')
        super(TranslateApiException, self).__init__(self.message, *args)


class Translator(object):
    """Implements Microsoft Cognitive Services Text Translation API"""

    base_url = "http://api.microsofttranslator.com/V2/Ajax.svc"

    def __init__(self, subscription_key):
        self.subscription_key = subscription_key
        self.access_token = None

    def get_access_token(self):
        response = requests.post(
            'https://api.cognitive.microsoft.com/sts/v1.0/issueToken?Subscription-Key=%s' % self.subscription_key,
            data=None
        )

        if "error" in response:
            raise TranslateApiException(
                response.get('error_description', 'No Error Description'),
                response.get('error', 'Unknown Error')
            )
        return response.text

    def call(self, path, params):
        """Calls the given path with the params urlencoded

        :param path: The path of the API call being made
        :param params: The parameters dictionary
        """
        if not self.access_token:
            self.access_token = self.get_access_token()

        resp = requests.get(
            "/".join([self.base_url, path]),
            params=params,
            headers={'Authorization': 'Bearer %s' % self.access_token}
        )
        resp.encoding = 'UTF-8-sig'
        return resp.json()

    def translate(self, text, to_lang, from_lang=None, content_type='text/plain', category='general'):
        params = {
            'text': text.encode('utf8'),
            'to': to_lang,
            'contentType': content_type,
            'category': category,
        }
        if from_lang is not None:
            params['from'] = from_lang
        return self.call("Translate", params)

    def get_languages(self):
        return self.call('GetLanguagesForTranslate', '')

    def detect_language(self, text):
        params = {
            'text': text.encode('utf8')
        }
        return self.call('Detect', params)
