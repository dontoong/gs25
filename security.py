import cx_Oracle as cx
con = cx.connect("your_id", "your_password", "your_ip", encoding="UTF-8")
cursor = con.cursor()
