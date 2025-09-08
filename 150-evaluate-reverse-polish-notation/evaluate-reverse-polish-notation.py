class Solution(object):
    def evalRPN(self, tokens):
        operator='+-*/'
        while len(tokens)!=1:
            i=0
            while i<len(tokens) and operator.find(str(tokens[i]))==-1:
                i+=1
            if operator.find(tokens[i])==0:
                tokens=tokens[:i-2]+[int(tokens[i-2])+int(tokens[i-1])]+tokens[i+1:]
            elif operator.find(tokens[i])==1:
                tokens=tokens[:i-2]+[int(tokens[i-2])-int(tokens[i-1])]+tokens[i+1:]
            elif operator.find(tokens[i])==2:
                tokens=tokens[:i-2]+[int(tokens[i-2])*int(tokens[i-1])]+tokens[i+1:]
            else:
                tokens=tokens[:i-2]+[float(tokens[i-2])/float(tokens[i-1])]+tokens[i+1:]
        return int(tokens[0])