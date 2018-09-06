class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x=str(x)#转换成字符  
        if x[0]=='-':#为负时  
            x=x[1:]#从第一个数字开始取  
            new_x='-'+x[::-1]#翻转  
        else:  
            new_x=x[::-1]  
        new_x=int(new_x)  
        if new_x>=-2**31 and new_x<=2**31-1:  
            return new_x  
        else:  
            return 0 