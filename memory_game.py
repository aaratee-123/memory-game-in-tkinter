
from tkinter import *
import random 
#from tkinter import PhotoImage
#from tkinter import ttk
from tkinter import messagebox
#from PIL import ImageTk,Image
#from tkinter import ttk
root=Tk()
root.title("Memory_game")
#root.iconbitmap('c:/gui/codemy.ico')
#root.geometry("500*550")
# creat our matches
# square=PhotoImage(file="/home/aaratiee/Desktop/index.png")
# my_label=Label(image=square)
# my_label.pack()

matches=[1,1,2,2,3,3,4,4,5,5,6,6]
#matches=[]
# shuffle our matches
random.shuffle(matches)
# creat button frame
my_frame=Frame(root)
my_frame.pack(pady=10)
# define some variable
count=0
veiw_answer_list=[]
veiw_dict={}
def button_click(b,number):
    global count,veiw_answer_list,veiw_dict

    if b["text"]== ' ' and count <2:
        b["text"]=matches[number]

    # add number to veiw answer list
        veiw_answer_list.append(number)
    # add button and number to view dict
        veiw_dict[b]=matches[number]
    #increment a counter
        count=count+1
    # print(veiw_dict)
        if len(veiw_answer_list)==2:
            if matches[veiw_answer_list[0]]==matches[veiw_answer_list[1]]:
                my_label.config(text="MATCH!!!")
                for key in veiw_dict:
                    key["state"]="disabled"
                count=0
                veiw_answer_list=[]
                messagebox.showinfo("currect","currect")
                veiw_dict={}
                #messagebox.showinfo("currect","currect")
            else:
                my_label.config(text="OHH!!!")
                count=0
                veiw_answer_list=[]
            #pop up box
                messagebox.showinfo("incurrect","incurrect")
            
            #reset button
            for key in veiw_dict:
                key["text"]=" "
                veiw_dict={}


    
  
b0=Button(my_frame,text=' ',font=("Helvetica",20),height=5,width=6,command=lambda: button_click(b0,0),fg="yellow",bg="blue")
b1=Button(my_frame,text=' ',font=("Helvetica",20),height=5,width=6,command=lambda: button_click(b1,1),fg="yellow",bg="blue")
b2=Button(my_frame,text=' ',font=("Helvetica",20),height=5,width=6,command=lambda: button_click(b2,2),fg="yellow",bg="blue")
b3=Button(my_frame,text=' ',font=("Helvetica",20),height=5,width=6,command=lambda: button_click(b3,3),fg="yellow",bg="blue")
b4=Button(my_frame,text=' ',font=("Helvetica",20),height=5,width=6,command=lambda: button_click(b4,4),fg="yellow",bg="blue")
b5=Button(my_frame,text=' ',font=("Helvetica",20),height=5,width=6,command=lambda: button_click(b5,5),fg="yellow",bg="blue")
b6=Button(my_frame,text=' ',font=("Helvetica",20),height=5,width=6,command=lambda: button_click(b6,6),fg="yellow",bg="blue")
b7=Button(my_frame,text=' ',font=("Helvetica",20),height=5,width=6,command=lambda: button_click(b7,7),fg="yellow",bg="blue")
b8=Button(my_frame,text=' ',font=("Helvetica",20),height=5,width=6,command=lambda: button_click(b8,8),fg="yellow",bg="blue")
b9=Button(my_frame,text=' ',font=("Helvetica",20),height=5,width=6,command=lambda: button_click(b9,9),fg="yellow",bg="blue")
b10=Button(my_frame,text=' ',font=("Helvetica",20),height=5,width=6,command=lambda: button_click(b10,10),fg="yellow",bg="blue")
b11=Button(my_frame,text=' ',font=("Helvetica",20),height=5,width=6,command=lambda: button_click(b11,11),fg="yellow",bg="blue")
# grid our buttons
b0.grid(row=0,column=0)
b1.grid(row=0,column=1)
b2.grid(row=0,column=2)
b3.grid(row=0,column=3)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=1,column=3)

b8.grid(row=2,column=0)
b9.grid(row=2,column=1)
b10.grid(row=2,column=2)
b11.grid(row=2,column=3)

my_label=Label(root,text=" ")
my_label.pack(pady=20)

print(matches)
root.mainloop()


