data = [1,2,3,4,'Nan','missing']

def get_fre_words(text:str, norm = False)->dict:
    """Docstring"""
    if norm:
        text = text.lower()
        for char in {'.',',','*',"-"}:
            text = text.replace(char, ' ')
    fre_words = dict()
    words = text.split()
    for w in words:
        if w in fre_words:
            fre_words[w] += 1
        else:
            fre_words[w] = 1
    return fre_words