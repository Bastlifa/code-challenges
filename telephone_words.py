
digits_to_letters = {
    0: '0',
    1: '1',
    2: 'ABC',
    3: 'DEF',
    4: 'GHI',
    5: 'JKL',
    6: 'MNO',
    7: 'PQRS',
    8: 'TUV',
    9: 'WXYZ'
}
cache = {}
def num_to_word(num_str):
    
    if num_str == '':
        return []
    if num_str in cache:
        return cache[num_str]

    num_arr = [int(i) for i in num_str]
    new_words =[]

    if len(num_arr) == 1:
        for c in digits_to_letters[num_arr[0]]:
            new_words.append(c)
        cache[num_str] = new_words
        return new_words
        
    for w in num_to_word(num_str[1:]):
        for c in digits_to_letters[num_arr[0]]:
            new_words.append(''.join([c,w]))
            # new_words.append(c + w)

    cache[num_str] = new_words
    return new_words

print(num_to_word('274'))
