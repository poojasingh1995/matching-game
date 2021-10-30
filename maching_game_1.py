from tkinter import*
import random
from tkinter import messagebox
import tkinter

root=Tk()
root.title("Memory Matching Game!")
# root.geometry("500*550")

global winner,matches
# set winner counter to 0
winner=0

# create our matches
matches=[1,1,2,2,3,3,4,4,5,5,6,6]
# matches[0]
# suffle our matches
random.shuffle(matches)
# create button frame
my_frame=Frame(root)
my_frame.pack(pady=10)
# define some variables
count=0
answer_list=[]
answer_dict={}

# reset the game
def reset():
    global matches,winner
    winner=0
    matches=[1,1,2,2,3,3,4,4,5,5,6,6]
    # shuffle our matches
    random.shuffle(matches)
    # reset label
    my_label.config(text=" ")
    # reset our title
    button_list=[box0,box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11]
    # loop the change button colors
    for button in button_list:
        button.config(text=" ",bg="SystemButtonFace",state="normal")
 
     
# create winner function
def win():
    my_label.config(text="congratulation! you won!!!")
    button_list=[box0,box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11]
    # loop the change button colors
    for button in button_list:
        button.config(bg="yellow")
 
# function for clicking button
def button_click(box,number):
    global count,answer_list,answer_dict,winner
    
    if box["text"]==" " and count<2:
        box["text"]=matches[number]
        # add number to answer list
        answer_list.append(number)
        # add button and number to answer dictionary
        answer_dict[box]=matches[number]
        # increment our counter
        count+=1
        print(answer_dict)
    
    # start to determine correct or not
    if len(answer_list)==2:
        if matches[answer_list[0]]==matches[answer_list[1]]:
            my_label.config(text="match!")
            for key in answer_dict:
                key["state"]="disabled"
            count=0
            answer_list=[]
            answer_dict={}
            # increment our winner counter
            winner+=1
            if winner ==6:
                win()
        else:
            my_label.config(text="opps!")
            count=0
            answer_list=[]
            # pop up box
            messagebox.showinfo("Incorrect!","Incorrect")
            # reset the button
            for key in answer_dict:
                key["text"]=" "
            answer_dict={}

# define our button
box0=Button(my_frame,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:button_click(box0,0),relief="groove")
box1=Button(my_frame,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:button_click(box1,1),relief="groove")
box2=Button(my_frame,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:button_click(box2,2),relief="groove")
box3=Button(my_frame,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:button_click(box3,3),relief="groove")
box4=Button(my_frame,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:button_click(box4,4),relief="groove")
box5=Button(my_frame,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:button_click(box5,5),relief="groove")
box6=Button(my_frame,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:button_click(box6,6),relief="groove")
box7=Button(my_frame,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:button_click(box7,7),relief="groove")
box8=Button(my_frame,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:button_click(box8,8),relief="groove")
box9=Button(my_frame,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:button_click(box9,9),relief="groove")
box10=Button(my_frame,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:button_click(box10,10),relief="groove")
box11=Button(my_frame,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:button_click(box11,11),relief="groove")

# gride our button
box0.grid(row=0,column=0)
box1.grid(row=0,column=1)
box1.grid(row=0,column=1)
box2.grid(row=0,column=2)
box2.grid(row=0,column=2)
box3.grid(row=0,column=3)

box4.grid(row=1,column=0)
box5.grid(row=1,column=1)
box6.grid(row=1,column=2)
box7.grid(row=1,column=3)

box8.grid(row=2,column=0)
box9.grid(row=2,column=1)
box10.grid(row=2,column=2)
box11.grid(row=2,column=3)

my_label=Label(root,text=" ")
my_label.pack(pady=20)

# create a menu
my_menu=Menu(root)
root.config(menu=my_menu)

# create an option dropdown menu
option_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Options",menu=option_menu)
option_menu.add_command(label="Reset_Game",command=reset)
option_menu.add_separator()
option_menu.add_command(label="Exit_Game",command=root.quit)
root.mainloop()