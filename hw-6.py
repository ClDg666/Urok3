def int_func(text):
    length = len(text)
    first = text[0].upper()
    last = text[1:length].lower()
    text_new = first + last
    return str(text_new)
    # print(text_new)


print(int_func('каравелла'))