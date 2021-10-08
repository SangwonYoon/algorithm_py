str1 = '!' + input()
str2 = '@' + input()
memo = [[0]*len(str2) for i in range(len(str1))]

for i in range(1,len(str2)):
    for j in range(1,len(str1)):
        if str1[j] != str2[i]: memo[j][i] = max(memo[j-1][i], memo[j][i-1])
        else: memo[j][i] = memo[j-1][i-1] + 1

print(memo[len(str1)-1][len(str2)-1])