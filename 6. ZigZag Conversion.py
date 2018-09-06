class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s == "":
            return s
        if numRows == 1:
            return s
        if len(s)%(2*numRows - 2) > 0:
            columns = len(s)/(2*numRows - 2) + 1
        else:
            columns = len(s)/(2*numRows - 2)
        
        #print len(s)
        #print columns
        
        
        a = 2*numRows -2
        s_tmp = ""
        for i in range(numRows):
            for j in range(columns):
                #print i
                #print j
                #print "======"
                if i == 0 or i == (numRows - 1):
                    if (j*a + i) < len(s):
                        s_tmp = s_tmp + s[j*a + i]
                else:
                    if (j*a + i) < len(s):
                        s_tmp = s_tmp + s[j*a + i]
                    if (j*a + a - i) < len(s):
                        s_tmp = s_tmp + s[j*a + a -i]
        return s_tmp