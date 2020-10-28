from tkinter import *
from pygame import mixer
from tkinter import filedialog
import tkinter.messagebox

window = Tk ()

mixer.init ()

window.geometry('300x300')
window.title('Audio Player')

def help_me():
    tkinter.messagebox.showinfo('Help','How can I help you')

def browse_file():
    global filename
    filename = filedialog.askopenfilename()

mb = Menu(window)
submenu = Menu(mb,tearoff=0)
window.config(menu=mb)

mb.add_cascade(label='File',menu=submenu)

submenu.add_command(label='Open',command=browse_file)
submenu.add_command(label='Exit',command=window.destroy)

submenu = Menu(mb,tearoff=0)
mb.add_cascade(label='About',menu=submenu)
#submenu = Menu(mb,tearoff=0)
submenu.add_command(label='Help',command=help_me)


#textLabel = Label(window,text='Play Button')
#textLabel.pack()

'''def printsomething () :
    print("It's being printed")'''
    
def play_music() :
    
    try:
        paused
    except:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text']="Music is playing"
        except:
            tkinter.messagebox.showerror('File Error','File Not Found')
            
    else:
        mixer.music.unpause()
        statusbar['text']="Music is resumed"

'''def stop_music() :
     mixer.music.stop ()'''
     
def set_volume (value):
    volume = int(value)/100
    mixer.music.set_volume (volume)
    
def pause_music():

    global paused
    paused=True
    mixer.music.pause() 
    statusbar['text']="Music is paused"

def rewind_music():
    mixer.music.rewind()
    statusbar['text']="Music is shuffled"

frame = Frame(window)
frame.pack(padx=10,pady=10)    

#photo = PhotoImage(file='p1.png')

'''photoLabel = Label(window,image=photo,height=200,width=150)
photoLabel.pack()'''

playButton = Button(frame,text='play',width=5,height=2,command=play_music,activebackground="lightgreen",cursor='hand2')
playButton.pack(padx=10,pady=10,side=LEFT)

#b=Button(text='Pause',width=5,height=2,bg='green',fg='white',activebackground='red',activeforeground='blue',cursor = 'hand2',command=stop_music).pack()

pausebtn =Button(frame,text='Pause',width=5,height=2,bg='green',fg='white',activebackground='red',activeforeground='blue',cursor = 'hand2',command=pause_music)
pausebtn.pack(padx=10,pady=10,side=LEFT)

bottomframe = Frame(window)
bottomframe.pack(padx=10,pady=10)

rewindButton = Button(frame,text='Shuffle',width=5,height=2,bg='pink',fg='white',activebackground='blue',activeforeground='orange',cursor = 'hand2',command=rewind_music)
rewindButton.pack(padx=10,pady=10,side=LEFT)

scale = Scale(bottomframe,from_=0,to=100,orient=HORIZONTAL,command=set_volume)
scale.set(50)
scale.pack()

l = Label(text='Volume').pack()

statusbar = Label(window,text="Keep enjoing music",relief=SUNKEN,anchor=W)
statusbar.pack(side=BOTTOM,fill=X)

window.mainloop()

