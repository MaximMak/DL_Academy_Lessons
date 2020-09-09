def first_non_repeating_letter(string):
    if string != '' and string & string != string:
        print(sorted(string, key=lambda x: (string.count(x), string.index(x)))[0])
    else:
        print(string)

first_non_repeating_letter('~><#~><')