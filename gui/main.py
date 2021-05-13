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
lightedgrey = '#%02x%02x%02x' % (235, 235, 235)
lightblack = '#%02x%02x%02x' % (42,42,42)
large_font = ('Verdana',23)
medium_font = ('Verdana',15)
small_font = ('Verdana',11)
#function homebodyframe/findbodyframe/findseatbodyframe
def homepage():
    findbodyframe.pack_forget()
    findseatbodyframe.pack_forget()
    homebodyframe.pack(fill=X)
def findtrip():
    homebodyframe.pack_forget()
    findseatbodyframe.pack_forget()
    findbodyframe.pack(fill=X, ipady=50)
def findseat():
    homebodyframe.pack_forget()
    findbodyframe.pack_forget()
    findseatbodyframe.pack(fill=X, ipady=50)
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
homebtn = Button(menuframe, text="Home", fg='white', font=small_font, bg=blue, bd=2, highlightbackground = "white", command=homepage)
findticketbtn = Button(menuframe, text="Find Ticket", fg='white', font=small_font, bg=blue, bd=2, highlightbackground = "white", command=findtrip)
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
#START HOME PAGE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
homebodyframe = LabelFrame(containerframe)
#Blank Frame 2
homeblankframe2 = LabelFrame(homebodyframe, bg=grey, bd=0)
homeblankframe2.pack(fill=X, ipady=17)
#Home Image Frame
homeimageframe = LabelFrame(homebodyframe, bd=0)
homeimageframe.pack(fill=X)
homeimage = ImageTk.PhotoImage(Image.open('images/homeimage.png').resize((750,200), Image.ANTIALIAS))
imagelabel = Label(homeimageframe, image=homeimage, bg='white', bd=0)
#Display Image
imagelabel.pack(fill=X)
#Look for Frame
lookforframe = LabelFrame(homebodyframe, bg=blue, bd=0)
wheretogoframe = LabelFrame(lookforframe, bg=blue, bd=0)
findtripenntryframe = LabelFrame(lookforframe, bg=blue, bd=0)
seetriplabelframe = LabelFrame(lookforframe, bg=blue, bd=0)
wheretogolabel = Label(wheretogoframe, text="Where do you want to go?", fg="white", bg=blue, font=medium_font)
findtripentry = Entry(findtripenntryframe, font=small_font)
findtripbtn = Button(findtripenntryframe, text="GO", fg='white', bg=weightedblue)
seetripbtn = Button(seetriplabelframe, text='SEE ALL TRIP', fg="white", bg=weightedblue, font=small_font)
nulllframe = LabelFrame(lookforframe, bg=blue, bd=0)
#Display Look for Frame
lookforframe.pack(fill=X)
wheretogoframe.grid(row=0, column=0, ipadx=80)
findtripenntryframe.grid(row=0, column=1)
seetriplabelframe.grid(row=0, column=2, ipadx=80)
nulllframe.grid(row=0, column=3, ipadx=0, ipady=25)
wheretogolabel.pack()
findtripentry.grid(row=0, column=0, ipadx=20, ipady=7)
findtripbtn.grid(row=0, column=1, ipady=5)
seetripbtn.pack()
#Blank Frame 3
homeblankframe3 = LabelFrame(homebodyframe, bg=grey, bd=0)
homeblankframe3.pack(fill=X, ipady=17)
#Train Future
futureframe = LabelFrame(homebodyframe, bd=0)
tmplabel = Label(futureframe, text='Train Future', font=large_font)
#Display Future
futureframe.pack(fill=X, ipady=25)
tmplabel.pack(anchor=CENTER)
#Blank Frame 4
homeblankframe4 = LabelFrame(homebodyframe, bg=grey, bd=0)
homeblankframe4.pack(fill=X, ipady=17)
#Footer Frame
footerframe = LabelFrame(containerframe, bg=lightblack, bd=0)
tmplabel2 = Label(footerframe, text='ON WORKING', bg=lightblack, fg='white', font=medium_font).pack()

