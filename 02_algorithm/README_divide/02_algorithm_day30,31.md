# :notebook_with_decorative_cover: 02_algorithm - Day30, 31

<br>

## 23. 10월10일(30일차) - `Tree`

### 23.1 트리의 정의 및 용어

------

:checkered_flag: <b>트리의 대표 특징</b>

- `싸이클이 없는 무향 연결 그래프`
- `비선형 구조`

------

<img src="https://user-images.githubusercontent.com/52685250/66529554-d543c980-eb3e-11e9-9b40-20eb93b7c497.JPG" alt="트리" width="600px">

- 한 개 이상의 노드로 이루어진 유한 집합
  - 루트(root) : 노드 중 부모가 없는 노드
    - 위 트리에서 루트 노드는  `A`이다.
  - 루트의 서브 트리(subtree) : 나머지 노드들은 n(>=0)개의 분리 집합 T1, ..., TN으로 분리될 수 있으며 이들은 각각의 하나의 트리가 됨(재귀적 정의)
  - 리프 노드(leaf node)(단말 노드) : 맨 끝에 있는 노드들
    - 위 트리에서 단말 노드는 `E`, `K`, `G`, `H`, `I`, `J` 가 해당된다.
- 용어 : `노드`, `간선`, `루트 노드`, `형제 노드`, `조상 노드`, `서브 트리`, `자손 노드`, `차수(degree)`, <b>`트리의 높이`</b>
  - <b>`트리의 높이`</b> : 트리에 있는 노드의 높이 중에서 가장 큰 값. 최대 레벨
  - 트리에서 <b>`높이`</b>의 개념이 중요하다!
  - 이를 이용하여 시간 복잡도도 계산할 수 있다.

<br>

### 23.2 이진 트리(Binary Tree)

#### (1) 기본 개념

- 모든 노드들의 최대 2개의 서브 트리를 갖는 특별한 형태의 트리
- 레벨 i에서 노드의 최대 개수는 2<sup>i</sup>개
- 높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수는 h+1개가 되며, 최대 개수는 2<sup>h+1</sup>-1개가 된다.

<br>

#### (2) 이진 트리의 종류

- `포화 이진 트리(Full Binary Tree)`

  <img src="https://user-images.githubusercontent.com/52685250/66530067-22c13600-eb41-11e9-8aaa-9e975ca94ede.JPG" alt="포화이진트리" width="600px">

  - 모든 레벨에 노드가 포화상태로 채워져 있는 이진 트리
  - 높이가 h일 때 최대의 노드 개수인 2<sup>h+1</sup>-1 의 노드를 가진 이진 트리
  - 루트를 1번으로 하여 2<sup>h+1</sup>-1까지 정해진 위치에 대한 노드 번호를 가진다. 이렇게 하면 위치를 쉽게 찾을 수 있다.

- `완전 이진 트리(Complete Binary Tree)`

  <img src="https://user-images.githubusercontent.com/52685250/66530113-57cd8880-eb41-11e9-8d62-7ea0a6e84316.JPG" alt="완전이진트리" width="600px">

  - 높이가 h이고 노드 수가 n개일 때, `포화 이진 트리의 노드 번호 1번부터 n번까지 빈 자리가 없는` 이진 트리
  - 위 트리는 노드가 10개인 완전 이진 트리임
  - 앞으로 알고리즘을 접하면서 `완전 이진 트리`를 가장 많이 쓰게 된다.

- `편향 이진 트리(Skewed Binary Tree)`

  <img src="https://user-images.githubusercontent.com/52685250/66530185-b3981180-eb41-11e9-852c-45edbd1af443.JPG" alt="편향이진트리" width="600px">

  - 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진 트리
  - 이진 트리 중에서 가장 피해야 할 제일 안 좋은 이진 트리

<br>

#### (3) 순회(Traversal)

- 트리의 각 노드를 중복되지 않게 전부 방문(visit) 하는 것
- 트리는 비선형 구조이므로 선형 구조에서와 같이 선후 연결 관계를 알 수 없다.

##### ① 전위 순회(preorder traversal)

<img src="https://user-images.githubusercontent.com/52685250/66530536-1d64eb00-eb43-11e9-876c-570ea6371e02.JPG" alt="전위순회" width="650px">

##### ② 중위 순회(inorder traversal)

<img src="https://user-images.githubusercontent.com/52685250/66530583-5604c480-eb43-11e9-80e5-361652ee3a8d.JPG" alt="중위순회" width="650px">

