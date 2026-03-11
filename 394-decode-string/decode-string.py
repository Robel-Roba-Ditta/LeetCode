class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:       
            if i == ']':
                ans = ""
                while stack and stack[-1] != '[':
                    ans = stack.pop() + ans 
                stack.pop()

                temp =""
                while stack and stack[-1].isdigit():
                    temp = stack.pop() + temp
                stack.append(int(temp) * ans)    
            else:
                stack.append(i)
        return "".join(stack)
        