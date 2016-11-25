def removeVowels(s, i):
    if len(s) == 1:
        if s == "a" or s == "e" or s == "i" or s == "o" or s == "u":
            return "No consonant(s) in "+s
        else:
            return s

        
    if i == len(s) - 1:
        if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
            s = s.replace(s[i], "")
            return s
        else:
            return s 
    else:
        if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
            s = s.replace(s[i], "")
            return removeVowels(s, i)
        else:
            return removeVowels(s, i+1)

print removeVowels("beautiful", 0) 
            
            
        
        
    
