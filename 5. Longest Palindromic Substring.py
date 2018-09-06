class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_tmp='#'+'#'.join(s)+'#'

        RL=[0]*len(s_tmp)
        MaxRight=0
        pos=0
        MaxLen=0
        final_pos = 0
        for i in range(len(s_tmp)):
           if i<MaxRight:
               RL[i]=min(RL[2*pos-i], MaxRight-i)
           else:
               RL[i]=1
           #尝试扩展，注意处理边界
           while i-RL[i]>=0 and i+RL[i]<len(s_tmp) and s_tmp[i-RL[i]]==s_tmp[i+RL[i]]:
               RL[i]+=1
           #更新MaxRight,pos
           if RL[i]+i-1>MaxRight:
               MaxRight=RL[i]+i-1
               pos=i
           #更新最长回文串的长度
           #MaxLen=max(MaxLen, RL[i])
           if MaxLen >= RL[i]:
               pass
           else:
               MaxLen = RL[i]
               final_pos = i
        
        start = final_pos-MaxLen+1
        end = final_pos+MaxLen-1
        if s_tmp[start] == '#':
            start = start + 1
            end = end - 1
        
        return s[(start - 1)/2:(end-1)/2 + 1]