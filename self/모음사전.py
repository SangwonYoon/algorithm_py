def make_string(words, w):
    if len(w) > 0:
        words.append(w)
    if len(w) == 5:
        return
    make_string(words, w+"A")
    make_string(words, w+"E")
    make_string(words, w+"I")
    make_string(words, w+"O")
    make_string(words, w+"U")

def solution(word):
    words = []
    make_string(words, "")
    words = list(set(words))
    words.sort()
    print(words)
    
    return words.index(word)+1