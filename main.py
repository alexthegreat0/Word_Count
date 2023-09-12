#Made by Alexandre Wilbur in 2023

def wordcounter():
    chaineacompter = str(input("Quel est votre chaine de mots?"))
    if chaineacompter == "a" or "I" or "A" or "i":
        print("La chaine contien 1 mots!")
    word_count = 0
    nmb1 = 0
    nmb2 = 1
    aaa = chaineacompter
    limit = len(chaineacompter)
    trieswithletter = 0
    while nmb2 < limit:
        aaa = str(chaineacompter[nmb1:nmb2])
        nmb1 = nmb1 + 1
        nmb2 = nmb2 + 1
        if aaa == " " and trieswithletter >= 1:
            word_count = word_count + 1
            trieswithletter = 0
        elif aaa != " ":
            trieswithletter = trieswithletter + 1
        if nmb2 == limit:
            if trieswithletter > 0:
                print("La chaine contien", word_count + 1, "mots!")
                exit()
            elif trieswithletter == 0:
                print("La chaine contien", word_count, "mots!")
                exit()
wordcounter()