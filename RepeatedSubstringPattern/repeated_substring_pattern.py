class RepeatedSubstringPattern():
    def repeatedSubstringPattern(self, s):
        if(len(s) == 1):
            return False        
        
        substr = ''
        count = 0
        while len(substr) < len(s):
            substr += s[count] # Loop1: a | Loop2: ab | Loop3: aba | Loop4: abac 
            multiple = len(s) / len(substr) # Loop1: 4 | Loop2: 2 | Loop3: 1.33
            print(multiple)
            print(substr * multiple)
            print(s)
            if(multiple != 1):
                if substr * multiple == s: # Loop1: a*6 -> aaaaaa == ababab ?  |  $ Loop2: ab*2 = abab == abac ?  
                    return True
            count += 1 #Loop1: 0 | Loop2: 1

        return False