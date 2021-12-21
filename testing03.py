from strsimpy.longest_common_subsequence import LongestCommonSubsequence

lcs = LongestCommonSubsequence()
x = "Boğa burcunun rengi nedir?"
x_x = "Rengi sarı"
y = "Boğa burcunun günleri nedir?"
y_y = "Boğa burcunun günü salı"
b = "Boğa burcu para kazanır mı?"
b_b = "Boğa burcu parayı iyi kazanır"
c = input(": ")
print("value")
print(lcs.distance(str(x), c))
print(lcs.distance(str(y), c))
print(lcs.distance(str(b), c))
if lcs.distance(str(x), c) <= 7:
    print(x_x)
elif lcs.distance(str(y), c) <= 7:
    print(y_y)
elif lcs.distance(str(b), c) <= 7:
    print(b_b)
else:
    print("Söylediğinizi anlayamıyorum.")

