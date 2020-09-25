# 01. HTTP & HTTPS

<br>

## 1. HTTP

- 웹 상에서 클라이언트와 서버 간 데이터를 주고 받기 위한 프로토콜이다. 클라이언트가 HTTP 프로토콜을 이용해 서버에 정보를 요청하면 서버는 이 요청에 대한 응답으로 정보를 전달한다.
- HTTP의 문제점
  - HTTP는 평문 통신이기 때문에 도청이 가능하다.
  - 통신 상대를 확인하지 않기 때문에 위장이 가능하다.
  - 완전성을 증명할 수 없기 때문에 변조가 가능하다.
- 위 세 가지는 다른 암호화하지 않은 프로토콜에도 공통되는 문제점들이다.

### (1) 도청 문제점 해결

- TCP/IP 구조의 통신은 전부 통신 경로 상에서 엿볼 수 있다.  패킷을 수집하는 것만으로도 도청할 수 있다. 평문으로 통신할 경우 메시지의 의미를 그대로 파악할 수 있으므로 <b>암호화하여 통신해야 한다.</b>
- 해결 방법
  - 통신 자체를 <b>암호화 `SSL` 또는 `TLS` 라는 다른 프로토콜을 조합해서 HTTP의 통신 내용을 암호화</b>할 수 있다. 이 때 SSL을 조합한 HTTP를 `HTTPS` 또는 `HTTP over SSL` 이라고 부른다.
  - 콘텐츠를 암호화 말 그대로 HTTP를 그대로 사용해서 운반하는 내용인 HTTP 메시지에 포함되는 콘텐츠만 암호화하는 것이다. <b>암호화해서 전송하면 받은 측에서는 그 암호를 해독하여 출력하는 처리가 필요하다.</b>

<br>

### (2) 위장 문제점 해결

- HTTP에 의한 통신에는 <b>상대가 누구인지 확인하는 처리가 없으므로 누구든지 request를 보낼 수 있다.</b> IP 주소나 포트 등에서 그 웹 서버에 액세스 제한이 없는 경우 request가 오면 <b>상대가 누구든지 response를 반환</b>한다. 이러한 특징은 아래와 같은 문제점을 유발한다.
  - request를 보낸 곳의 웹 서버가 원래 의도한 response를 보내야 하는 웹 서버인지를 확인할 수 없다.
  - response를 반환하는 곳의 클라이언트가 원래 의도한 request를 보낸 클라이언트인지 확인할 수 없다.
  - 통신하고 있는 상대가 접근이 허가된 상대인지를 확인할 수 없다.
  - 어디에서, 누가 request를 보냈는지 확인할 수 없다.
  - 의미없는 request도 수신해기 때문에 DoS 공격을 방지할 수 없다.
- 해결 방법
  - `SSL`을 통해서 상대가 누구인지 확인할 수 있다. `SSL`은 상대를 확인하는 수단으로 <b>증명서</b>를 제공하고 있다.
  - 증명서는 신뢰할 수 있는 <b>제 3 자 기관에 의해</b> 발행되므로 서버나 클라이언트가 실제로 존재하는 사실을 증명한다.
  - 이 증명서를 이용함으로써 통신 상대가 내가 통신하고자 하는 서버임을 나타내고 사용자는 개인 정보 누설 등의 위험성이 줄어들게 된다.
  - 추가로 클라이언트는 이 증명서로 본인 확인을 하고 웹 사이트 인증에서도 이용할 수 있다.

<br>

### (3) 변조 문제점 해결

- 위에서 살펴본 HTTP의 문제점에서 `완전성`이라는 용어가 등장했는데 이는 <b>정보의 정확성</b>을 의미한다.
- 서버 또는 클라이언트에서 수신한 내용이 송신측에서 보낸 내용과 일치한다라는 것을 보장할 수 없는 것이다.
- request나 response가 보내진 후 상대가 수신하는 사이에 누군가에 의해 변조되더라도 이 사실을 알 수 없다.
- 이와 같이 공격자가 도중에 request나 response를 빼앗아 변조하는 공격을 중간자 공격(Man-in-the-Middle) 이라고 부른다.
- 해결 방법
  - `MDS`, `SHA-1` 등의 해시 값을 확인하는 방법과 파일의 디지털 서명을 확인하는 방법이 존재하지만 확실히 확인할 수 있는 것은 아니기에 이 보다 더 확실하게 방지하려면 `HTTPS`를 사용해야 한다.
  - `SSL` 에는 인증이나 암호화, 그리고 다이제스트 기능을 제공하고 있기 때문이다.

