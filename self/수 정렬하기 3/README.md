## 카운팅 정렬(계수 정렬)

1. 요소 값들끼리 서로 비교하지 않고 정렬하는 알고리즘
2. 최소값과 최대값의 간격이 클 수록 필요한 메모리의 크기가 증가한다.

### 제한사항

1. 정수로 표현할 수 있는 자료에 대해서만 적용 가능
2. 자료의 범위를 알고 있어야 한다.

### 정렬 과정

다음과 같은 수열 A를 정렬하는 상황

_A : 5, 5, 3, 4, 5, 1, 0, 4, 1, 3, 0, 2, 4, 2, 3, 0_

1. 배열의 최대값 + 1의 길이를 갖는 배열을 생성해준다.

2. 각 숫자가 몇번 등장하는지 세어 해당 인덱스의 배열 값을 1 증가시킨다.
   ex) i가 등장했으면 -> arr[i]++

|   숫자    |  0  |  1  |  2  |  3  |  4  |  5  |
| :-------: | :-: | :-: | :-: | :-: | :-: | :-: |
| 등장 횟수 |  3  |  2  |  2  |  3  |  3  |  3  |

3. 등장 횟수를 누적합으로 바꿔준다.

- 등장 횟수만큼 작은 순서대로 print해주면 되는데 누적합을 구하는 이유는?

0,2,0,100,2,0 같은 수열을 정렬할 때 3~99까지는 무의미한 순회를 하기 때문에 불필요한 탐색을 줄이고자 누적합을 구함

|  숫자  |  0  |  1  |  2  |  3  |  4  |  5  |
| :----: | :-: | :-: | :-: | :-: | :-: | :-: |
| 누적합 |  3  |  5  |  7  | 10  | 13  | 16  |

4. 원래 배열을 선형 탐색하면서 누적합 배열을 거쳐 출력 배열에 값을 입력한다.

   출력 배열에 삽입 후 누적합 배열의 값을 1 감소시킨다.
   ![이미지 1](https://blog.kakaocdn.net/dn/QiWZZ/btq89vkmDh7/40myVsVLfxYVPs9fKtu7s0/img.png)
   (C : 누적합)

### 시간 복잡도

O(n)이 소요된다.
