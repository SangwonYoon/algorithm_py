### 너비 우선 탐색 알고리즘(BFS, Breadth First Search)

수빈이가 동생을 찾을 수 있는 가장 빠른 시간을 구하는 문제이므로 너비 우선 탐색을 이용해야 한다.

수빈이가 이동할 수 있는 위치는 X를 기준으로 X-1, X+1, X\*2이다.

자식 노드를 3개 이하로 갖는 트리를 그린다. (X-1, X+1, X\*2 중 이전 노드와 중복되지 않는 것)

![트리 구조](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbSqr8h%2Fbtqx2TOmWM5%2Fom66GLkkc3rCkFNxKzrYlk%2Fimg.png)

트리 구조를 list에 옮긴다. list의 인덱스값 I는 노드의 값, list의 I번 인덱스의 값은 I값을 갖는 노드의 깊이를 의미한다.

동생의 위치인 K번 인덱스의 값을 구할때 까지 너비 우선 탐색을 실시한다.
