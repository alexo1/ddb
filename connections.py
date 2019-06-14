import pyodbc


def query_sqlite(query,path):
    results=[]
    con = pyodbc.connect("DRIVER={SQLITE3};Database="+path)
    cursor=con.cursor()
    cursor.execute(query)
    while True:
        row = cursor.fetchone()
        if not row:
            break
        results.append(row)
    return results

def query_mysql(query):
    con_string = "DRIVER={MySQL};SERVER=127.0.0.1;DATABASE=ecommerce;USER=admin;PASSWORD=pass;OPTION=3;"
    con = pyodbc.connect(con_string)
    cursor=con.cursor()
    cursor.execute(query)
    
    results=cursor.fetchall()
    
    return results
def query_postgres(query):
    pass

print("Kisumu campus running sqlite3 on windows vm with ip 10.0.0.2\n")
sql="SELECT * FROM students_student;"
path="kisumu_campus/db.sqlite3"
all_kis_students=query_sqlite(query=sql,path=path)
print(all_kis_students)

print("\n\nMombasa campus running mysql on linux vm with ip 127.0.0.1\n")
sql="select * from carts_cart;"
all_mombasa_carts=query_mysql(query=sql)
print(all_mombasa_carts)

