sentence = '(1+2)+2*3+4'

postfixArray = []
fuhao = []

for c in sentence:
    if (c == '*') or (c == '/'):
        fuhao.append(c)
    elif (c == '+') or (c == '-'):
        while (fuhao != []) and ((fuhao[-1] == '*') or (fuhao[-1] == '/')):
            postfixArray.append(fuhao.pop())
        fuhao.append(c)
    elif c == '(':
        fuhao.append(c)
    elif c == ')':
        while fuhao[-1] != '(':
            postfixArray.append(fuhao.pop())
        fuhao.pop()
    else:
        postfixArray.append(c)


while fuhao != []:
    postfixArray.append(fuhao.pop())

print(postfixArray)

resultStack = []
for c in postfixArray:
    if c == '+':
        b = resultStack.pop()
        a = resultStack.pop()
        resultStack.append(a + b)
    elif c == '-':
        b = resultStack.pop()
        a = resultStack.pop()
        resultStack.append(a - b)
    elif c == '*':
        b = resultStack.pop()
        a = resultStack.pop()
        resultStack.append(a * b)
    elif c == '/':
        b = resultStack.pop()
        a = resultStack.pop()
        resultStack.append(a / b)
    else:
        resultStack.append(float(c))

print resultStack
