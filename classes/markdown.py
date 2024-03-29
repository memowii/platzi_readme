class Markdown:
    SPECIAL_CHARS_DICT = {
        'á': '%C3%A1',
        'é': '%C3%A9',
        'í': '%C3%AD',
        'ó': '%C3%B3',
        'ú': '%C3%BA',
        'ñ': '%C3%B1',
        '¿': '%C2%BF'
    }

    VALID_CHARS = [
        '¿'
    ]

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
        word_array = Markdown.get_words_array(text)
        return '#' + '-'.join(word_array)

    @staticmethod
    def change_special_chars(text):
        changed_text = text
        for special_char, symbol in Markdown.SPECIAL_CHARS_DICT.items():
            if special_char in changed_text:
                changed_text = changed_text.replace(special_char, symbol)
        return changed_text

    @staticmethod
    def is_valid_char(char):
        return char.isalpha() or char in Markdown.VALID_CHARS

    @staticmethod
    def get_words_array(text):
        word_array = []
        i = 0
        while i < len(text):
            if Markdown.is_valid_char(text[i]):
                word = ''
                while i < len(text) and Markdown.is_valid_char(text[i]):
                    word += text[i]
                    i += 1
                changed_word = Markdown.change_special_chars(word.lower())
                word_array.append(changed_word)
            i += 1
        return word_array

    @staticmethod
    def index_link(text):
        return Markdown.link(text, Markdown.slug(text))