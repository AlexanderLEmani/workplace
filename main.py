words = 'Hello how are you'
symbol_dic = {}

for char in words:
    if char not in symbol_dic:
        if char == " ":
            symbol_dic["space"] = 1
        symbol_dic[char] = 1
    else:
        if char == " ":
            symbol_dic["space"] += 1
        symbol_dic[char] += 1
print(symbol_dic)

print (sum([num for num in range(100) if "3" in str(num)]))
print ( " ".join(
    [
        word.upper()
        for word in words.split()
        if len(word) > 4
    ]
        )
)
