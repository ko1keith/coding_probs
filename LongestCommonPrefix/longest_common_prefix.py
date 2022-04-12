class LongestCommonPrefix: 
    def longestCommonPrefix(self, strs):
        if len(strs) == 1:
            return strs[0]
        elif "" in strs:
            return ""
        
        
        lcp = '' 
        for i in range(len(min(strs, key=len))):
            index_chars = list(map(lambda string: string[i], strs))
            print(index_chars)
            if(index_chars.count(index_chars[0]) == len(index_chars)):
                lcp += index_chars[0][0]
            else:
                return lcp
        
        return lcp