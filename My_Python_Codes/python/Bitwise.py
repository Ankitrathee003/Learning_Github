# AND  &
# Or  |
# NOT -
# XOR ^
# LEFT-SHIFT <<
# RIGHT-SHIFT >>

x=13       # 1101
y=2      # 0010
print(x&y)
print(x|y)
print(~y)   # NOT operator will give 2'S complement here  x=13=01101 to find two complement just add one to it (11110) =14 and give sign of 1 st dight output is 1 so -ve (-14)
print(x^y)  # same ke liae 0 and different ke liae 1
print(x<<y)  # shifting Bits to LEFT
print(x>>y)  # shifting bits to Right