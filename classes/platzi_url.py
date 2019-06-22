import re
from urllib.parse import urlparse


class PlatziUrl:

    @staticmethod
    def is_valid_url(url):
        parse_result = urlparse(url)
        return bool(parse_result.scheme) and bool(parse_result.netloc)

    @staticmethod
    def is_platzi_class(path):
        match_object = re.search('^/clases/.*?/', path)
        return len(match_object.group(0)) == len(path)

    @staticmethod
    def is_platzi_url(url):
        if PlatziUrl.is_valid_url(url):
            parse_result = urlparse(url)
            return parse_result.netloc == 'platzi.com' and PlatziUrl.is_platzi_class(parse_result.path)