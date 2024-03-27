import flask

@app.route('/') # / 페이지 라우팅 
def index():
    username = request.cookies.get('username', None) # 이용자가 전송한 쿠키의 username 입력값을 가져옴
    if username: # username 입력값이 존재하는 경우
        return render_template('index.html', text=f'Hello {username}, {"flag is " + FLAG if username == "admin" else "you are not admin"}') # "admin"인 경우 FLAG 출력, 아닌 경우 "you are not admin" 출력
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST']) # login 페이지 라우팅, GET/POST 메소드로 접근 가능
def login():
    if request.method == 'GET': # GET 메소드로 요청 시
        return render_template('login.html') # login.html 페이지 출력
    elif request.method == 'POST': # POST 메소드로 요청 시
        username = request.form.get('username') # 이용자가 전송한 username 입력값을 가져옴
        password = request.form.get('password') # 이용자가 전송한 password 입력값을 가져옴
        try:
            pw = users[username] # users 변수에서 이용자가 전송한 username이 존재하는지 확인
        except: 
            return '<script>alert("not found user");history.go(-1);</script>' # 존재하지 않는 username인 경우 경고 출력
        if pw == password: # password 체크
            resp = make_response(redirect(url_for('index')) ) # index 페이지로 이동하는 응답 생성
            resp.set_cookie('username', username) # username 쿠키 설정
            return resp 
        return '<script>alert("wrong password");history.go(-1);</script>' # password가 동일하지 않은 경우
try:
    FLAG = open('./flag.txt', 'r').read() # flag.txt 파일로부터 FLAG 데이터를 가져옴.
except:
    FLAG = '[**FLAG**]'
users = {
    'guest': 'guest',
    'admin': FLAG # FLAG 데이터를 패스워드로 선언
}