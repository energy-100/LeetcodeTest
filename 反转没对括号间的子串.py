class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [''] #先放入一个空

        for st in s:
            if st == "(":
                tmp = ''
                stack.append(tmp)
            elif st == ")": #这里是elif
                for i in range(len(stack[-1])):
                    stack[-2] += stack[-1][-(i + 1)]
                stack.pop() #反转之后要移除最后一个元素
            else:
                stack[-1] += st

        return stack[-1]



if __name__ == '__main__':
    s=Solution()
    print(s.reverseParentheses('(abcd)'))
