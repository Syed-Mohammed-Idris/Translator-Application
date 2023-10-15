
######################## Packages ############################
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from googletrans import Translator, LANGUAGES

###################### Main Window ############################
root = Tk()
root.geometry('600x500')
root.title('Translator')
root.iconbitmap('tr.ico')
root.resizable(False,False)
root.configure(bg='#856ff8')

########################################## Functions ############################################
def tt(event=None):
    translator = Translator()
    translated=translator.translate(text=entry1.get(1.0,END),dest=font_box.get())
    entry2.delete(1.0,END)
    entry2.insert(END,translated.text)

def main_exit():
    rr = messagebox.askyesnocancel('Notification','Do you want to exit?',parent=root)
    if(rr==True):
        root.destroy()

#################################### Binding Functions ####################################
def on_enterentry1(e):
    entry1['bg'] = 'springgreen'
def on_leaveentry1(e):
    entry1['bg'] = 'white'
def on_enterentry2(e):
    entry2['bg'] = 'springgreen'
def on_leaveentry2(e):
    entry2['bg'] = 'white'
def on_enterbtn1(e):
    btn1['bg'] = 'springgreen'
def on_leavebtn1(e):
    btn1['bg'] = 'cyan'
def on_enterbtn2(e):
    btn2['bg'] = 'springgreen'
def on_leavebtn2(e):
    btn2['bg'] = 'cyan'

##################################### ComboBox Languages #########################################
language = list(LANGUAGES.values())
font_box = ttk.Combobox(root,values=language,width=30,state='readonly')
font_box.set('Choose Language')
font_box.place(x=390,y=10)

####################################### Entry Box ###############################################
entry1 = Text(root,font=('times',20,'italic bold'),height=4,wrap=WORD,padx=5,pady=5,width=30)
entry1.place(x=155,y=50)
entry2 = Text(root,font=('times',20,'italic bold'),height=4,wrap=WORD,padx=5,pady=5,width=30)
entry2.place(x=155,y=200)

######################################### Labels ###############################################
label1 = Label(root,text='Enter Words : ',font=('times',17,'italic bold'),bg='#856ff8')
label1.place(x=10,y=50)
label2 = Label(root,text='Translated : ',font=('times',17,'italic bold'),bg='#856ff8')
label2.place(x=28,y=200)
label3 = Label(root,text='Translate To-> ',font=('times',11,'italic bold'),bg='#856ff8')
label3.place(x=288,y=10)
label4 = Label(root,text='Developed by Syed Mohammed Idris',font=('times',10,'italic bold'),bg='#856ff8')
label4.place(x=1,y=480)
label5 = Label(root,text='Exposys Data Labs',font=('times',10,'italic bold'),bg='#856ff8')
label5.place(x=488,y=480)
################################################## Buttons #############################################################
imgbt1 = PhotoImage(file='click.png')
imgbt2 = PhotoImage(file='images.png')
imgbt1 = imgbt1.subsample(5,5)
imgbt2 = imgbt2.subsample(5,5)
btn1 = Button(root,text='Translate',bd=10,bg='cyan',activebackground='blue',width=140,font=('times',15,'italic bold'),
              image=imgbt1,compound=RIGHT,command=tt)
btn1.place(x=110,y=370)
btn2 = Button(root,text='Exit',bd=10,bg='cyan',activebackground='red',width=140,font=('times',15,'italic bold'),
              image=imgbt2,compound=RIGHT,command=main_exit)
btn2.place(x=320,y=370)
root.bind('<Return>',tt)

###################### Binding ###########################
entry1.bind('<Enter>',on_enterentry1)
entry1.bind('<Leave>',on_leaveentry1)

entry2.bind('<Enter>',on_enterentry2)
entry2.bind('<Leave>',on_leaveentry2)

btn1.bind('<Enter>',on_enterbtn1)
btn1.bind('<Leave>',on_leavebtn1)

btn2.bind('<Enter>',on_enterbtn2)
btn2.bind('<Leave>',on_leavebtn2)

root.mainloop()

################## Exposys Data Labs ####################
#########################################################
# Developed By,                                         #
# Syed Mohammed Idris                                   #
# 1hk18is094@hkbk.edu.in                                #
# HKBK College Of Engineering                           #
# Information Science and Engineering                   #
# Internship Domain:Software Development[1 Month]       #
#########################################################