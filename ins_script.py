# create table student (
# s_id int primary key,
# s_name varchar(50) not null,
# s_email varchar(25),
# s_contact int,
# s_address varchar(25),
# s_did int,
# s_cid int
# );
from tkinter import *
import mysql.connector
conn = mysql.connector.connect(user='root', password='Mysql@123',host='localhost', database='Mahira')
cursor=conn.cursor()
class First:
    def __init__(self,root):
        self.f=Frame(root,height=500,width=500)
        self.f.pack()
        self.l1=Label(text='Student ID: ')
        self.l2=Label(text='Student Name: ')
        self.l3=Label(text='Student Email: ')
        self.l4=Label(text='Student Contact: ')
        self.l5 = Label(text='Student Address: ')
        self.l6 = Label(text='Student Department ID: ')
        self.l7 = Label(text='Student College ID: ')
        self.e1=Entry(self.f,width=18)
        self.e2=Entry(self.f,width=18)
        self.e3=Entry(self.f,width=18)
        self.e4=Entry(self.f,width=18)
        self.e5 = Entry(self.f, width=18)
        self.e6 = Entry(self.f, width=18)
        self.e7 = Entry(self.f, width=18)
        self.b1=Button(self.f,text='Submit',command=self.insert)
        self.l1.place(x=50,y=30)
        self.e1.place(x=200,y=30)
        self.l2.place(x=50,y=60)
        self.e2.place(x=200,y=60)
        self.l3.place(x=50,y=90)
        self.e3.place(x=200,y=90)
        self.l4.place(x=50,y=120)
        self.e4.place(x=200,y=120)
        self.l5.place(x=50, y=150)
        self.e5.place(x=200, y=150)
        self.l6.place(x=50, y=180)
        self.e6.place(x=200, y=180)
        self.l7.place(x=50, y=210)
        self.e7.place(x=200, y=210)
        self.b1.place(x=200, y=240)
    def insert(self):
        str1 = int(self.e1.get())
        str2 = self.e2.get()
        str3=self.e3.get()
        str4=int(self.e4.get())
        str5 = self.e5.get()
        str6 = int(self.e6.get())
        str7 = int(self.e7.get())
        sql="insert into student(s_id,s_name,s_email, s_contact,s_address,s_did,s_cid)values('%d','%s','%s','%d','%s','%d','%d')"%(str1,str2,str3,str4,str5,str6,str7)
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
        print(f"Data for s_id {str1} inserted.")
        conn.close()
        self.del_script()
    def del_script(self):
        root.destroy()
        import del_script
root=Tk()
root.title('Inserting A Row In Table Student Using Tkinter')
obj=First(root)
root.mainloop()