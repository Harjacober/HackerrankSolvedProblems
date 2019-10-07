def minion_game(string):
    stuartscore = 0
    kevinscore = 0
    vowel = "AEIOU"
    lenstring = len(string)
    for i in range(lenstring):
        if string[i] in vowel:
            kevinscore += lenstring-i
        else:
            stuartscore += lenstring-i
    if stuartscore > kevinscore:
        print("Stuart {}".format(stuartscore))
    elif kevinscore > stuartscore:
        print("Kevin {}".format(kevinscore))
    else:
        print("Draw")
