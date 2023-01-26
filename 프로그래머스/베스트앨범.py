def solution(genres, plays):
    result = []
    songs = {}
    for i in range(len(genres)):
        if genres[i] not in songs:
            songs[genres[i]] = [[plays[i], -1], [plays[i], i]]
        else:
            songs[genres[i]].append([plays[i], i])
            songs[genres[i]][0][0] += plays[i]

    i = list(songs.values())
    i.sort(key = lambda x : x[0][0], reverse=True)
    print(i)

    for j in range(len(i)):
        i[j].pop(0)
        if len(i[j]) == 1:
            result.append(i[j][0][1])
        else:
            i[j].sort(key = lambda x : x[0], reverse=True)
            print(i[j])
            result.append(i[j][0][1])
            result.append(i[j][1][1])

    return result