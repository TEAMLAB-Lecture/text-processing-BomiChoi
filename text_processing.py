#######################
# Test Processing I   #
#######################

"""
NLP에서 흔히하는 전처리는 소문자 변환, 앞뒤 필요없는 띄어쓰기를 제거하는 등의 텍스트 정규화 (text normalization)입니다. 
이번 숙제에서는 텍스트 처리 방법을 파이썬으로 배워보겠습니다. 
"""


def normalize(input_string):
    li = input_string.lower().strip().split(' ')
    li_2 = []
    for l in li:
        if l != '':
            li_2.append(l)
    normalized_string = ' '.join(li_2)
    return normalized_string


def no_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    # no_vowel_string = input_string

    # for v in vowels:
    #     no_vowel_string.replace(v, '')

    # for i in range(len(no_vowel_string[:])):
    #     if i in vowels:
    #         del no_vowel_string[i]
    #         i -= 1

    no_vowel_string = ''
    for i in input_string:
        if i not in vowels:
            no_vowel_string += i

    return no_vowel_string
