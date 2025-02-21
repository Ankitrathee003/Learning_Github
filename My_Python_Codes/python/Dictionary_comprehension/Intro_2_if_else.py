# ODD_EVEN
d={i:'even' if i%2==0 else 'odd' for i in range(1,11) }
# print(d)




# ord('a') gives the Unicode code point of the lowercase letter 'a'.
# ord('z') gives the Unicode code point of the lowercase letter 'z'.
# chr(i) converts a Unicode code point i back to its corresponding character.
alphabet_dict = {chr(i):i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)}
print(alphabet_dict)