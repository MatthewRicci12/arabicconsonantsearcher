import requests
import re

def space_remover(some_list):
    newlist = []

    for result in some_list:
        newresult = ''
        for letter in result:
            if letter != ' ':
                newresult += letter
        newlist.append(newresult)

    return newlist

def underscore_remover(some_list):
    newlist = []

    for result in some_list:
        newresult = ''
        for letter in result:
            if letter != '_':
                newresult += letter
        newlist.append(newresult)

    return newlist

def unicode_decoder(word):
    HEX_LENGTH = 8
    PERCENT_LENGTH = 6
    percent_charmap_decode = {'%D8%A7': 'ا', '%D8%A8': 'ب', '%D8%AA': 'ت', '%D8%AB': 'ث', '%D8%AC': 'ج', '%D8%AD':'ح',
                              '%D8%AE': 'خ', '%D8%AF': 'د', '%D8%B0': 'ذ', '%D8%B1': 'ر', '%D8%B2': 'ز', '%D8%B3': 'س',
                              '%D8%B4': 'ش', '%D8%B5': 'ص', '%D8%B6': 'ض', '%D8%B7': 'ط', '%D8%B8': 'ظ', '%D8%B9': 'ع',
                              '%D8%BA': 'غ', '%D9%81': 'ف', '%D9%82': 'ق', '%D9%83': 'ك', '%D9%84': 'ل', '%D9%85': 'م',
                              '%D9%86': 'ن', '%D9%87': 'ه', '%D9%88': 'و', '%D9%89':'ى', '%D8%A5': 'إ', '%D8%A3': 'أ',
                              '%D8%A9': 'ة', '%D8%A1': 'ء', '%D9%8A':'ي', '%D8%A6':'ئ'}

    hexamap_decode = {'\\xd8\\xa3': 'أ', '\\xd8\\xa5': 'إ', '\\xd8\\xa8': 'ب', '\\xd8\\xaa': 'ت', '\\xd8\\xab': 'ث',
                      '\\xd8\\xac': 'ج', '\\xd8\\xad': 'ح', '\\xd8\\xae': 'خ', '\\xd8\\xaf': 'د', '\\xd8\\xb0': 'ذ',
                      '\\xd8\\xb1': 'ر', '\\xd8\\xb2': 'ز', '\\xd8\\xb3': 'س', '\\xd8\\xb4': 'ش', '\\xd8\\xb5': 'ص',
                      '\\xd8\\xb6': 'ض', '\\xd8\\xb7': 'ط', '\\xd8\\xb8': 'ظ', '\\xd8\\xb9': 'ع', '\\xd8\\xba': 'غ',
                      '\\xd9\\x81': 'ف', '\\xd9\\x82': 'ق', '\\xd9\\x83': 'ك', '\\xd9\\x84': 'ل', '\\xd9\\x85': 'م',
                      '\\xd9\\x86': 'ن', '\\xd9\\x87': 'ه', '\\xd9\\x88': 'و', '\\xd9\\x8a': 'ي', '\\xd8\\xa1': 'ء',
                      '\\xd8\\xa9': 'ة', '\\xd9\\x89': 'ى', '\\xd8\\xa7': 'ا', '\\xd8\\xa6':'ئ'}

    newstring = ''

    is_hex = False
    is_percent = False

    if word[0] == "%":
        is_percent = True
    elif word[0] == "\\":
        is_hex = True

    if is_hex:
        for i in range(0, len(word), HEX_LENGTH):
            char = word[i:i + HEX_LENGTH]
            newstring += hexamap_decode[char]
    elif is_percent:
        for i in range(0, len(word), PERCENT_LENGTH):
            char = word[i:i + PERCENT_LENGTH]
            newstring += percent_charmap_decode[char]


    return newstring

