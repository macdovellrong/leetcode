from collections import OrderedDict


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        Romandict = OrderedDict(M=1000, CM=900, D=500, CD=400, C=100, XC=90, L=50, XL=40, X=10, IX=9, V=5, IV=4, I=1)
        print(Romandict)
        Romandict_order = sorted(Romandict.items(), key=lambda obj: obj[1],reverse=True)

        str = ''
        if num == 0:
            return ''
        while num > 0:
            for Roman_tuple in Romandict_order:
                if (num - Roman_tuple[1]) >= 0 :
                    print(num,Roman_tuple)
                    num = num - Roman_tuple[1]
                    str += Roman_tuple[0]
                    break

        return str

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            num = int(line);

            ret = Solution().intToRoman(num)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()