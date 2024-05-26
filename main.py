word = input()
symbol_dic = {}

for char in word:
    if char not in symbol_dic:
        if char == " ":
            symbol_dic["space"] = 1
        symbol_dic[char] = 1
    else:
        if char == " ":
            symbol_dic["space"] += 1
        symbol_dic[char] += 1
print(symbol_dic)
