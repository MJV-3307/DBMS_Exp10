from tkinter import *
import mysql.connector
conn = mysql.connector.connect(user='root', password='Mysql@123',host='localhost', database='Mahira')
cursor=conn.cursor()
class upd_script:
    def __init__(self,root):
        self.f=Frame(root,height=500,width=500)
        self.f.pack()
        self.l1 = Label(text='Student ID to update: ')
        self.e1 = Entry(self.f, width=18)
        self.l2 = Label(text='New Student Name: ')
        self.e2 = Entry(self.f, width=18)
        self.b1=Button(self.f,text="Update Row",command=self.updation)
        self.l1.place(x=50, y=30)
        self.e1.place(x=200, y=30)
        self.l2.place(x=50, y=60)
        self.e2.place(x=200, y=60)
        self.b1.place(x=200,y=90)
    def updation(self):
        str1 = int(self.e1.get())
        str2 = self.e2.get()
        sql = "update student set s_name='%s' where s_id='%d'" % (str2,str1)
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
        print(f"Data updated for s_id {str1}.")
        conn.close()
        self.sel_script()
    def sel_script(self):
        root.destroy()
        import sel_script
root=Tk()
root.title('Updating A Row In Table Student Using Tkinter')
obj=upd_script(root)
root.mainloop()