from .platzi_lesson import PlatziLesson


class PlatziModule:

    def __init__(self, soup_module):
        self.module = soup_module

    def get_title(self):
        return self.module.header.div.h3.text

    def get_lessons(self):
        lessons = self.module.section.contents
        return list(map(lambda lesson: PlatziLesson(lesson), lessons))