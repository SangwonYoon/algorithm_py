### 좌표 압축 알고리즘

좌표들간에 값의 차이가 크고 정확한 값보다는 좌표의 대소 비교가 중요할 때 사용되는 알고리즘

각 좌표들의 값의 순위를 좌표의 값 대신 사용한다.

| 좌표 압축 전 | [0.0] | [1,1] | [0,2] | [2,0] | [0,3] | [3,2] | [1,4] | [4,4] | [100,50] | [150,30] |
| :----------: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :------: | :------: |
| 좌표 압축 후 | [0,0] | [1,1] | [0,2] | [2,0] | [0,3] | [3,2] | [1,4] | [4,4] |  [5,6]   |  [6,5]   |

### 이분 탐색 / 해시 탐색

**이분 탐색 알고리즘** : 데이터를 정렬한 뒤 탐색 범위를 절반씩 줄여가며 index를 탐색하는 알고리즘

이분 탐색의 시간 복잡도 : O(logN)

**해시 탐색 알고리즘** : 값과 index를 미리 연결해 둔 뒤 값을 통해 index를 탐색하는 알고리즘

해시 탐색의 시간 복잡도 : O(1)
