class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x=str(x)#ת�����ַ�  
        if x[0]=='-':#Ϊ��ʱ  
            x=x[1:]#�ӵ�һ�����ֿ�ʼȡ  
            new_x='-'+x[::-1]#��ת  
        else:  
            new_x=x[::-1]  
        new_x=int(new_x)  
        if new_x>=-2**31 and new_x<=2**31-1:  
            return new_x  
        else:  
            return 0 