import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)

'''
Чтобы это запомнить (хотя я практически всегда пользуюсь подсказкой), можно
использовать аббревиатуру DBES (Decode Bytes, Encode Strings), что означает
Декодирование Байтов, Кодирование Строк. Когда у вас есть байты, а вам
нужна строка, декодируйте байты. Если у вас есть строка, и вам нужно преобразовать
ее в байты, закодируйте строку.
'''
