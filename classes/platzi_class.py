import requests
from bs4 import BeautifulSoup
import datetime
from .platzi_module import PlatziModule


class PlatziClass:
    PYTHON_PARSER = 'html.parser'
    RESPONSE_OK = 200

    def __init__(self, url):
        self.url = url
        self.soup = self.get_soup()

    def get_response(self):
        response = requests.get(self.url)
        if response.status_code == PlatziClass.RESPONSE_OK:
            return response
        else:
            raise Exception('An error occurred when making the resquest. Status code {}.'.format(response.status_code))

    def get_soup(self):
        response = self.get_response()
        return BeautifulSoup(response.text, PlatziClass.PYTHON_PARSER)

    def get_title(self):
        course_banner_title = self.soup.select('.CourseBanner-title')[0]
        return course_banner_title.span.text

    def get_modules(self):
        modules = self.soup.select('.Concept')
        return list(map(lambda module: PlatziModule(module), modules))

    def get_duration(self):
        total_duration = 0
        modules = self.get_modules()
        for module in modules:
            lessons = module.get_lessons()
            for lesson in lessons:
                total_duration += lesson.get_duration()
        return total_duration

    def get_formated_duration(self):
        class_duration = self.get_duration()
        return str(datetime.timedelta(minutes=class_duration))