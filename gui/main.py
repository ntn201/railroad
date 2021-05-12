from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title('Good Job!')
root.geometry('1000x800') #wxh
root.maxsize(width=1000, height=800)
root.minsize(width=1000, height=800)
#Mystyle MyColor
blue = '#%02x%02x%02x' % (42,42,123)
weightedblue = '#%02x%02x%02x' % (0,0,102)
green = '#%02x%02x%02x' % (48, 191, 81)
grey = '#%02x%02x%02x' % (208,208,208)
lightblack = '#%02x%02x%02x' % (42,42,42)
large_font = ('Verdana',23)
medium_font = ('Verdana',15)
small_font = ('Verdana',11)
#Container
containerframe = LabelFrame(root, bg=blue)

#Header
headerframe = LabelFrame(containerframe, bg=blue)
brandframe = LabelFrame(headerframe, bd=0, bg=blue)
dateframe = LabelFrame(headerframe, bd=0, bg=blue)
trainbrandlabel = Label(brandframe, text='TRAIN MANAGEMENT SYSTEM', bg=blue, fg='white', font=large_font)
trainbrandlabel2 = Label(dateframe, text='Monday, 28/01/01', bg=blue, fg='white', font=small_font)
#Display Header
brandframe.grid(row=0, column=0, ipadx=60)
dateframe.grid(row=0, column=1, ipadx=100)
trainbrandlabel.pack(pady=15)
trainbrandlabel2.pack(pady=15)

#Blank Frame 1
blankframe1 = LabelFrame(containerframe, bg=grey, bd=0)

#Menu Frame
menuframe = LabelFrame(containerframe, bd=0, bg=blue)
homebtn = Button(menuframe, text="Home", fg='white', font=small_font, bg=blue, bd=2, highlightbackground = "white")
findticketbtn = Button(menuframe, text="Find Ticket", fg='white', font=small_font, bg=blue, bd=2, highlightbackground = "white")
reservebtn = Button(menuframe, text="Reservation Information", fg='white', font=small_font, bg=blue, bd=2, highlightbackground = "white")
checkticketbtn = Button(menuframe, text="Check Ticket", fg='white', font=small_font, bg=blue, bd=2, highlightbackground = "white")
regulationbtn = Button(menuframe, text="Regulations", fg='white', font=small_font, bg=blue, bd=2, highlightbackground = "white")
guidesbtn = Button(menuframe, text="Guides", fg='white', font=small_font, bg=blue, bd=2, highlightbackground = "white")
contactbtn = Button(menuframe, text="Contact", fg='white', font=small_font, bg=blue, bd=2, highlightbackground = "white")
#Display Menu
homebtn.grid(row=0, column=0, ipadx=25)
findticketbtn.grid(row=0, column=1, ipadx=25)
reservebtn.grid(row=0, column=2, ipadx=25)
checkticketbtn.grid(row=0, column=3, ipadx=25)
regulationbtn.grid(row=0, column=4, ipadx=25)
guidesbtn.grid(row=0, column=5, ipadx=15)
contactbtn.grid(row=0, column=6, ipadx=15)

#Blank Frame 2
blankframe2 = LabelFrame(containerframe, bg=grey, bd=0)

#Home Image Frame
homeimageframe = LabelFrame(containerframe, bd=0)
homeimage = ImageTk.PhotoImage(Image.open('images/homeimage.png').resize((750,200), Image.ANTIALIAS))
imagelabel = Label(homeimageframe, image=homeimage, bg='white', bd=0)
#Display Image
imagelabel.pack(fill=X)

#Look for Frame
lookforframe = LabelFrame(containerframe, bg=blue, bd=0)
wheretogoframe = LabelFrame(lookforframe, bg=blue, bd=0)
findtripenntryframe = LabelFrame(lookforframe, bg=blue, bd=0)
seetriplabelframe = LabelFrame(lookforframe, bg=blue, bd=0)
wheretogolabel = Label(wheretogoframe, text="Where do you want to go?", fg="white", bg=blue, font=medium_font)
findtripentry = Entry(findtripenntryframe, font=small_font)
findtripbtn = Button(findtripenntryframe, text="GO", fg='white', bg=weightedblue)
seetriplabel = Label(seetriplabelframe, text='SEE ALL TRIP', fg="white", bg=blue, font=small_font)
nulllframe = LabelFrame(lookforframe, bg=blue, bd=0)
#Display Look for Frame
wheretogoframe.grid(row=0, column=0, ipadx=80)
findtripenntryframe.grid(row=0, column=1)
seetriplabelframe.grid(row=0, column=2, ipadx=80)
nulllframe.grid(row=0, column=2, ipadx=0, ipady=25)
wheretogolabel.pack()
findtripentry.grid(row=0, column=0, ipadx=20, ipady=7)
findtripbtn.grid(row=0, column=1, ipady=5)
seetriplabel.pack()

#Blank Frame 3
blankframe3 = LabelFrame(containerframe, bg=grey, bd=0)

#Train Future
futureframe = LabelFrame(containerframe, bd=0)
tmplabel = Label(futureframe, text='Train Future', font=large_font)
#Display Future
tmplabel.pack(anchor=CENTER)

#Blank Frame 4
blankframe4 = LabelFrame(containerframe, bg=grey, bd=0)

#Footer Frame
footerframe = LabelFrame(containerframe, bg=lightblack, bd=0)
tmplabel2 = Label(footerframe, text='ON WORKING', bg=lightblack, fg='white', font=medium_font).pack()

#Display Frame
containerframe.pack(fill=BOTH, expand=YES)
headerframe.pack(fill=X, side=TOP)
blankframe1.pack(fill=X, ipady=17)
menuframe.pack(fill=X)
blankframe2.pack(fill=X, ipady=17)
homeimageframe.pack(fill=X)
lookforframe.pack(fill=X)
blankframe3.pack(fill=X, ipady=17)
futureframe.pack(fill=X, ipady=25)
blankframe4.pack(fill=X, ipady=17)
footerframe.pack(fill=X, side=BOTTOM)

root.mainloop()