---

:heavy_check_mark: <b>SSL 의 메시지 다이제스트</b>

- SSL에서는 데이터를 보호하기 위해 `암호화`, `메시지 다이제스트`, `디지털 증명서` 방법을 이용하는데 이 중 `메시지 다이제스트`란 데이터로부터 고정 길이 데이터를 꺼내는 계산을 의미한다.
- 메시지 다이제스트는 전송 중에 누가 변조하지 않았음을 보장하고 정보가 잘 전송되었음 보장하기 위해 사용된다.
- 기본적인 인증은 암호화되지 않은 base64 인코딩을 사용하는 반면 다이제스트 인증은 사용자 이름, 암호, 서버 제공 nonce 값, HTTP 방법 및 요청 된 URI에 해시 함수를 적용하여 자격 증명을 암호화된 형태로 전달한다.
- 메시지 다이제스트는 고정된 크기의 메시지로, 해쉬함수를 이용해서 생성되는데 해쉬는 많은 양의 메시지를 128비트나 160비트의 다이제스트로 압축한다.
- 서명된 메시지를 보내기 위해 메시지 작성자의 컴퓨터는 해당 메시지에 대한 다이제스트를 생성하고 다이제스트와 작성자의 개인 키로 전자 서명을 계산하여, 메시지와 전자 서명을 모두 보낸다. 수신인은 작성자의 공개키를 사용하여 수신된 메시지에 대한 다이제스트를 생성하고, 수신된 전자 서명을 사용하여 작성자를 확인한다.
- 해쉬함수가 안전성이 보장된다는 가정하에서, 메시지 다이제스트 서명은 메시지 자체에 서명을 하는 것과 동일한 보안 서비스를 제공하게 된다.

---

<br>

## 2. HTTPS

> `HTTP` + `암호화` + `인증` + `완전성 보호` => `HTTPS`

<br>

### (1) HTTPS 특징

- `HTTPS`는 `SSL` 의 껍질을 덮어쓴 `HTTP`라고 할 수 있다. 즉, `HTTPS`는 새로운 어플리케이션 계층의 프로토콜이 아니라는 것이다.
- HTTP 통신하는 소켓 부분을 `SSL` 또는 `TLS` 라는 프로토콜로 대체하는 것 뿐이다.
- HTTP는 원래 TCP와 직접 통신했지만, HTTPS에서 HTTP는 SSL과 통신하고 <b>SSL이 TCP와 통신</b>하게 된다. SSL을 사용한 HTTPS는 암호화와 증명서, 안전성 보호를 이용할 수 있게 된다. 즉, 하나의 레이어를 더 둔 것이다.
- HTTPS 의 SSL 에서는 공통키 암호화 방식과 공개키 암호화 방식을 혼합한 하이브리드 암호 시스템을 사용한다. 공통키를 공개키 암호화 방식으로 교환한 다음에 다음부터의 통신은 공통키 암호를 사용하는 방식이다. 암호화 방식은 추후 자세히 살펴보자.

<br>

### (2) HTTPS에서 제공하는 기능

- <b>기밀성</b>
  - 인터넷과 같은 공공 매체에서 두 참여자 간의 통신을 보호한다.
  - <b>암호화</b>과정을 통해 <b>평문</b> 정보 형식을 뒤죽박죽 된 읽을 수 없는 정보 형식인 <b>암호문</b>으로 변환한다.
- <b>무결성</b>
  - 변조되지 않은 정보를 목적지에 안전하게 전송해준다.
  - 전체 정보가 잘 도착했는지, 전송 중에 누가 변조하지 않고 잘 전송되었는지
