word = input("문자열을 입력해라:").upper()
cloop = len(word)
he = 0
while he <cloop:
    he+=1
    if he != cloop:
        print(word, end=',')
    else:
        print(word)
    