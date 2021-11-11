## 파이썬 라이브러리 collections.deque

deque는 앞과 뒤에서 데이터를 처리할 수 있는 양방향 자료형이다. 양방향이기 때문에 스택(Stack)처럼 써도 되고 큐(Queue)처럼 써도 된다.

**from collections import deque**로 import 할 수 있다.

### method 종류

- append(item)
- appendleft(item)
- pop()
- popleft()
- extend(array)
- extendleft(array)
- remove(item)
- rotate(num)

### deque를 써야하는 이유

list의 경우 pop(0)의 시간복잡도가 O(N)인 반면,
deque의 경우 popleft()의 시간복잡도가 O(1)이다.
