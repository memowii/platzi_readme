class Markdown:
    SPECIAL_CHARS_DICT = {
        'á': '%C3%A1',
        'é': '%C3%A9',
        'í': '%C3%AD',
        'ó': '%C3%B3',
        'ú': '%C3%BA',
        'ñ': '%C3%B1'
    }

    @staticmethod
    def h1(text, toc=False):
        return '# {}{}'.format(text, ' <!-- omit in toc -->' if toc else '')

    @staticmethod
    def h2(text, toc=False):
        return '## {}{}'.format(text, ' <!-- omit in toc -->' if toc else '')

    @staticmethod
    def h3(text, toc=False):
        return '### {}{}'.format(text, ' <!-- omit in toc -->' if toc else '')

    @staticmethod
    def h4(text, toc=False):
        return '#### {}{}'.format(text, ' <!-- omit in toc -->' if toc else '')

    @staticmethod
    def hr():
        return '---'

    @staticmethod
    def link(text, href):
        return '[{}]({})'.format(text, href)

    @staticmethod
    def slug(text):
        word_array = Markdown.get_word_array(text)
        return '#' + '-'.join(word_array)

    @staticmethod
    def change_special_chars(text):
        changed_text = text
        for special_char, symbol in Markdown.SPECIAL_CHARS_DICT.items():
            if special_char in changed_text:
                changed_text = changed_text.replace(special_char, symbol)
        return changed_text

    @staticmethod
    def get_word_array(text):
        word_array = []
        i = 0
        while i < len(text):
            if text[i].isalpha():
                word = ''
                while i < len(text) and text[i].isalpha():
                    word += text[i]
                    i += 1
                changed_word = Markdown.change_special_chars(word.lower())
                word_array.append(changed_word)
            i += 1
        return word_array

    @staticmethod
    def index_link(text):
        return Markdown.link(text, Markdown.slug(text))