##### ③ 전위 순회(postorder traversal)

<img src="https://user-images.githubusercontent.com/52685250/66530619-75035680-eb43-11e9-8fc1-0eb6e4d4d82a.JPG" alt="후위순회" width="650px">

<br>

### 23.3 트리의 표현

#### (1) 배열을 이용한 이진 트리의 표현

- 이진 트리에 각 노드 번호를 부여
  - 루트의 번호를 1로 부여
  - 레벨 n에 있는 노드에 대하여 왼쪽부터 오른쪽으로 2<sup>n</sup> 부터 2<sup>n+1</sup> - 1까지 번호를 차례대로 부여

<img src="https://user-images.githubusercontent.com/52685250/66531778-f4932480-eb47-11e9-8568-2cbd1b358767.JPG" width="650px">

- 노드 번호의 성질
  - 노드 번호가 i인 노드의 부모 노드 번호 : i / 2
  - 노드 번호가 i인 노드의 왼쪽 자식 노드 번호 : 2*i
  - 노드 번호가 i인 노드의 오른쪽 자식 노드 번호 : 2*i+1
  - 레벨 n의 노드 번호 시작 번호 : 2<sup>n</sup>
  - 노드 번호를 배열의 인덱스로 사용한다!
- 배열을 이용한 이진 트리의 표현의 단점
  - 편향 이진 트리의 경우 사용하지 않는 배열 원소에 대한 메모리 공간 낭비 발생
  - 트리의 중간에 새로운 노드를 삽입하거나 기존의 노드를 삭제할 경우 배열의 크기 변경이 어려워 비효율적이다.

<br>

#### (2) 연결리스트를 이용한 이진 트리의 표현

<img src="https://user-images.githubusercontent.com/52685250/66536498-1c8a8400-eb58-11e9-9b71-5b1ddce02397.JPG" alt="연결리스트로 이진트리 표현" width="700px">

- 배열을 이용한 이진 트리의 표현의 단점을 해결
- 이진 트리의 모든 노드는 최대 2개의 자식 노드를 가지므로 일정한 구조의 단순 연결 리스트 노드를 사용하여 구현

<br>

> <b>[연습문제]간선의 수가 `V`이고 연결 정보가 `arr`일 때, 전위 / 중위 / 후위 순회 결과를 출력</b>
>
> `input_01.txt`
>
> ```
> 13
> 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
> ```
>
> `practice_01.py`
>
> ```python
> import sys
> sys.stdin = open('input_01.txt', 'r')
> 
> def preorder(n): # 전위 순회
>  if n != 0:
>      print(n, end=' ')
>      preorder(child[n][0])
>      preorder(child[n][1])
> 
> def inorder(n): # 중위 순회
>  if n != 0:
>      inorder(child[n][0])
>      print(n, end=' ')
>      inorder(child[n][1])
> 
> def postorder(n): # 후위 순회
>  if n != 0:
>      postorder(child[n][0])
>      postorder(child[n][1])
>      print(n, end=' ')
> 
> V = int(input()) # 간선의 수
> arr = list(map(int, input().split()))
> child = [[0, 0] for i in range(V + 1)]
> 
> for i in range(V - 1):
>  if child[arr[i * 2]][0] == 0: # 부모 노드 i*2에 자식 노드가 없는 경우
>      child[arr[i * 2]][0] = arr[i * 2 + 1]
>  else: # 이미 자식이 한 개 있는 경우
>      child[arr[i * 2]][1] = arr[i * 2 + 1]
> 
> print('전위 순회 결과: ', end=' ')
> preorder(1)
> print()
> 
> print('중위 순회 결과: ', end=' ')
> inorder(1)
> print()
> 
> print('후위 순회 결과: ', end=' ')
> postorder(1)
> ```
>
> `result`
>
> ```
> 전위 순회 결과:  1 2 4 7 12 3 5 8 9 6 10 11 13
> 중위 순회 결과:  12 7 4 2 1 8 5 9 3 10 6 13 11
> 후위 순회 결과:  12 7 4 2 8 9 5 10 13 11 6 3 1
> ```

<br>

### 23.4 이진 탐색 트리

#### (1) 기본 개념

- 탐색작업을 효율적으로 하기 위한 자료구조
- 모든 원소는 `서로 다른 유일한 키`를 갖는다. (`중복된 값 X`)
- key(왼쪽 서브 트리) < key(루트 노드) < key(오른쪽 서브 트리)
- 왼쪽 서브 트리와 오른쪽 서브 트리도 이진 탐색 드리다.
- 중위 순회하면 오름차순으로 정렬된 값을 얻을 수 있다.

