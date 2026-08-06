sentence = "my life is better today than yesterday. I am happy"
sentence = sentence.lower()
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in text:
        if char in vowels:
            count += 1
    return count
result = count_vowels(sentence)
print(result)

# to make a string declear true if it is lowercased, we use the function "islower()"
# but to make a string use other functions such as count or anyother, we put a "." after its declearation e.g sentenced.