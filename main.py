import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

win=tk.Tk()
win.geometry("1350x700+0+0")
win.title("Student Management System")

title_label=tk.Label(win,text="Student Management System",font=("Arial",30,"bold"),border=12,relief=tk.GROOVE,bg="lightgrey")
title_label.pack(side=tk.TOP,fill=tk.X)

detail_fram=tk.LabelFrame(win,text="Enter Details",font=("Arial",20),bd=12,relief=tk.GROOVE)
detail_fram.place(x=20,y=90,width=420,height=575)


data_fram=tk.Frame(win,bd=12,bg="lightgrey",relief=tk.GROOVE)
data_fram.place(x=475,y=90,width=810,height=575)


rollno=tk.StringVar()
name=tk.StringVar()
class_var=tk.StringVar()
section=tk.StringVar()
contact=tk.StringVar()
fathersnm=tk.StringVar()
address=tk.StringVar()
gender=tk.StringVar()
dob=tk.StringVar()


search_by=tk.StringVar()

rollno_lbl=tk.Label(detail_fram,text="Roll No",font=('Arial',15),bg="lightgrey")
rollno_lbl.grid(row=0,column=0,padx=2,pady=2)

rollno_ent=tk.Entry(detail_fram,bd=7,font=('Arial',15),textvariable=rollno)
rollno_ent.grid(row=0,column=1,padx=2,pady=2)

name_lbl=tk.Label(detail_fram,text="Name",font=('Arial',15),bg="lightgrey")
name_lbl.grid(row=1,column=0,padx=2,pady=2)

name_ent=tk.Entry(detail_fram,bd=7,font=('Arial',15),textvariable=name)
name_ent.grid(row=1,column=1,padx=2,pady=2)

class_lbl=tk.Label(detail_fram,text="Class",font=('Arial',15),bg="lightgrey")
class_lbl.grid(row=2,column=0,padx=2,pady=2)

class_ent=tk.Entry(detail_fram,bd=7,font=('Arial',15),textvariable=class_var)
class_ent.grid(row=2,column=1,padx=2,pady=2)


section_lbl=tk.Label(detail_fram,text="Section",font=('Arial',15),bg="lightgrey")
section_lbl.grid(row=3,column=0,padx=2,pady=2)

section_ent=tk.Entry(detail_fram,bd=7,font=('Arial',15),textvariable=section)
section_ent.grid(row=3,column=1,padx=2,pady=2)

contact_lbl=tk.Label(detail_fram,text="Contact",font=('Arial',15),bg="lightgrey")
contact_lbl.grid(row=4,column=0,padx=2,pady=2)

contact_ent=tk.Entry(detail_fram,bd=7,font=('Arial',15),textvariable=contact)
contact_ent.grid(row=4,column=1,padx=2,pady=2)

fathersnm_lbl=tk.Label(detail_fram,text="Father's Name",font=('Arial',15),bg="lightgrey")
fathersnm_lbl.grid(row=5,column=0,padx=2,pady=2)

fathersnm_ent=tk.Entry(detail_fram,bd=7,font=('Arial',15),textvariable=fathersnm)
fathersnm_ent.grid(row=5,column=1,padx=2,pady=2)

address_lbl=tk.Label(detail_fram,text="Address",font=('Arial',15),bg="lightgrey")
address_lbl.grid(row=6,column=0,padx=2,pady=2)

address_ent=tk.Entry(detail_fram,bd=7,font=('Arial',15),textvariable=address)
address_ent.grid(row=6,column=1,padx=2,pady=2)

gender_lbl=tk.Label(detail_fram,text="Gender",font=('Arial',15),bg="lightgrey")
gender_lbl.grid(row=7,column=0,padx=2,pady=2)

gender_ent=ttk.Combobox(detail_fram,font=('Arial',15),state="readonly",textvariable=gender)
gender_ent['values']=("Male","Female")
gender_ent.grid(row=7,column=1,padx=2,pady=2)

dob_lbl=tk.Label(detail_fram,text="D.O.B",font=('Arial',15),bg="lightgrey")
dob_lbl.grid(row=8,column=0,padx=2,pady=2)

dob_ent=tk.Entry(detail_fram,bd=7,font=('Arial',15),textvariable=dob)
dob_ent.grid(row=8,column=1,padx=2,pady=2)


def fetch_data():
            conn=pymysql.connect(host="localhost",user="root",passwd="",database="sms1")
            curr=conn.cursor()
            curr.execute("SELECT * FROM data")
            rows=curr.fetchall()

            if len(rows)!=0:
                    student_table.delete(*student_table.get_children())
                    for row in rows:
                            student_table.insert('',tk.END,values=row)
                            conn.commit()
            conn.close()
                    

