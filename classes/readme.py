from .platzi_class import PlatziClass
from .markdown import Markdown
import os


class Readme:
    FILE_NAME = 'README.md'
    FILE_MODE_W = 'w'
    RESOURCES_LINE = 'Resources:'
    NEW_LINE_CHAR = '\n'
    INDEX_INDENTATION_LEVEL_1 = '* '
    INDEX_INDENTATION_LEVEL_2 = '  - '
    INDEX_INDENTATION_LEVEL_3 = '    + '

    def __init__(self, course_url, name=None, path=None):
        self.course_url = course_url
        self.name = name
        self.path = path
        self.file_name = self.get_file_name()
        self.validate_file_name(self.file_name)
        self.platzi_class = PlatziClass(self.course_url)

    def get_file_name(self):
        if self.name and not self.path:
            return self.name
        elif not self.name and self.path:
            file_name_with_path = self.path + Readme.FILE_NAME
            self.validate_file_name(file_name_with_path)
            return file_name_with_path
        elif self.name and self.path:
            file_name_with_path = self.path + self.name
            self.validate_file_name(file_name_with_path)
            return file_name_with_path

        return Readme.FILE_NAME

    def validate_file_name(self, file_name):
        if os.path.isfile(file_name):
            print('Error: a file with that name already exists.')
            exit(1)

    def create_readme(self):
        file = open(self.file_name, Readme.FILE_MODE_W)

        link_class_title = Markdown.link(self.platzi_class.get_title(),
                                         self.platzi_class.url)
        class_title = Markdown.h1(link_class_title)
        file.write(class_title)
        file.write(Readme.NEW_LINE_CHAR * 2)

        file.write(self.create_index())

        modules = self.platzi_class.get_modules()
        for module in modules:
            module_title = Markdown.h2(module.get_title())
            file.write(module_title)
            file.write(Readme.NEW_LINE_CHAR * 2)

            lessons = module.get_lessons()
            for lesson in lessons:
                link_lesson_title = Markdown.link(lesson.get_title(), lesson.get_link())
                lesson_title = Markdown.h3(link_lesson_title)
                file.write(lesson_title)
                file.write(Readme.NEW_LINE_CHAR * 4)
                file.write(Markdown.hr())
                file.write(Readme.NEW_LINE_CHAR * 2)
        file.write(Markdown.h4(Readme.RESOURCES_LINE, True))
        file.close()

    def create_index(self):
        index = ''

        class_title = self.platzi_class.get_title()
        index_class_title = Readme.INDEX_INDENTATION_LEVEL_1 + Markdown.index_link(class_title)
        index += index_class_title
        index += Readme.NEW_LINE_CHAR

        modules = self.platzi_class.get_modules()
        for module in modules:
            module_title = module.get_title()
            index_module_title = Readme.INDEX_INDENTATION_LEVEL_2 + Markdown.index_link(module_title)
            index += index_module_title
            index += Readme.NEW_LINE_CHAR

            lessons = module.get_lessons()
            for lesson in lessons:
                lesson_title = lesson.get_title()
                index_lesson_title = Readme.INDEX_INDENTATION_LEVEL_3 + Markdown.index_link(lesson_title)
                index += index_lesson_title
                index += Readme.NEW_LINE_CHAR
        index += Readme.NEW_LINE_CHAR
        return index
