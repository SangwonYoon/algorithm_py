def flipStr(i,string,flag):
    if flag != 0:
        string =  string[:flag] + string[i-1:flag-1:-1] + string[i:]
    else:
        string =  string[:flag] + string[i-1::-1] + string[i:]
    flag = -1
    return string, flag

string = input()
i = 0
flag = -1
while(i < len(string)):
    if string[i] == "<":
        if flag != -1:
            string, flag = flipStr(i,string,flag)
        i = string[i:].find(">") + i + 1
    elif string[i] == " ":
        string, flag = flipStr(i,string,flag)
        i += 1
    else:
        if flag == -1:
            flag = i
        i += 1

    if i == len(string) - 1:
        if flag != -1:
            string, flag = flipStr(i+1,string,flag)
        break

print(string)