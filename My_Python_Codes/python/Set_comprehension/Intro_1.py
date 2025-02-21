s={i**2 for i in range(1,11)}
print(s,type(s))

z=['ankit','rathee','hariom']
x={i[::-1] for i in z} #individual string will be reversed but order may change
print(x)