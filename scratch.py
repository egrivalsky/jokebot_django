from datamuse import datamuse
datamuse = datamuse.Datamuse()






def related_words(word):
    related = datamuse.words(rel_jja=word)
    print(word)
    word_list = []
    for n in related:
        related_words = n['word']
        word_list.append(related_words)
    print(word_list)


related_words('octopus')