<br>

#### (2) 탐색 연산

<img src="https://user-images.githubusercontent.com/52685250/66536880-7b043200-eb59-11e9-96ab-4e3a1786a172.JPG" alt="탐색연산" width="600px">

- 루트에서 탐색 시작
- `탐색할 키 값 x`를 `루트 노드의 키 값 k`와 비교
  - x == k : 탐색 성공
  - x < k : 루트 노드의 왼쪽 서브 트리에 대해서 탐색연산 수행
  - x > k : 루트 노드의 오른쪽 서브 트리에 대해서 탐색연산 수행
- 서브 트리에 대해서 순환적(재귀적)으로 탐색 연산을 반복하고 탐색 수행할 서브 트리가 없으면 탐색 실패

<br>

#### (3) 삽입 연산

<img src="https://user-images.githubusercontent.com/52685250/66537021-ef3ed580-eb59-11e9-8218-034d3caf5ce8.JPG" alt="삽입연산" width="750px" height="280px">

- 먼저 탐색 연산을 수행
  - 삽입할 원소와 같은 원소가 트리에 있으면 삽입할 수 없으므로, `같은 원소에 트리에 있는지 탐색하여 확인`한다.
  - 탐색에서 `탐색 실패가 결정되는 위치`가 삽입 위치가 된다.
- 탐색 실패한 위치에 원소를 삽입한다.

<br>

#### (4) 삭제 연산 <a href="https://robodream.tistory.com/192" target="_blank">(이미지 출처)</a>

##### ① 삭제할 노드가 단말 노드인 경우(차수 = 0)

<img src="https://user-images.githubusercontent.com/52685250/66540788-f967d080-eb67-11e9-999e-3d7dd65bd2d0.JPG" width="600px">

- 단말 노드는 자식 노드를 갖지 않으므로 단말 노드를 삭제하고 부모 노드를 찾아서 링크 필드를 NULL로 설정하여 연결을 끊어줌

##### ② 삭제할 노드가 하나의 자식 노드(서브 트리)를 가진 경우(차수 = 1)

<img src="https://user-images.githubusercontent.com/52685250/66540789-f967d080-eb67-11e9-81aa-51dae95c93cb.JPG" width="600px">

- 삭제되는 노드가 왼쪽이나 오른쪽 서브 트리 중 하나만 갖는 경우 그 노드는 삭제하고 서브 트리를 부모 노드를 향하도록 함

##### ③ 삭제할 노드가 두 개의 자식 노드(서브 트리)를 가진 경우(차수 = 2)

<img src="https://user-images.githubusercontent.com/52685250/66540790-f967d080-eb67-11e9-9b7c-b005741e123a.JPG" width="600px">

- 노드를 삭제하면 자식 노드들은 트리에서 연결이 끊어지게 됨
- 노드가 삭제된 후에도 이진 탐색 드리가 유지되어야 하므로 트리를 재구성해야 함
- 자손 노드 중에 삭제한 노드의 자리에 들어올 노드를 선택해야 함
- 이때 삭제 노드와 가장 비슷한 값을 가진 노드를 삭제 노드 위치로 가져와야 함
- 삭제 노드와 가장 비슷한 값을 가진 노드는 왼쪽 서브 트리에서 가장 큰 키 값을 가진 노드이거나 오른쪽 서브 트리에서 가장 작은 키 값을 가진 노드
  - 왼쪽 서브 트리에서 가장 큰 키 값을 갖는 노드 선택
  - 오른쪽 서브 트리에서 가장 작은 키 값을 갖는 노드 선택

<br>

#### (5) 이진 탐색 트리의 성능

- 연산의 시간 : 트리의 높이만큼 걸린다. => `O(h)` (h : BST의 깊이(height))
  - 그만큼 트리에서 `트리의 높이`가 매우 중요하다!
- 평균의 경우
  - 이진 트리가 균형적으로 생성되어 있는 경우
  - `O(logn)`
- 최악의 경우
  - 한쪽으로 치우친 편향 이진 트리의 경우
  - `O(n)`
  - 순차탐색과 시간복잡도가 같다.

<br>

### 23.5 힙(heap)

#### (1) 기본 개념

