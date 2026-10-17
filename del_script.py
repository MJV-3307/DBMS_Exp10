from tkinter import *
import mysql.connector
conn = mysql.connector.connect(user='root', password='Mysql@123',host='localhost', database='Mahira')
cursor=conn.cursor()
class del_script:
    def __init__(self,root):
        self.f=Frame(root,height=500,width=500)
        self.f.pack()
        self.l1 = Label(text='Student ID to delete: ')
        self.e1 = Entry(self.f, width=18)
        self.b1=Button(self.f,text="Delete Row",command=self.deletion)
        self.l1.place(x=50, y=30)
        self.e1.place(x=200, y=30)
        self.b1.place(x=200,y=150)
    def deletion(self):
        str1 = int(self.e1.get())
        sql = "delete from student where s_id='%d'" % (str1)
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
        print(f"Data for s_id {str1} deleted.")
        conn.close()
        self.upd_script()
    def upd_script(self):
        root.destroy()
        import upd_script
root=Tk()
root.title('Deleting A Row From Table Student Using Tkinter')
obj=del_script(root)
root.mainloop()