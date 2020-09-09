# import sqlite3
#
# conn = sqlite3.connect('Chinook_Sqlite.sqlite')
#
# cursor = conn.cursor()
#
#
# cursor.execute("SELECT Name FROM artists ORDER BY Name")
# result = cursor.fetchall()
# print(result)
# conn.close()

def find_missing_letter(chars):
    missingChar = ''
    for i in range(0, len(chars) - 1):
        if (ord(chars[i + 1]) - ord(chars[i]) > 1):
            missingChar = chr(ord(chars[i]) + 1)

    print(missingChar)
find_missing_letter(['O','Q','R','S'])
    #['  *  ', ' *** ', '*****']