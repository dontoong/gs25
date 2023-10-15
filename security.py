import cx_Oracle as cx
con = cx.connect("아이디", "비밀번호", "ip주소", encoding="UTF-8")
cursor = con.cursor()
