def count_x(word):
    count = 0
    if word == '':
        return 0
    first_letter = word[0]
    if first_letter == 'x':
        count+=1
        
    return count + count_x(word[1:])

print(count_x(input()))
