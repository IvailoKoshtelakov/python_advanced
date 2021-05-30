def recursive_power(number, power):
    ll = []
    if power == 1:
        return
    ll.append(recursive_power(number, power - 1))


print(recursive_power(2, 10))
def palindrome(word, index=0, left_index=-1):
    if word[index] == word[left_index]:
        palindrome(word, index+1, left_index-1)