- <b>인증</b>
  - 웹사이트의 진위 여부를 확인할 수 있다.
  - 예를 들어 와이파이 액세스 포인트를 운영하는 사람이 가짜 웹사이트를 브라우저에 보낼 수도 있다.
  - HTTPS는 `example.com`이라는 웹사이트가 실제로 `example.com`인지 확인한다. 일부 인증서는 `yourbank.com`이 YourBank.Inc라는 걸 알리기 위해 해당 웹사이트의 법적 신원을 검사하기도 한다.
  - 공개 키 인프라의 실제 애플리케이션이 갖는 문제는 양쪽 당사자가 (물리적으로 떨어져 있는) 상대편이 실제로 누구인지 알 방법이 없다는 것이다.
  - 그래서 상대편의 신원을 보증하기 위해 상호 신뢰할 수 있는 제3자, 즉 인증 기관(CA)이 필수다.
  - 인증 기관은 `example.com`이라는 도메인 이름(고유한 식별자)이 공개 키 `XXX`와 연결되어 있음을 기술한 인증서를 발행한다. 

<br>

### (3) HTTPS의 보안 이외에 또 다른 장점

- 검색 엔진 최적화(SEO)
  - 지난 2014년 구글에서 HTTP를 HTTPS로 바꾸라고 권고했다.
  - 구글에서는 HTTPS 웹사이트에 검색 결과 순위에 가산점을 더 주겠다고 발표했다.
  - 왜냐하면 웹사이트를 검색하는 사용자들은 결국에는 가장 안전하다고 생각하는 사이트를 더 많이 방문하기 때문에 비교적 안전하다고 판단되는 사이트를 검색 결과의 상위 순위로 보여준다.
- 가속화된 모바일 페이지(AMP, Accelerated Mobile Page) 제작
  - AMP : 구글이 만든 모바일 기기에서 훨씬 빠르게 콘텐츠를 로딩하기 위해 제작한 방법으로 HTML에서 불필요한 부분을 없앤 것
  - 구글의 검색 결과 페이지를 보면 스마트폰과 태블릿의 사용자들이 모바일에서 사용하기 편하도록 AMP 컨텐츠들이 두드러져 있는 것을 볼 수 있다.
- 모바일 친화적인 웹사이트를 만드는 것과 모바일 검색순위 및 SEO를 증가시키는 것이 중요해지고 있기 때문에 HTTPS는 이제 필수적인 요소가 되었다.

<br>

---

:book: <b>Reference</b>

- [https://github.com/WooVictory/Ready-For-Tech-Interview/blob/master/Network/HTTP%2C%20HTTPS.md](https://github.com/WooVictory/Ready-For-Tech-Interview/blob/master/Network/HTTP%2C HTTPS.md)
- https://github.com/JaeYeopHan/Interview_Question_for_Beginner/tree/master/Network
- [https://webactually.com/2018/11/http%EC%97%90%EC%84%9C-https%EB%A1%9C-%EC%A0%84%ED%99%98%ED%95%98%EA%B8%B0-%EC%9C%84%ED%95%9C-%EC%99%84%EB%B2%BD-%EA%B0%80%EC%9D%B4%EB%93%9C/](https://webactually.com/2018/11/http에서-https로-전환하기-위한-완벽-가이드/)
- http://ko.security.wikidok.net/wp-d/575aa262d16e73173de7a3ed/View

- [https://www.it-swarm.dev/ko/http/%EB%8B%A4%EC%9D%B4%EC%A0%9C%EC%8A%A4%ED%8A%B8%EC%99%80-%EA%B8%B0%EB%B3%B8-%EC%9D%B8%EC%A6%9D%EC%9D%98-%EC%B0%A8%EC%9D%B4%EC%A0%90%EC%9D%80-%EB%AC%B4%EC%97%87%EC%9E%85%EB%8B%88%EA%B9%8C/942207010/](https://www.it-swarm.dev/ko/http/다이제스트와-기본-인증의-차이점은-무엇입니까/942207010/)
- [http://blog.wishket.com/http-vs-https-%EC%B0%A8%EC%9D%B4-%EC%95%8C%EB%A9%B4-%EC%82%AC%EC%9D%B4%ED%8A%B8%EC%9D%98-%EB%A0%88%EB%B2%A8%EC%9D%B4-%EB%B3%B4%EC%9D%B8%EB%8B%A4/](http://blog.wishket.com/http-vs-https-차이-알면-사이트의-레벨이-보인다/)