Scheme

웹 서버와 어떤 프로토콜로 통신할지 나타냅니다.

Host

Authority의 일부로, 접속할 웹 서버의 주소에 대한 정보를 가지고 있습니다.

Port

Authority의 일부로, 접속할 웹 서버의 포트에 대한 정보를 가지고 있습니다.

Path

접근할 웹 서버의 리소스 경로로 '/'로 구분됩니다.

Query

웹 서버에 전달하는 파라미터이며 URL에서 '?' 뒤에 위치합니다.

Fragment

메인 리소스에 존재하는 서브 리소스를 접근할 때 이를 식별하기 위한 정보를 담고 있습니다. '#' 문자 뒤에 위치합니다.

foo://example.com:8042/over/there?name=ferret#nose
순서대로 Scheme, Authority, Path, Query, Fragment

URL 구성 요소 중 Host는 웹 브라우저가 접속할 웹 서버의 주소를 나타냅니다. Host는 Domain Name, 
IP Address의 값을 가질 수 있습니다. IP Address는 네트워크상에서 통신이 이루어질 때 장치를 식별하기 위해 사용되는 주소입니다. 
불규칙한 숫자로 이루어진 IP Address는 사람이 외우기 어려우므로, 일반적으로는 도메인의 특성을 담은 이름을 정의하여 IP 대신 사용합니다.

Domain Name을 Host 값으로 이용할 때, 브라우저는 Domain Name Server(DNS)에 Domain Name을 질의하고, 
DNS가 응답한 IP Address를 사용합니다. 예를 들어, 웹 브라우저에서 http://example.com에 접속할 경우, 
DNS에 질의해 얻은 example.com의 IP와 통신합니다.

Domain Name에 대한 정보는 MacOS/Linux/Windows에서 nslookup 명령어를 사용해 확인할 수 있습니다.

웹 브라우저(Web Browser): 웹 브라우저는 HTTP/S로 이용자와 웹 서버의 통신을 중개하며, 서버로부터 전달받은 다양한 웹 리소스들을 가공해 이용자에게 효과적으로 전달합니다. 이용자가 다양한 프로토콜들을 알지 못해도 쉽게 웹을 사용할 수 있도록 도와줍니다.

URL(Uniform Resource Locator): URL은 리소스의 위치를 나타내는 문자열로, 브라우저는 이를 사용하여 서버에 특정 리소스를 요청할 
수 있습니다.

DNS(Domain Name Server): Host의 도메인 이름을 IP로 변환하거나 IP를 도메인 이름으로 변환합니다.

웹 렌더링(Web Rendering): 서버로부터 받은 리소스를 이용자에게 시각화하는 것을 말합니다.