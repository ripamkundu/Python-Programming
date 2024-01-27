input = "Ripam Kundu"
# Output = "mapiR udnuK"

words = []
word = " "
for char in input:
    if char == " ":
        words.append(word[::-1])
        
        word = " "
    else:
        word = word + char
words.append(word[::-1])
# r = words[::-1]
o = " ".join(words)
print(o)