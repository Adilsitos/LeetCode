class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        index = 0
        
        if len(needle) > len(haystack):
            return -1
        
        if len(needle) == 0 :
            return 0
        
        i = 0
        while len(haystack) != 0:
            
            if haystack[i] == needle[i] and len(haystack) >= len(needle):
                
                i += 1

                if i == len(needle):
                    return index 
            
            else:
                index += 1
                haystack = haystack[1:]
                i = 0
                
            
                
         
        return -1 
