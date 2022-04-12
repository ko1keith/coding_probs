class ImplementStrStr():
    def strStr(self, haystack, needle):
        if needle == "" or needle == haystack:
            return 0
        elif needle not in haystack:
            return -1
        
        substr = ""
        for i in range(len(haystack)):
            #build substr
            substr += haystack[i]
            # #compare needle to substr
            if needle in substr:
                return i - (len(needle) - 1)
            
        return -1