from tkinter import*
from tkinter import ttk
from tkinter import messagebox
form = Tk()


fnt  = "None 30 bold"
bg   = "#eeaaff"
bgtxt= "#5099ff"
fg   = "#0000ff"
fgtxt= "#000000"
fw   = 700
fh   = 500 
x    = (form.winfo_screenwidth() - fw) / 2
y    = (form.winfo_screenheight() - fh) / 2
pad  = 10

form.geometry("%dx%d+%d+%d" % (fw ,fh ,x ,y))
form.title("Employees Data")
form.config( bg =bg)

Label(form,text="Employee Data" ,bg ="navy" ,fg = "lightblue",font =fnt).pack(pady =pad)
frame = Frame(form,bg =bg)
frame.pack(pady =pad)

Label(frame ,text="code :",bg =bg,fg =fg ,font =fnt).grid(row =0 ,column =0)
Label(frame,text="name :" ,bg=bg,fg =fg,font =fnt).grid(row =1,column =0)
Label(frame,text="adreess :", bg=bg ,fg =fg,font =fnt).grid(row=2 ,column =0)

svcode    =StringVar()
svname    =StringVar()
svaddress =StringVar()

txtcode   = Entry(frame,bg=bgtxt ,fg=fgtxt ,font=fnt,textvariable =svcode)
txtname   = Entry(frame,bg=bgtxt,fg=fgtxt ,font =fnt,textvariable =svname)
txtaddress= Entry(frame,bg=bgtxt ,fg =fgtxt ,font =fnt ,textvariable =svaddress)
txtcode.grid(row =0,column =1,pady =pad)
txtname.grid(row =1,column =1,pady =pad)
txtaddress.grid(row =2 ,column =1,pady =pad)
def create():
    if txtcode.get().strip() =="":
        messagebox.showinfo("code","Enter your code")
        txtcode.focus()
    elif txtname.get().strip() =="":
        messagebox.showinfo("name","Enter your name")
        txtname.focus()
    elif txtaddress.get().strip()=="":
        messagebox.showinfo("address","Enter you address")
        txtaddress.focus()
    else:
        filename = svcode.get()+"_"+svname.get()+".txt"
        f =open("filename" ,"w+")
        f.write("code : "+svcode.get()+"\n")
        f.write("name : "+svname.get()+"\n")
        f.write("adress :"+svaddress.get()+"\n")
        f.close
        messagebox.showinfo("file created","Employee file been added")
        

btnStyle =ttk.Style()
btnStyle.configure("TButton",font =fnt ,pady =pad ,padding =pad)
ttk.Button(form ,text ="Create Employee File",command =create).pack(pady =pad)
ttk.Button(form ,text ="EXIT").pack(pady =pad)
