def is_anagram(str1: str, str2: str) -> bool:
    #Anagrams are words with the exact same letters but rearranged in different ways
    # Example of Anagrams: "listen", "silent". "Astronomer", "Moon starer".
    # cleaning the strings: removing spaces and and converting to lower()
    
    clean_str1 = str1.replace(" ", "").lower()
    clean_str2 = str2.replace(" ", "").lower()
    
    
    # to compare sorted character list, we use
    return sorted(clean_str1) == sorted(clean_str2)

# examples
print(is_anagram("listen", "silent")) #output will be true
print(is_anagram("hello", "world")) #output will be false
print(is_anagram("dormitory", "dirty room")) 
