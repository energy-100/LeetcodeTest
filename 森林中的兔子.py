
import math
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res=0
        elems=set(answers)
        elemdict=dict()
        for elem in elems:
            counts=answers.count(elem)
            res+=(math.ceil(counts/(elem+1)))*(elem+1)
        return res

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res=0
        elems=set(answers)
        elemdict=dict()
        for elem in elems:
            counts=answers.count(elem)
            a=counts%(elem+1)
            b=counts//(elem+1) #双除号取商，除以 elem+1
            if a==0:
                res+=b*(elem+1) #乘以elem+1
            else:
                res+=(b+1)*(elem+1)
            # res+=(math.ceil(counts/(elem+1)))*(elem+1)
        return res