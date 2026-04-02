def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    
    """
    
    
    
    longest = ""
    
    for i in range(len(s)):
        for j in range(i+1, len(s)):  
            
            current = s[i:j+1]
            
            if current == current[::-1]:
                if len(current) > len(longest):
                    longest = current
                    
    return longest
        
        
        
        
        
    
    
    
