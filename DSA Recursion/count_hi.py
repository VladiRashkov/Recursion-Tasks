def count_hi(word):
    return int(word[0:2]=="hi") + count_hi(word[1:]) if len(word) >=2 else 0
print(count_hi(input()))