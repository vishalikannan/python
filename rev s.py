def reverse(str):
    s = ""
    for ch in str:
        s = ch + s
    return s
mystr = "aabbcc"
print(reverse(mystr))
