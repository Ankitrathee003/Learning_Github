#sq={1:1,2:4,3:9,4:16}
# sq={x:x**2 for x in range(1,5)}
# print(sq)


# sq1={f'{x} square is':x**2 for x in range(1,5)}
# print(sq1)


# sq2={f'{x} square is':x**2 for x in range(1,5)}
# for a,b in sq2.items():
#     print(a,b)


x="ankitrathee"
word_count={i: x.count(i) for i in x}
print(word_count)
