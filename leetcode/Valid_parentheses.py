class Solution(object):
    def isValid(self, s):
        k = len(s)
        while len(s) > 0:
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")
                
            if len(s) == k:
                return False
            else:
                k = len(s)
        return True
        
        
        