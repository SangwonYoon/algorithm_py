### 백트래킹 알고리즘

가능한 모든 방법을 탐색하는 '완전 탐색 기법' 중 하나로, 목표지점에 갈수 있는 **유망한 루트인지 탐색**하고, 유망하지 않은 루트라고 판단되면 빠르게 **백트래킹**하여 완전 탐색 기법의 효율을 높인다.

1. DFS 수행: DFS 알고리즘을 수행하여 노드를 찾는다.

2. 유망한 노드 검토: 현재 노드가 유망한 노드라면 DFS를 계속 진행하고, 그렇지 않으면 상위 노드로 돌아간다(백트래킹). -> 루트를 가지치기하여 효율성 증대
