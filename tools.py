from razdel import tokenize
from nltk.corpus import stopwords
import pymorphy2

def tokenize_and_base(text):
    morph = pymorphy2.MorphAnalyzer()

    russian_stopwords = set(stopwords.words('russian'))
    additional_stopwords = {'и', 'припев', 'но', 'я', 'в', 'но', 'что',
                            'мой', 'свой', 'весь', 'всё', 'на', 'мы', 'c', 'a','вест','это', 'сам'}
    russian_stopwords.update(additional_stopwords)
    words = [i.text for i in tokenize(text)]
    processed_words = []
    for word in words:
        # Remove punctuation
        if not word.isalpha():
            continue
        # Remove stopwords
        if word in russian_stopwords:
            continue
        parsed_word = morph.parse(word)[0]
        normal_form = parsed_word.normal_form
        if normal_form in russian_stopwords:
            continue
        processed_words.append(normal_form)
    return processed_words


if __name__ == '__main__':
    text = 'Припев:\n\nЯ ведь не из робких,\nВсе мне по плечу.\nСильный я и ловкий,\nВетра проучу!\n\nДул сильный ветер, крыши рвал.\nИ, несмотря на поздний час,\nВ округе вряд ли кто-то спал -\nСтихия не на шутку разошлась.\n\nНо вдруг какой-то парень с криком побежал\nИ принялся махать метлой:\n"Ах, ветер, негодяй, ты спать мне помешал,\nА ну-ка выходи на бой!"\n\n(Припев)\n\nИ ветер закружился, заметался\nИ ели начал с корнем рвать:\n"Откуда этот сумасшедший взялся,\nЧто хочет с ветром воевать".\n\nНо парень не сдавался и метлой махал,\nИ удалялся вглубь полей.\nИ впрямь неплохо с ветром воевал,\nА ветер становился злей...\n\n(Припев)\n\nНо вдруг метла со свистом улетела прочь\nИ храбрый парень вслед за ней.\nА после этого спокойней стала ночь -\nИсчез во мраке дуралей.\n\nЕго под утро пастухи нашли в стогу -\nОн очень крепко спал,\nА ветер песни напевал ему\nИ кудри ласково трепал.\n\n(Припев)  '
    result = tokenize_and_base(text)
    print(result)