def unicode_encoder(consonants):
    percent_charmap_encode = {"ا":"%D8%A7", "ب":"%D8%A8", "ت":"%D8%AA", "ث":"%D8%AB", "ج":"%D8%AC", "ح":"%D8%AD", "خ":"%D8%AE",
               "د":"D8%AF", "ذ":"%D8%B0", "ر":"%D8%B1", "ز":"%D8%B2", "س":"%D8%B3", "ش":"%D8%B4", "ص":"%D8%B5",
               "ض": "%D8%B6", "ط":"%D8%B7", "ظ":"%D8%B8", "ع":"%D8%B9", "غ":"%D8%BA", "ف":"%D9%81", "ق":"%D9%82",
               "ك":"%D9%83", "ل":"%D9%84", "م":"%D9%85", "ن":"%D9%86", "ه":"%D9%87", "و":"%D9%88", "ي":"%D9%89",
               "إ": "%D8%A5", "أ":"%D8%A3", "ة":"%D8%A9", "ى": "%D9%89", 'ء': "%D8%A1"
               }

    hexamap_encode = {'أ': '\\\\xd8\\\\xa3', 'إ': '\\\\xd8\\\\xa5', 'ب': '\\\\xd8\\\\xa8', 'ت': '\\\\xd8\\\\xaa', 'ث': '\\\\xd8\\\\xab',
     'ج': '\\\\xd8\\\\xac', 'ح': '\\\\xd8\\\\xad', 'خ': '\\\\xd8\\\\xae', 'د': '\\\\xd8\\\\xaf', 'ذ': '\\\\xd8\\\\xb0',
     'ر': '\\\\xd8\\\\xb1', 'ز': '\\\\xd8\\\\xb2', 'س': '\\\\xd8\\\\xb3', 'ش': '\\\\xd8\\\\xb4', 'ص': '\\\\xd8\\\\xb5',
     'ض': '\\\\xd8\\\\xb6', 'ط': '\\\\xd8\\\\b7', 'ظ': '\\\\xd8\\\\xb8', 'ع': '\\\\xd8\\\\xb9', 'غ': '\\\\xd8\\\\xba',
     'ف': '\\\\xd9\\\\x81', 'ق': '\\\\xd9\\\\x82', 'ك': '\\\\xd9\\\\x83', 'ل': '\\\\xd9\\\\x84', 'م': '\\\\xd9\\\\x85',
     'ن': '\\\\xd9\\\\x86', 'ه': '\\\\xd9\\\\x87', 'و': '\\\\xd9\\\\x88', 'ي': '\\\\xd9\\\\x8a', 'ء': '\\\\xd8\\\\xa1',
     'ة': '\\\\xd8\\\\xa9', 'ى': '\\\\xd9\\\\x89', 'ا': '\\\\xd8\\\\xa7'}
    # {'أ': '\\xd8\\xa3', 'إ': '\\xd8\\xa5', 'ب': '\\xd8\\xa8', 'ت': '\\xd8\\xaa', 'ث': '\\xd8\\xab',
    #  'ج': '\\xd8\\xac', 'ح': '\\xd8\\xad', 'خ': '\\xd8\\xae', 'د': '\\xd8\\xaf', 'ذ': '\\xd8\\xb0',
    #  'ر': '\\xd8\\xb1', 'ز': '\\xd8\\xb2', 'س': '\\xd8\\xb3', 'ش': '\\xd8\\xb4', 'ص': '\\xd8\\xb5',
    #  'ض': '\\xd8\\xb6', 'ط': '\\xd8\\b7', 'ظ': '\\xd8\\xb8', 'ع': '\\xd8\\xb9', 'غ': '\\xd8\\xba',
    #  'ف': '\\xd9\\x81', 'ق': '\\xd9\\x82', 'ك': '\\xd9\\x83', 'ل': '\\xd9\\x84', 'م': '\\xd9\\x85',
    #  'ن': '\\xd9\\x86', 'ه': '\\xd9\\x87', 'و': '\\xd9\\x88', 'ي': '\\xd9\\x8a', 'ء': '\\xd8\\xa1',
    #  'ة': '\\xd8\\xa9', 'ى': '\\xd9\\x89', "ا": "\\xd8\\xa7"}

    percentletters = []
    hexletters = []

    for letter in consonants:
        percentletters.append(percent_charmap_encode[letter])
        hexletters.append(hexamap_encode[letter])

    return (percentletters, hexletters)

def wiktsearcher(consonants):
    URL_HANDLE = r"https://en.wiktionary.org/w/index.php?title=Category:Arabic_lemmas&from="

    first_letter = consonants[0]
    url = URL_HANDLE + first_letter
    r = requests.get(url)

    content = r.content

    #print("Content:", content)

    percentstring, hexstring = unicode_encoder(consonants)
    print("Percentstring, hexstring:", percentstring, hexstring)

    #(?<=title=")[\w\\]*\\xd8\\xa7[\w\\]*
    percentregex = r"(?<=\/wiki\/)[\w%]*"
    hexregex = r'(?<=title=")[\w\\\s]*'
    for percent in percentstring:
        percentregex += percent + r"[\w%]*"

    for hex in hexstring:
        hexregex += hex + r"[\w\\\s]*"

    percentregex += r'\b'

    print("Percentregex, hexregex:", percentregex, hexregex)

    matches = set()

    percent_search = re.findall(percentregex, str(content))
    hex_search = re.findall(hexregex, str(content))
    percent_search = underscore_remover(percent_search)
    hex_search = space_remover(hex_search)

    print("Percent search, hex search:", percent_search, hex_search)

    matches = []

    for percentresult, hexresult in zip(percent_search, hex_search):
        toadd = (unicode_decoder(percentresult), unicode_decoder(hexresult))
        matches.append(toadd)

    return matches


def syllabizer(word):
    glyphs = {"b":"ب", "t":"ت", "th":"ث", "g":"ج", "H":"ح", "x":"خ", "d":"د", "dh":"ذ", "r":"ر", "z":"ز", "s":"س", "1":"ش",
                  "S":"ص", "D":"ض", "T":"ط", "Z":"ظ", "3":"ع", "gh":"غ", "f":"ف", "q":"ق", "k":"ك", "l":"ل", "m":"م", "n":"ن",
                  "h":"ه", "w":"و", "y":"ي", "aa":"ا", "ee":"ي", "oo":"و", "a":"أ", "i":"إ", "u":"ا", "An":"ا", "ä":"ة"}
    cons = []

    for letter in word:
        cons.append(glyphs[letter])

    return cons


def main():
    usr_input = input("Type the consonants: ")
    in_arabic = syllabizer(usr_input)

    print("User Input:", usr_input)
    print("In Arabic:", in_arabic)

    result = wiktsearcher(in_arabic)

    print(result)
    print()
    for tup in result:
        print(tup[0])







if __name__ == "__main__":
    main()