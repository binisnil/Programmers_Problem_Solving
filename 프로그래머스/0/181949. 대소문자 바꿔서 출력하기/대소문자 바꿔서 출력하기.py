str = input()
s = ""
for char in str:
    if ord(char) >= 97:
        s += chr(ord(char) - 32)
    elif ord(char) <= 90:
        s += chr(ord(char) + 32)

print(s)