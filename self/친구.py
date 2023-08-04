# 친구

n = int(input()) # 50보다 작거나 같은 자연수

friend = [] # 2-친구의 수를 저장하는 리스트
network = [] # 친구 네트워크를 입력받아 저장하는 리스트
network_cp = [] # network의 복사본 리스트

for i in range(n):
    temp = list(input())
    network.append(temp.copy())
    network_cp.append(temp.copy())

for me in range(n):
    myfriends = network[me]
    for f in range(len(myfriends)):
        if myfriends[f] == "Y":
            for ff in range(len(network[f])):
                if network[f][ff] == "Y" and ff != me and network_cp[me][ff] == "N":
                    network_cp[me][ff] = "Y"
    friend.append(network_cp[me].count("Y"))

print(max(friend))