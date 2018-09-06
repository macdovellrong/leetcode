class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str_tmp = ""
        flag = 0
        if str == "":
            return 0
        for i in range(len(str)):
            if str[i] == " " and flag == 0:
                continue
            if str[i] == '-' and str_tmp == "" and flag == 0:
                str_tmp += str[i]
                flag = 1
                continue
            if str[i] == '+' and str_tmp == "" and flag == 0:
                flag = 1
                continue
            if str[i] in ["0","1","2","3","4","5","6","7","8","9"]:
                str_tmp += str[i]
                print str_tmp
                flag = 1
                continue
            else:
                print "aaa"
                break
        
        if str_tmp == '' or str_tmp == '-' or str_tmp == '+':
            return 0
        if int(str_tmp) < (-2**31):
            return -2**31
        if int(str_tmp) > (2**31 - 1):
            return 2**31 - 1
        return int(str_tmp)