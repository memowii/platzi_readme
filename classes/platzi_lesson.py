import re


class PlatziLesson:
    MINUTES_PATTERN = '(\d+):(\d+)'
    HOST_NAME = 'https://platzi.com'

    def __init__(self, soup_lesson):
        self.lesson = soup_lesson

    def get_link(self):
        return PlatziLesson.HOST_NAME + self.lesson.a['href']

    def get_title(self):
        return self.lesson \
                   .select('.MaterialContent-title')[0] \
                   .text

    def get_duration(self):
        text_duration = self.lesson \
                            .select('.MaterialContent-duration')[0] \
                            .text
        matches = re.search(PlatziLesson.MINUTES_PATTERN, text_duration)
        text_minutes = matches.group(1)
        return int(text_minutes)