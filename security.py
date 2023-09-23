import cx_Oracle as cx
con = cx.connect("c##kmg", "Rla3241265", "192.168.137.1:1521/orcl", encoding="UTF-8")
cursor = con.cursor()