#START FIND PAGE !!!!!!!!!!!!!!!!!!!!!!
findbodyframe = LabelFrame(containerframe, bd=0, bg=grey)
#Blank Frame 1
findblankframe1 = LabelFrame(findbodyframe, bg=grey, bd=0)
findblankframe1.pack(fill=X, ipady=5)
#Comprehension Part
findcomprehensionframe = LabelFrame(findbodyframe, bd=0, bg=blue)
findcomprehensionlabel = Label(findcomprehensionframe, text="Find Ticket", font=medium_font, bg=blue, fg="white")
findcomprehensionframe.pack(ipadx=25)
findcomprehensionlabel.pack()
#Blank Frame 2
findblankframe2 = LabelFrame(findbodyframe, bg=grey, bd=0)
findblankframe2.pack(fill=X, ipady=17)
#Find Form Frame
findformframe = LabelFrame(findbodyframe, background="white", bd=0, highlightthickness=3, highlightbackground = "black")
findformframe.pack(ipadx=60)
marginframe1 = LabelFrame(findformframe, bg='white', bd=0)
marginframe1.pack()
journeyinfolabel = Label(marginframe1, text='JOURNEY INFORMATION', font=medium_font, fg=blue, bg="white")
journeyinfolabel.grid(row=0, column=0, ipadx=200)
#Blank Frame 3 (Horizontal Line)
findblankframe3 = LabelFrame(findformframe, bg='white', highlightthickness=2, highlightbackground = "black")
findblankframe3.pack(fill=X)
#Starting Station
marginframe2 = LabelFrame(findformframe, bd=0, bg=lightedgrey)
marginframe2.pack()
startlabel = Label(marginframe2, text='Starting Station', font=small_font, fg=blue, bg=lightedgrey)
startlabel.grid(row=1, column=0, sticky=W, columnspan=2)
startentry = Entry(marginframe2, highlightthickness=1, highlightbackground = blue, font=small_font)
startentry.grid(row=2, column=0, ipadx=270, ipady=5, columnspan=2)
#Blank Frame 4
findblankframe4 = LabelFrame(marginframe2, bg=lightedgrey, bd=0)
findblankframe4.grid(row=3, column=0, ipady=7, columnspan=2)
#Destination Station
destilabel = Label(marginframe2, text='Destination', font=small_font, fg=blue, bg=lightedgrey)
destilabel.grid(row=4, column=0, sticky=W, columnspan=2)
destientry = Entry(marginframe2, highlightthickness=1, highlightbackground = blue, font=small_font)
destientry.grid(row=5, column=0, ipadx=270, ipady=5, columnspan=2)
#Blank Frame 5
findblankframe5 = LabelFrame(marginframe2, bg=lightedgrey, bd=0)
findblankframe5.grid(row=6, column=0, ipady=7, columnspan=2)
#One-Doulbe Way selection
r = IntVar()
Radiobutton(marginframe2, text="One-way", font=small_font, fg=blue, variable=r, value=1).grid(row=7, column=0)
Radiobutton(marginframe2, text='Round-trip', font=small_font, fg=blue, variable=r, value=2).grid(row=7, column=1)
#Blank Frame 6
findblankframe6 = LabelFrame(marginframe2, bg=lightedgrey, bd=0)
findblankframe6.grid(row=8, column=0, ipady=7, columnspan=2)
#Depart and Return Day
departlabel = Label(marginframe2, text='Departure Day', font=small_font, fg=blue, bg=lightedgrey)
departlabel.grid(row=9, column=0, sticky=W)
departentry = Entry(marginframe2, highlightthickness=1, highlightbackground = blue, font=small_font)
departentry.grid(row=10, column=0, ipadx=35, ipady=5, sticky=W)
returndaylabel = Label(marginframe2, text='Returning Day', font=small_font, fg=blue, bg=lightedgrey)
returndaylabel.grid(row=9, column=1, sticky=W)
returndayentry = Entry(marginframe2, highlightthickness=1, highlightbackground = blue, font=small_font)
returndayentry.grid(row=10, column=1, ipadx=35, ipady=5, sticky=W)
#Blank Frame 7
findblankframe7 = LabelFrame(marginframe2, bg=lightedgrey, bd=0)
findblankframe7.grid(row=11, column=0, ipady=7, columnspan=2)
#Find Button
submitfindbtn = Button(marginframe2, text="FIND", font=medium_font, fg="white", bg=blue, command=findseat)
submitfindbtn.grid(row=12, ipadx=40, columnspan=2)

#START FIND SEAT PAGE !!!!!!!!!!!!!!!!!!!
findseatbodyframe = LabelFrame(containerframe, bd=0, bg="green")

#Display Fixed Frame
containerframe.pack(fill=BOTH, expand=YES)
headerframe.pack(fill=X, side=TOP)
blankframe1.pack(fill=X, ipady=17)
menuframe.pack(fill=X)
homebodyframe.pack(fill=X)
footerframe.pack(fill=X, side=BOTTOM)

root.mainloop()
