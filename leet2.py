
# lower_alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# upper_alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# leet_chars = ["4", "|3", "(", "|)", "3", "|=", "6", "|-|", "|", "9", "|<", "1", "|v|", "|/|", "0", "|*", "O,", "|2", "5", "7", "|_|", "|/", "|/|/", "><", "`/", "2"]


# def to_upper(message):
#     upper_case = ''
#     for letter in message:
#         if letter in lower_alpha:
#             for i in range(len(lower_alpha)):
#                 if letter == lower_alpha[i]:
#                     upper_case += upper_alpha[i]
#                     break
#         else:
#             upper_case += letter
#     return upper_case

# def to_leet(message):
#     upper_case = to_upper(message)
#     leet = ''
#     for letter in upper_case:
#         if letter in upper_alpha:
#             for i in range(len(upper_alpha)):
#                 if letter == upper_alpha[i]:
#                     leet += leet_chars[i]
#         else:
#             leet += letter
#     return leet

# message = raw_input("Enter some text:\n")
# leet_message = to_leet(message)
# print leet_message


#=========== Dictionary Version =========================
leet_dict = {
    'A': "4",
    'B': "|3",
    'C': "(",
    'D': "|)",
    'E': "3",
    'F': "|=",
    'G': "6",
    'H': "|-|",
    'I': "|",
    'J': "9",
    'K': "|<",
    'L': "1",
    'M': "|v|",
    'N': "|/|",
    'O': "0",
    'P': "|*",
    'Q': "O,",
    'R': "|2",
    'S': "5",
    'T': "7",
    'U': "|_|",
    'V': "|/",
    'W': "|/|/",
    'X': "><",
    'Y': "`/",
    'Z': "2"
}

def to_leet(message):
    upper_case = message.upper()
    leet = ''
    for letter in upper_case:
        if letter in leet_dict:
            letter = leet_dict[letter]
        leet += letter
    return leet

message = raw_input("Enter some text:\n")
leet_message = to_leet(message)
print leet_message

