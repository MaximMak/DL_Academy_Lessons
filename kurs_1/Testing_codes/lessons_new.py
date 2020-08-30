# def duplicate_encode(word):
#     iter_word = str(word)
#     check_list = []
#     format_list = []
#     for i in iter_word:
#         if i not in check_list:
#             check_list.append(i)
#             i = '('
#             format_list.append(i)
#         else:
#             check_list.append(i)
#             i = ')'
#             format_list.append(i)
#     return '{}'.format(''.join(map(str, format_list)))

def song_decoder(song):
   print(' '.join(song.replace('WUB', ' ').split()))

song_decoder("AWUBWUBWUBBWUBWUBWUBC")

#your code here