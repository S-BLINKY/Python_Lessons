def is_palindrome(word):
    # a palindrome is a word which when turned or reflected does not change in spelling e.g level, bob, wow, beeb.
    word = word.lower()
    left = 0
    right = len(word) - 1
    
    while (left < right):
        if (word[left] != word[right]):
            return False
        
        left += 1
        right -= 1
        
    return True

result = is_palindrome("level")
print(result)

        
        