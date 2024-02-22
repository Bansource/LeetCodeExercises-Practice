# The string that is inserted gets checked by the for loop and inserts
# in a new string. However it goes in the opposite direction

word = input()
password = ''

for index in range(len(word) - 1, -1, -1):  # Starts at -1, and gets inserted in the string backwards
    letter = word[index]
    if letter == 'i':
        password += '!'  # adds the ! to the empty string if letter matched
    elif letter == 'a':
        password += '@'
    elif letter == 'm':
        password += 'M'
    elif letter == 'B':
        password += '8'
    elif letter == 'o':
        password += '.'
    else:
        password += letter  # adds the letter if not any of the above

password += 'q*s'

print(password)
