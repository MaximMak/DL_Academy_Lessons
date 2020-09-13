def first_non_repeating_letter(string):
    dick = {}
    for s in string:
        dick.update({s: dick.get(s, 0)+1})
    # проверка на регистр
        if s.isupper():
            dick.update({s.lower(): dick.get(s)})
        else:
            dick.update({s.upper(): dick.get(s)})
    result = ''
    dick_len = len(dick)
    i=0
    while True:
        if i >= dick_len:
            break
        else:
            item = list(dick.items())[i]
            if item[1] == 1:
                result = item[0]
                break
        i += 1
    return result

first_non_repeating_letter('~><#~><')