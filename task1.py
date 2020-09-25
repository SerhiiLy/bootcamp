# There is string s = "string". Write the code that reverses
# string, i.e. returns "gnirts"


# 1
def reverse(string):
    return string[::-1]


s = "string"
reverse_string = reverse(s)
print(reverse_string)

# 2
print(''.join(list(reversed(s))))


# 3
def reverse3(string):
    reverse_word = ""
    for i in string:
        reverse_word = i + reverse_word
    return reverse_word


reverse_string3 = reverse3(s)
print(reverse_string3)
