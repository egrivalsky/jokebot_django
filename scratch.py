from datamuse import datamuse
datamuse = datamuse.Datamuse()






def related_words(word):
    if ' ' in word:
        words = word.split(' ')
        for word in words:
            related = datamuse.words(rel_jja=word)
            print(word)
            word_list = []
        print("if statement complete")


    related = datamuse.words(rel_jja=word)
    print(word)
    word_list = []
    for n in related:
        related_words = n['word']
        word_list.append(related_words)
    print("words for " + word + " : ")
    print(word_list)


related_words('octopus helper telephone')