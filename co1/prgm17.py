dict={
    "one":101,
    "two":999,
    "three":888,
    "four":897,
    "five":345,
    "six":998
}
print("Ascending order:")
for i in sorted(dict.keys()):
    print(i,dict[i])
print("Descending order:")
for i in sorted(dict.keys(),reverse=-1):
    print(i,dict[i])