def add_func():
        if rollno.get() == "" or name.get() == "" or class_var.get() == "":
                messagebox.showerror("Error!","Please fill all the fields!")
        else:
            conn=pymysql.connect(host="localhost",user="root",passwd="",database="sms1")
            curr=conn.cursor()
            curr.execute("INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(rollno.get(),name.get(),class_var.get(),section.get(),contact.get(),fathersnm.get(),address.get(),gender.get(),dob.get()))
            conn.commit()
            conn.close()
        messagebox.showinfo("Success", "Record added successfully!")
          

        fetch_data()
       


def get_cursor(event):
        cursor_row=student_table.focus()
        content=student_table.item(cursor_row)
        row=content['values']
        rollno.set(row[0])
        name.set(row[1])
        class_var.set(row[2])
        section.set(row[3])
        contact.set(row[4])
        fathersnm.set(row[5])
        address.set(row[6])
        gender.set(row[7])
        dob.set(row[8])


def clear():
        rollno.set("")
        name.set("")
        class_var.set("")
        section.set("")
        contact.set("")
        fathersnm.set("")
        address.set("")
        gender.set("")
        dob.set("")
        messagebox.showinfo("Success", "Form cleared successfully!")


def update_func():
    conn = pymysql.connect(host="localhost", user="root", passwd="", database="sms1")
    curr = conn.cursor()
    curr.execute(
    "UPDATE data SET name=%s, `class`=%s, section=%s, contact=%s, fathersnm=%s, address=%s, gender=%s, dob=%s WHERE rollno=%s",
    (name.get(), class_var.get(), section.get(), contact.get(), fathersnm.get(), address.get(), gender.get(), dob.get(), rollno.get()))

    conn.commit()
    fetch_data()
    conn.close()
    messagebox.showinfo("Success", "Record updated successfully!")
    clear()
    

def delete_func():
    if rollno.get() == "":
        messagebox.showerror("Error!", "Please select a record to delete.")
    else:
        conn = pymysql.connect(host="localhost", user="root", passwd="", database="sms1")
        curr = conn.cursor()
        
      
        curr.execute("DELETE FROM data WHERE rollno=%s", (rollno.get(),))
        
        conn.commit()
        conn.close()
        
        fetch_data() 
        clear() 
        messagebox.showinfo("Success", "Record deleted successfully!")  
    




btn_fram=tk.Frame(detail_fram,bg="lightgrey",bd=10,relief=tk.GROOVE)
btn_fram.place(x=22,y=390,width=340,height=120)

add_btn=tk.Button(btn_fram,bg="lightgrey",text="Add",bd=7,font=('Arial',13),width=15,command=add_func)
add_btn.grid(row=0,column=0,padx=2,pady=2)

update_btn=tk.Button(btn_fram,bg="lightgrey",text="Update",bd=7,font=('Arial',13),width=15,command=update_func)
update_btn.grid(row=0,column=1,padx=3,pady=2)

delete_btn=tk.Button(btn_fram,bg="lightgrey",text="Delete",bd=7,font=('Arial',13),width=15,command=delete_func)
delete_btn.grid(row=1,column=0,padx=3,pady=2)

clear_btn=tk.Button(btn_fram,bg="lightgrey",text="Clear",bd=7,font=('Arial',13),width=15,command=clear)
clear_btn.grid(row=1,column=1,padx=3,pady=2)


search_fram=tk.Frame(data_fram,bg="lightgrey",bd=10,relief=tk.GROOVE)
search_fram.pack(side=tk.TOP,fill=tk.X)

search_lbl=tk.Label(search_fram,text="Search",bg="lightgrey",font=('Arial',14))
search_lbl.grid(row=0,column=0,padx=2,pady=2)

search_in=ttk.Combobox(search_fram,font=('Arial',14),state="readonly",textvariable=search_by)
search_in['values']=("Name","Roll No","Contact","Father's Name","Class","Section","D.O.B")
search_in.grid(row=0,column=1,padx=12,pady=2)

search_btn=tk.Button(search_fram,text="Search",font=("Arial",13),bd=9,width=14,bg="lightgrey")
search_btn.grid(row=0,column=2,padx=12,pady=2)

showall_btn=tk.Button(search_fram,text="Show All",font=("Arial",13),bd=9,width=14,bg="lightgrey")
showall_btn.grid(row=0,column=3,padx=12,pady=2)


main_fram=tk.Frame(data_fram,bg="lightgrey",bd=11,relief=tk.GROOVE)
main_fram.pack(fill=tk.BOTH,expand=True)

y_scroll=tk.Scrollbar(data_fram,orient=tk.VERTICAL)
x_scroll=tk.Scrollbar(data_fram,orient=tk.HORIZONTAL)

student_table=ttk.Treeview(main_fram,columns=("Roll No","Name","Class","Section","Contact","Father's Name","Address","Gender","D.O.B"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)


y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)


student_table.heading("Roll No",text="Roll No")
student_table.heading("Name",text="Name")
student_table.heading("Class",text="Class")
student_table.heading("Section",text="Section")
student_table.heading("Contact",text="Contact")
student_table.heading("Father's Name",text="Father's Name")
student_table.heading("Address",text="Address")
student_table.heading("D.O.B",text="D.O.B")
student_table.heading("Gender",text="Gender")

student_table['show']='headings'

student_table.column("Roll No",width=100)
student_table.column("Name",width=100)
student_table.column("Class",width=100)
student_table.column("Section",width=100)
student_table.column("Contact",width=100)
student_table.column("Father's Name",width=100)
student_table.column("Address",width=150)
student_table.column("D.O.B",width=100)
student_table.column("Gender",width=100)

student_table.pack(fill=tk.BOTH,expand=True)

fetch_data()

student_table.bind("<ButtonRelease-1>",get_cursor)

win.mainloop()
