# 04. Cookie vs Session

<br>

## (1) HTTP 프로토콜의 특징

- 쿠키와 세션을 사용하는 이유는 HTTP 프로토콜의 특징이자 약점을 보완하기 위해 사용된다. 간단하게 HTTP 프로토콜의 특징을 살펴보자.
- **비연결지향(Connectionless)** : 클라이언트와 서버가 한 번 연결을 맺은 후, 클라이언트 요청에 대해 서버가 응답을 마치면 맺었던 연결을 끊어버리는 성질
- **상태정보 유지 안함(Stateless)** : 연결이 끊어지는 순간 클라이언트와 서버간의 통신이 끝남(각각 완벽하게 독립적)
- 비연결지향이라는 특성 덕분에 계속해서 커넥션을 유지하지 않기 때문에 서버 리소스 낭비가 줄어드는 것은 아주 큰 장점이지만, 통신할 때마다 새로 커넥션을 만들기 때문에 클라이언트 측면에서는 상태를 유지(ex. 인증에 쓰이는 상태, ...)를 위해 통신할 때마다 어떤 절차를 가져야하는 단점이 생긴다.

<br>

## (2) Cookie

- **클라이언트의 로컬에 저장**되는 키, 값의 작은 데이터파일
- **Text 형태**로 데이터가 저장
- 웹페이지에 접속하면 요청한 웹페이지를 서버로부터 받고 쿠키를 로컬에 저장하고, 클라이언트가 재요청시에 웹페이지 요청과 함께 쿠키 값도 매 헤더에 추가해서 보내기 때문에 상당한 트래픽을 발생시킨다.
- 결제정보등을 쿠키에 저장하였을때 쿠키가 유출되면 `보안에 대한 문제점`도 발생할 수 있다.
- 하나의 쿠키는 **4[KB]** 정도의 용량 제한이 있고 한 도메인 당 최대 쿠키 수는 **20개**로 제한되어 있다.
  - 클라이언트도 모르게 접속되는 사이트에 의하여 설정될 수 있기 때문에 쿠키로 인해 문제가 발생하는 걸 막기 위함
- ex) 아이디 자동완성 / 공지 메세지 하루 안보기 / 팝업 안보기 체크 / 비로그인 장바구니에 담기 등 편의를 위하되 <u>지워지거나 유출되도 큰 일은 없을 정보들(가벼운 정보들)을 저장</u>
- 쿠키는 **만료일자**를 지정하게 되어 있어 언젠가 제거된다. 만료일자로 지정된 날짜에 쿠키는 제거되는 것이다.
- 클라이언트에 저장되고 클라이언트의 메모리를 사용하기 때문에 **서버 자원 사용하지 않음**
- 세선 쿠키와 지속 쿠키
  - 만료 일자를 지정하지 않으면 항상 유지하라는 것으로 판단하고 지속 쿠키에 저장되고, 만료 일자를 지정하면 세션 쿠키로 저장된다.
  - 세션 쿠키는 브라우저 메모리에 저장되므로 브라우저가 종료되면 쿠키는 사라지고 지속 쿠키는 파일로 저장되므로 브라우저가 종료되어도 쿠키는 남아있게 된다.
  - 참고로 세션 쿠키의 값은 보안상 꽤나 안전한 브라우저(ex. 구글 크롬)의 메모리에 저장되기 때문에 보안에 유리하지만 파일로 저장되는 지속 쿠키의 경우 비교적으로 보안에 취약하다.

<br>

## (3) Session

- 쿠키의 트래픽 문제와 쿠키를 함부로 변경할 수 있는 보안적 이슈를 해결하기 위해 등장
- 쿠키와 달리 <b>서버</b>에 클라이언트의 상태 정보를 저장하는 기술로 논리적인 연결임
- 웹 서버에 클라이언트에 대한 정보를 저장하고 클라이언트에게는 클라이언트를 구분할 수 있는 ID를 부여하는데 이것을 `session id`라 한다.
  - 클라이언트가 서버에 접속하면 서버가 <u>특정 session id를 발급하고 클라이언트는 session id를 쿠키를 사용해 저장.</u> 클라이언트가 서버에 다시 접속하면 해당 쿠키(session id가 담긴)를 이용해 <u>서버에 session id를 전달하여 인증을 받게 된다.</u>
- 결과적으로 세션을 통해 <b>클라이언트의 정보는 서버에 두고, 세션 아이디를 이용해서 인증받고 정보를 이용하는 방식</b>이다.
- 클라이언트가 로그아웃하거나, 설정 시간동안 반응이 없으면 무효화 되기 때문에 정확한 만료 시점 알 수 없음
- 세션이 여러모로 좋은 점이 많은데도 불구하고 쿠키를 사용하는 이유
  - 세션은 서버에 데이터를 저장하면서 서버의 자원을 사용하기 때문에 서버 자원에 한계가 있고 서버 메모리를 사용하다보면 속도 저하도 올 수 있기 때문이다.

<br>

## :mag: Cookie와 Session 차이점 정리

| 항목                 | Cookie                                                       | Session                                                      |
| -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| <b>저장 위치</b>     | 클라이언트의 로컬                                            | 서버                                                         |
| 저장 형식            | Text 형태                                                    | Object 형태                                                  |
| 만료시점             | 쿠키 저장시 설정함<br>(별도 설정이 없다면 브라우저 종료할 때가 만료시점) | 정확한 시점 모름                                             |
| 용량제한             | 한 도메인 당 20개, 한 쿠키당 4KB                             | 제한없음                                                     |
| <b>보안</b>          | 보안에 비교적 취약<br>(클라이언트 로컬에 저장)               | 비교적 안전<br>(클라이언트 정보 자체는 서버에 저장)          |
| 속도                 | 비교적 빠름<br>(쿠키에 정보가 있으므로 서버에 요청시 헤더를 바로 참조) | 비교적 느림<br>(제공받은 세선 아이디를 이용해서 서버에서 다시 데이터를 참조) |
| <b>라이프 사이클</b> | 지속 쿠키 경우 브라우저 종료해도 저장되어 있을 수 있음       | 서버에서 만료 일자를 정해서 지울 수 있고<br>세션 쿠키에 세션 아이디를 지정한 경우<br>브라우저 종료시 세션아이디가 날라갈 수 있음 |

<br>

---

:page_facing_up: <b>Reference</b>

- https://jeong-pro.tistory.com/80

---

