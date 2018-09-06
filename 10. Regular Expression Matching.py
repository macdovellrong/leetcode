import re
class Solution(object):
    def isMatch(self, s, p):
        ans = (re.match(p, s))
        if(ans == None):
            return False;
        if(ans.group(0) != s):
            return False;
        return True;
 