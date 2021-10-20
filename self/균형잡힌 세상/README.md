### sys.stdin.readline으로 입력을 받을 때 주의사항

rstrip() 메소드를 이용하지 않으면 개행문자(\n)이 포함되어 입력 받아진다.

### input()이 sys.stdin.readline()보다 느린 이유

1. input()은 파라미터 값으로 prompt message를 받아 출력을 한다. 반면 sys.stdin.readline()은 어떤 값도 출력하지 않음.

2. input()은 사용자 키 입력 값 하나 마다 버퍼에 저장을한다. 이때 입력의 종료가 되는 기준이 바로 개행 문자가 되는 것이다. 그래서 개행 문자를 생략해서 입력 값을 저장하게 되는 것이다.

반면 sys.stdin.readline()는 개행문자까지 포함한 하나의 줄을 한 번에 버퍼로 입력 받게 된다.
