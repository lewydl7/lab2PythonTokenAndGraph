import nltk


def open_file(path):
    try:
        file = open(path, "r+")
        return path
    except IOError as e:
         print(e)


class TextReader:

    @staticmethod
    def read_tokens_txt(path):
        path = open_file(path)
        with open(path, "r+", encoding='utf-8') as file:
            for l in file:
                for word in l.split():
                    for token in nltk.word_tokenize(word):
                        yield token

    @staticmethod
    def read_tokens_conll(path):
        path = open_file(path)
        with open(path, "r+", encoding='utf-8') as file:
            for l in file:
                yield l.split()[0][1:-1]

    @staticmethod
    def read_sentences_txt(path):
        path = open_file(path)
        with open(path, "r+", encoding='utf-8') as file:
            temp = ''
            flag = False
            for c in file.read():
                if flag:
                    if c.isupper():
                        yield temp.strip()
                        temp = ''
                    if not c.isspace():
                        flag = False
                    temp += c
                else:
                    temp += c
                    if c == '.':
                        flag = True
            yield temp

    @staticmethod
    def read_sentences_conll(path):
        path = open_file(path)
        with open(path, "r+", encoding='utf-8') as file:
            temp = ''
            flag = False
            for line in file:
                line, token_type = line.split()[0][1:-1], line.split()[2]
                if token_type == 'Interp':
                    flag = False
                if flag:
                    temp += ' '
                temp += line
                flag = True
                if line == '.':
                    yield temp
                    temp = ''
                    flag = False

if __name__ == '__main__':
    for t in TextReader.read_sentences_conll('nkjp.conll'):
        print(t)