- <font color="red"><b><u>완전 이진 트리</u></b></font>에 있는 노드 중에서 키 값이 가장 큰 노드나 키 값이 가장 작은 노드를 찾기 위해서 만든 자료구조
- 최대 힙(max heap)
  - 키 값이 가장 큰 노드를 찾기 위한 <b>완전 이진 트리</b>
  - 부모 노드의 키 값 > 자식 노드의 키 값
  - 루트 노드 : 키 값이 가장 큰 노드
- 최소 힙(min heap)
  - 키 값이 가장 작은 노드를 찾기 위한 <b>완전 이진 트리</b>
  - 부모 노드의 키 값 < 자식 노드의 키 값
  - 루트 노드 : 키 값이 가장 작은 노드

<br>

#### (2) 삽입 연산

<img src="https://user-images.githubusercontent.com/52685250/66541251-9d9e4700-eb69-11e9-84bf-d9f2ca390eee.JPG" width="700px">

<img src="https://user-images.githubusercontent.com/52685250/66541252-9d9e4700-eb69-11e9-8b88-91f61d352ef6.JPG" width="700px">

- `23삽입`과 같은 과정을 `힙 재구성`이라고 한다.

<br>

#### (3) 삭제 연산

- 힙에서는 루트 노드의 원소만을 삭제할 수 있다.
- 루트 노드의 원소를 삭제하여 반환한다.
- 힙의 종류에 따라 최대값 또는 최소값을 구할 수 있다.
  - 우선순위 큐와 비교

<img src="https://user-images.githubusercontent.com/52685250/66541428-3df46b80-eb6a-11e9-82ed-06e28a217644.JPG" width="700px">

<br>

#### (4) 활용

- 우선순위 큐를 구현하는 가장 효율적인 방법
  - 노드 하나의 추가 / 삭제가 시간 복잡도가 O(logN)이고 최대값 / 최소값을 O(1)에 구할 수 있다.
  - 완전 정렬보다 관리 비용이 적다.
- 배열을 통해 트리 형태를 쉽게 구현할 수 있다.
  - 부모나 자식 노드를 O(1)연산으로 쉽게 찾을 수 있다.
  - n 위치에 있는 노드의 자식은 2<sup>n</sup> 과 2<sup>n+1</sup> 위치한다.
  - 완전 이진 트리의 특성에 의해 추가 / 삭제 위치는 자료의 시작과 끝 인덱스로 쉽게 판단할 수 있다.
  - 루트 노드부터 1번으로 인덱스 번호 시작

<br>

#### (5) 힙 정렬

- 힙 정렬 과정
  - 힙에서 루트 노드의 키 값을 출력
  - 힙의 마지막 노드를 루트 노드로 가정하여 나머지 노드들로 새로운 힙을 만듬
  - 새로 만들어진 힙 트리의 루트 노드를 출력하고 앞에서 만든 힙의 마지막 노드를 루트 노드로 가정하여 새로운 힙을 만드는 과정을 반복
- 힙 정렬의 시간 복잡도
  - N개의 노드 삽입 연산(O(logN)) + N개의 노드 삭제 연산(O(logN))
  - 따라서, 전체 정렬은 `O(NlogN)`이다.
  - 힙 정렬은 수행 시간이 빠르다.
- 힙 정렬은 배열에 저장된 자료를 정렬하기에 유용하다.

<br>

## 24. 10월11일(31일차) - `Tree 문제풀이`

### 24.1 [문제] 이진 탐색

```python
def inorder(n):
    global idx
    if n <= N:
        inorder(n * 2)
        arr[n] = idx
        idx += 1
        inorder(n * 2 + 1)

for tc in range(int(input())):
    N = int(input())
    idx = 1
    arr = [0] * (N + 1)
    inorder(1)
    print('#{} {} {}'.format(tc + 1, arr[1], arr[N // 2]))
```

<br>

### 24.2 [문제] 이진 힙

```python
def heap_check(n):
    p, c = n // 2, n
    while True:
        if c <= 1 or arr[p] < arr[c]: break
        arr[p], arr[c] = arr[c], arr[p]
        c, p = p, c // 2

for tc in range(int(input())):
    N = int(input())
    input_data = list(map(int, input().split()))
    arr = [0] * (N + 1)
    for idx in range(N):
        arr[idx + 1] = input_data[idx]
        heap_check(idx + 1)
    result = 0
    while True:
        N = N // 2
        if N == 0: break
        result += arr[N]
    print('#{} {}'.format(tc + 1, result))
```

