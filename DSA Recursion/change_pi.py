def change_pi(word):
    if len(word)<2:
        return word
    
    if word[0:2] == "pi":
        return '3.14'+ change_pi(word[2:])
    
    else: 
        return word[0] + change_pi(word[1:])

print(change_pi(input()))