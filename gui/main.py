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
    userinfobodyframe.pack_forget()
    firstpageframe.pack()
    secondpageframe.pack_forget()
    thirdpageframe.pack_forget()
    homebodyframe.pack(fill=X)
def findtrip():
    homebodyframe.pack_forget()
    findseatbodyframe.pack_forget()
    userinfobodyframe.pack_forget()
    firstpageframe.pack()
    secondpageframe.pack_forget()
    thirdpageframe.pack_forget()
    findbodyframe.pack(fill=X, ipady=50)
def findseat():
    homebodyframe.pack_forget()
    findbodyframe.pack_forget()
    findseatbodyframe.pack(fill=X, ipady=40)
def userinfo():
    findseatbodyframe.pack_forget()
    userinfobodyframe.pack(fill=X, ipady=35)
def payment():
    firstpageframe.pack_forget()
    secondpageframe.pack()
def completed():
    secondpageframe.pack_forget()
    thirdpageframe.pack()

seatno = 0
def changecolor1():
    seatno = 1
    seatbtn1.config(image=redbtn1)
def changecolor2():
    seatno = 2
    seatbtn2.config(image=redbtn2)
def changecolor3():
    seatno = 3
    seatbtn3.config(image=redbtn3)
def changecolor4():
    seatno = 4
    seatbtn4.config(image=redbtn4)
def changecolor5():
    seatno = 5
    seatbtn5.config(image=redbtn5)
def changecolor6():
    seatno = 6
    seatbtn6.config(image=redbtn6)
def changecolor7():
    seatno = 7
    seatbtn7.config(image=redbtn7)
def changecolor8():
    seatno = 8
    seatbtn8.config(image=redbtn8)
def changecolor9():
    seatno = 9
    seatbtn9.config(image=redbtn9)
def changecolor10():
    seatno = 10
    seatbtn10.config(image=redbtn10)
def changecolor11():
    seatno = 11
    seatbtn11.config(image=redbtn11)
def changecolor12():
    seatno = 12
    seatbtn12.config(image=redbtn12)
def changecolor13():
    seatno = 13
    seatbtn13.config(image=redbtn13)
def changecolor14():
    seatno = 14
    seatbtn14.config(image=redbtn14)
def changecolor15():
    seatno = 15
    seatbtn15.config(image=redbtn15)
def changecolor16():
    seatno = 16
    seatbtn16.config(image=redbtn16)
def changecolor17():
    seatno = 17
    seatbtn17.config(image=redbtn17)
def changecolor18():
    seatno = 18
    seatbtn18.config(image=redbtn18)
def changecolor19():
    seatno = 19
    seatbtn19.config(image=redbtn19)
def changecolor20():
    seatno = 20
    seatbtn20.config(image=redbtn20)
def changecolor21():
    seatno = 21
    seatbtn21.config(image=redbtn21)
def changecolor22():
    seatno = 22
    seatbtn22.config(image=redbtn22)
def changecolor23():
    seatno = 23
    seatbtn23.config(image=redbtn23)
def changecolor24():
    seatno = 24
    seatbtn24.config(image=redbtn24)
def changecolor25():
    seatno = 25
    seatbtn25.config(image=redbtn25)
def changecolor26():
    seatno = 26
    seatbtn26.config(image=redbtn26)
def changecolor27():
    seatno = 27
    seatbtn27.config(image=redbtn27)
def changecolor28():
    seatno = 28
    seatbtn28.config(image=redbtn28)
def changecolor29():
    seatno = 29
    seatbtn29.config(image=redbtn29)
def changecolor30():
    seatno = 30
    seatbtn30.config(image=redbtn30)
def changecolor31():
    seatno = 31
    seatbtn31.config(image=redbtn31)
def changecolor32():
    seatno = 32
    seatbtn32.config(image=redbtn32)
def changecolor33():
    seatno = 33
    seatbtn33.config(image=redbtn33)
def changecolor34():
    seatno = 34
    seatbtn34.config(image=redbtn34)
def changecolor35():
    seatno = 35
    seatbtn35.config(image=redbtn35)
def changecolor36():
    seatno = 36
    seatbtn36.config(image=redbtn36)
def changecolor37():
    seatno = 37
    seatbtn37.config(image=redbtn37)
def changecolor38():
    seatno = 38
    seatbtn38.config(image=redbtn38)
def changecolor39():
    seatno = 39
    seatbtn39.config(image=redbtn39)
def changecolor40():
    seatno = 40
    seatbtn40.config(image=redbtn40)
def changecolor41():
    seatno = 41
    seatbtn41.config(image=redbtn41)
def changecolor42():
    seatno = 42
    seatbtn42.config(image=redbtn42)
def changecolor43():
    seatno = 43
    seatbtn43.config(image=redbtn43)
def changecolor44():
    seatno = 44
    seatbtn44.config(image=redbtn44)
def changecolor45():
    seatno = 45
    seatbtn45.config(image=redbtn45)
def changecolor46():
    seatno = 46
    seatbtn46.config(image=redbtn46)
def changecolor47():
    seatno = 47
    seatbtn47.config(image=redbtn47)
def changecolor48():
    seatno = 48
    seatbtn48.config(image=redbtn48)
def changecolor49():
    seatno = 49
    seatbtn49.config(image=redbtn49)
def changecolor50():
    seatno = 50
    seatbtn50.config(image=redbtn50)
def changecolor51():
    seatno = 51
    seatbtn51.config(image=redbtn51)
def changecolor52():
    seatno = 52
    seatbtn52.config(image=redbtn52)
def changecolor53():
    seatno = 53
    seatbtn53.config(image=redbtn53)
def changecolor54():
    seatno = 54
    seatbtn54.config(image=redbtn54)
def changecolor55():
    seatno = 55
    seatbtn55.config(image=redbtn55)
def changecolor56():
    seatno = 56
    seatbtn56.config(image=redbtn56)
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
r1 = IntVar()
Radiobutton(marginframe2, text="One-way", font=small_font, fg=blue, variable=r1, value=1).grid(row=7, column=0)
Radiobutton(marginframe2, text='Round-trip', font=small_font, fg=blue, variable=r1, value=2).grid(row=7, column=1)
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
findseatbodyframe = LabelFrame(containerframe, bd=0, bg=grey)
#Blank Frame 1
seatblankframe1 = LabelFrame(findseatbodyframe, bg=grey, bd=0)
seatblankframe1.pack(fill=X, ipady=35)
#Seat Background Frame
seatbgframe = LabelFrame(findseatbodyframe, bd=0, bg=grey)
seatbgframe.pack()
#Seat Holder Container Frame
seatcontainerframe = LabelFrame(seatbgframe, highlightthickness=2, highlightbackground = blue)
seatcontainerframe.grid(row=0, column=0)
#56 Seats (VERY LAZY THIS PART!!!!)
#Left-Mid-Right Part Frame
seatleftframe = LabelFrame(seatcontainerframe, bd=0, bg=lightedgrey)
seatmidframe = LabelFrame(seatcontainerframe, bd=0, bg=lightedgrey)
seatrightframe = LabelFrame(seatcontainerframe, bd=0, bg=lightedgrey)
seatleftframe.grid(row=0, column=0)
seatmidframe.grid(row=0, column=1)
seatrightframe.grid(row=0, column=2)
#Import Image
greenbtn1 = ImageTk.PhotoImage(Image.open('images/green/1.png').resize((64, 45), Image.ANTIALIAS))
greenbtn2 = ImageTk.PhotoImage(Image.open('images/green/2.png').resize((64, 45), Image.ANTIALIAS))
greenbtn3 = ImageTk.PhotoImage(Image.open('images/green/3.png').resize((64, 45), Image.ANTIALIAS))
greenbtn4 = ImageTk.PhotoImage(Image.open('images/green/4.png').resize((64, 45), Image.ANTIALIAS))
greenbtn5 = ImageTk.PhotoImage(Image.open('images/green/5.png').resize((64, 45), Image.ANTIALIAS))
greenbtn6 = ImageTk.PhotoImage(Image.open('images/green/6.png').resize((64, 45), Image.ANTIALIAS))
greenbtn7 = ImageTk.PhotoImage(Image.open('images/green/7.png').resize((64, 45), Image.ANTIALIAS))
greenbtn8 = ImageTk.PhotoImage(Image.open('images/green/8.png').resize((64, 45), Image.ANTIALIAS))
greenbtn9 = ImageTk.PhotoImage(Image.open('images/green/9.png').resize((64, 45), Image.ANTIALIAS))
greenbtn10 = ImageTk.PhotoImage(Image.open('images/green/10.png').resize((64, 45), Image.ANTIALIAS))
greenbtn11 = ImageTk.PhotoImage(Image.open('images/green/11.png').resize((64, 45), Image.ANTIALIAS))
greenbtn12 = ImageTk.PhotoImage(Image.open('images/green/12.png').resize((64, 45), Image.ANTIALIAS))
greenbtn13 = ImageTk.PhotoImage(Image.open('images/green/13.png').resize((64, 45), Image.ANTIALIAS))
greenbtn14 = ImageTk.PhotoImage(Image.open('images/green/14.png').resize((64, 45), Image.ANTIALIAS))
greenbtn15 = ImageTk.PhotoImage(Image.open('images/green/15.png').resize((64, 45), Image.ANTIALIAS))
greenbtn16 = ImageTk.PhotoImage(Image.open('images/green/16.png').resize((64, 45), Image.ANTIALIAS))
greenbtn17 = ImageTk.PhotoImage(Image.open('images/green/17.png').resize((64, 45), Image.ANTIALIAS))
greenbtn18 = ImageTk.PhotoImage(Image.open('images/green/18.png').resize((64, 45), Image.ANTIALIAS))
greenbtn19 = ImageTk.PhotoImage(Image.open('images/green/19.png').resize((64, 45), Image.ANTIALIAS))
greenbtn20 = ImageTk.PhotoImage(Image.open('images/green/20.png').resize((64, 45), Image.ANTIALIAS))
greenbtn21 = ImageTk.PhotoImage(Image.open('images/green/21.png').resize((64, 45), Image.ANTIALIAS))
greenbtn22 = ImageTk.PhotoImage(Image.open('images/green/22.png').resize((64, 45), Image.ANTIALIAS))
greenbtn23 = ImageTk.PhotoImage(Image.open('images/green/23.png').resize((64, 45), Image.ANTIALIAS))
greenbtn24 = ImageTk.PhotoImage(Image.open('images/green/24.png').resize((64, 45), Image.ANTIALIAS))
greenbtn25 = ImageTk.PhotoImage(Image.open('images/green/25.png').resize((64, 45), Image.ANTIALIAS))
greenbtn26 = ImageTk.PhotoImage(Image.open('images/green/26.png').resize((64, 45), Image.ANTIALIAS))
greenbtn27 = ImageTk.PhotoImage(Image.open('images/green/27.png').resize((64, 45), Image.ANTIALIAS))
greenbtn28 = ImageTk.PhotoImage(Image.open('images/green/28.png').resize((64, 45), Image.ANTIALIAS))
greenbtn29 = ImageTk.PhotoImage(Image.open('images/green/29.png').resize((64, 45), Image.ANTIALIAS))
greenbtn30 = ImageTk.PhotoImage(Image.open('images/green/30.png').resize((64, 45), Image.ANTIALIAS))
greenbtn31 = ImageTk.PhotoImage(Image.open('images/green/31.png').resize((64, 45), Image.ANTIALIAS))
greenbtn32 = ImageTk.PhotoImage(Image.open('images/green/32.png').resize((64, 45), Image.ANTIALIAS))
greenbtn33 = ImageTk.PhotoImage(Image.open('images/green/33.png').resize((64, 45), Image.ANTIALIAS))
greenbtn34 = ImageTk.PhotoImage(Image.open('images/green/34.png').resize((64, 45), Image.ANTIALIAS))
greenbtn35 = ImageTk.PhotoImage(Image.open('images/green/35.png').resize((64, 45), Image.ANTIALIAS))
greenbtn36 = ImageTk.PhotoImage(Image.open('images/green/36.png').resize((64, 45), Image.ANTIALIAS))
greenbtn37 = ImageTk.PhotoImage(Image.open('images/green/37.png').resize((64, 45), Image.ANTIALIAS))
greenbtn38 = ImageTk.PhotoImage(Image.open('images/green/38.png').resize((64, 45), Image.ANTIALIAS))
greenbtn39 = ImageTk.PhotoImage(Image.open('images/green/39.png').resize((64, 45), Image.ANTIALIAS))
greenbtn40 = ImageTk.PhotoImage(Image.open('images/green/40.png').resize((64, 45), Image.ANTIALIAS))
greenbtn41 = ImageTk.PhotoImage(Image.open('images/green/41.png').resize((64, 45), Image.ANTIALIAS))
greenbtn42 = ImageTk.PhotoImage(Image.open('images/green/42.png').resize((64, 45), Image.ANTIALIAS))
greenbtn43 = ImageTk.PhotoImage(Image.open('images/green/43.png').resize((64, 45), Image.ANTIALIAS))
greenbtn44 = ImageTk.PhotoImage(Image.open('images/green/44.png').resize((64, 45), Image.ANTIALIAS))
greenbtn45 = ImageTk.PhotoImage(Image.open('images/green/45.png').resize((64, 45), Image.ANTIALIAS))
greenbtn46 = ImageTk.PhotoImage(Image.open('images/green/46.png').resize((64, 45), Image.ANTIALIAS))
greenbtn47 = ImageTk.PhotoImage(Image.open('images/green/47.png').resize((64, 45), Image.ANTIALIAS))
greenbtn48 = ImageTk.PhotoImage(Image.open('images/green/48.png').resize((64, 45), Image.ANTIALIAS))
greenbtn49 = ImageTk.PhotoImage(Image.open('images/green/49.png').resize((64, 45), Image.ANTIALIAS))
greenbtn50 = ImageTk.PhotoImage(Image.open('images/green/50.png').resize((64, 45), Image.ANTIALIAS))
greenbtn51 = ImageTk.PhotoImage(Image.open('images/green/51.png').resize((64, 45), Image.ANTIALIAS))
greenbtn52 = ImageTk.PhotoImage(Image.open('images/green/52.png').resize((64, 45), Image.ANTIALIAS))
greenbtn53 = ImageTk.PhotoImage(Image.open('images/green/53.png').resize((64, 45), Image.ANTIALIAS))
greenbtn54 = ImageTk.PhotoImage(Image.open('images/green/54.png').resize((64, 45), Image.ANTIALIAS))
greenbtn55 = ImageTk.PhotoImage(Image.open('images/green/55.png').resize((64, 45), Image.ANTIALIAS))
greenbtn56 = ImageTk.PhotoImage(Image.open('images/green/56.png').resize((64, 45), Image.ANTIALIAS))
redbtn1 = ImageTk.PhotoImage(Image.open('images/red/1.png').resize((64, 45), Image.ANTIALIAS))
redbtn2 = ImageTk.PhotoImage(Image.open('images/red/2.png').resize((64, 45), Image.ANTIALIAS))
redbtn3 = ImageTk.PhotoImage(Image.open('images/red/3.png').resize((64, 45), Image.ANTIALIAS))
redbtn4 = ImageTk.PhotoImage(Image.open('images/red/4.png').resize((64, 45), Image.ANTIALIAS))
redbtn5 = ImageTk.PhotoImage(Image.open('images/red/5.png').resize((64, 45), Image.ANTIALIAS))
redbtn6 = ImageTk.PhotoImage(Image.open('images/red/6.png').resize((64, 45), Image.ANTIALIAS))
redbtn7 = ImageTk.PhotoImage(Image.open('images/red/7.png').resize((64, 45), Image.ANTIALIAS))
redbtn8 = ImageTk.PhotoImage(Image.open('images/red/8.png').resize((64, 45), Image.ANTIALIAS))
redbtn9 = ImageTk.PhotoImage(Image.open('images/red/9.png').resize((64, 45), Image.ANTIALIAS))
redbtn10 = ImageTk.PhotoImage(Image.open('images/red/10.png').resize((64, 45), Image.ANTIALIAS))
redbtn11 = ImageTk.PhotoImage(Image.open('images/red/11.png').resize((64, 45), Image.ANTIALIAS))
redbtn12 = ImageTk.PhotoImage(Image.open('images/red/12.png').resize((64, 45), Image.ANTIALIAS))
redbtn13 = ImageTk.PhotoImage(Image.open('images/red/13.png').resize((64, 45), Image.ANTIALIAS))
redbtn14 = ImageTk.PhotoImage(Image.open('images/red/14.png').resize((64, 45), Image.ANTIALIAS))
redbtn15 = ImageTk.PhotoImage(Image.open('images/red/15.png').resize((64, 45), Image.ANTIALIAS))
redbtn16 = ImageTk.PhotoImage(Image.open('images/red/16.png').resize((64, 45), Image.ANTIALIAS))
redbtn17 = ImageTk.PhotoImage(Image.open('images/red/17.png').resize((64, 45), Image.ANTIALIAS))
redbtn18 = ImageTk.PhotoImage(Image.open('images/red/18.png').resize((64, 45), Image.ANTIALIAS))
redbtn19 = ImageTk.PhotoImage(Image.open('images/red/19.png').resize((64, 45), Image.ANTIALIAS))
redbtn20 = ImageTk.PhotoImage(Image.open('images/red/20.png').resize((64, 45), Image.ANTIALIAS))
redbtn21 = ImageTk.PhotoImage(Image.open('images/red/21.png').resize((64, 45), Image.ANTIALIAS))
redbtn22 = ImageTk.PhotoImage(Image.open('images/red/22.png').resize((64, 45), Image.ANTIALIAS))
redbtn23 = ImageTk.PhotoImage(Image.open('images/red/23.png').resize((64, 45), Image.ANTIALIAS))
redbtn24 = ImageTk.PhotoImage(Image.open('images/red/24.png').resize((64, 45), Image.ANTIALIAS))
redbtn25 = ImageTk.PhotoImage(Image.open('images/red/25.png').resize((64, 45), Image.ANTIALIAS))
redbtn26 = ImageTk.PhotoImage(Image.open('images/red/26.png').resize((64, 45), Image.ANTIALIAS))
redbtn27 = ImageTk.PhotoImage(Image.open('images/red/27.png').resize((64, 45), Image.ANTIALIAS))
redbtn28 = ImageTk.PhotoImage(Image.open('images/red/28.png').resize((64, 45), Image.ANTIALIAS))
redbtn29 = ImageTk.PhotoImage(Image.open('images/red/29.png').resize((64, 45), Image.ANTIALIAS))
redbtn30 = ImageTk.PhotoImage(Image.open('images/red/30.png').resize((64, 45), Image.ANTIALIAS))
redbtn31 = ImageTk.PhotoImage(Image.open('images/red/31.png').resize((64, 45), Image.ANTIALIAS))
redbtn32 = ImageTk.PhotoImage(Image.open('images/red/32.png').resize((64, 45), Image.ANTIALIAS))
redbtn33 = ImageTk.PhotoImage(Image.open('images/red/33.png').resize((64, 45), Image.ANTIALIAS))
redbtn34 = ImageTk.PhotoImage(Image.open('images/red/34.png').resize((64, 45), Image.ANTIALIAS))
redbtn35 = ImageTk.PhotoImage(Image.open('images/red/35.png').resize((64, 45), Image.ANTIALIAS))
redbtn36 = ImageTk.PhotoImage(Image.open('images/red/36.png').resize((64, 45), Image.ANTIALIAS))
redbtn37 = ImageTk.PhotoImage(Image.open('images/red/37.png').resize((64, 45), Image.ANTIALIAS))
redbtn38 = ImageTk.PhotoImage(Image.open('images/red/38.png').resize((64, 45), Image.ANTIALIAS))
redbtn39 = ImageTk.PhotoImage(Image.open('images/red/39.png').resize((64, 45), Image.ANTIALIAS))
redbtn40 = ImageTk.PhotoImage(Image.open('images/red/40.png').resize((64, 45), Image.ANTIALIAS))
redbtn41 = ImageTk.PhotoImage(Image.open('images/red/41.png').resize((64, 45), Image.ANTIALIAS))
redbtn42 = ImageTk.PhotoImage(Image.open('images/red/42.png').resize((64, 45), Image.ANTIALIAS))
redbtn43 = ImageTk.PhotoImage(Image.open('images/red/43.png').resize((64, 45), Image.ANTIALIAS))
redbtn44 = ImageTk.PhotoImage(Image.open('images/red/44.png').resize((64, 45), Image.ANTIALIAS))
redbtn45 = ImageTk.PhotoImage(Image.open('images/red/45.png').resize((64, 45), Image.ANTIALIAS))
redbtn46 = ImageTk.PhotoImage(Image.open('images/red/46.png').resize((64, 45), Image.ANTIALIAS))
redbtn47 = ImageTk.PhotoImage(Image.open('images/red/47.png').resize((64, 45), Image.ANTIALIAS))
redbtn48 = ImageTk.PhotoImage(Image.open('images/red/48.png').resize((64, 45), Image.ANTIALIAS))
redbtn49 = ImageTk.PhotoImage(Image.open('images/red/49.png').resize((64, 45), Image.ANTIALIAS))
redbtn50 = ImageTk.PhotoImage(Image.open('images/red/50.png').resize((64, 45), Image.ANTIALIAS))
redbtn51 = ImageTk.PhotoImage(Image.open('images/red/51.png').resize((64, 45), Image.ANTIALIAS))
redbtn52 = ImageTk.PhotoImage(Image.open('images/red/52.png').resize((64, 45), Image.ANTIALIAS))
redbtn53 = ImageTk.PhotoImage(Image.open('images/red/53.png').resize((64, 45), Image.ANTIALIAS))
redbtn54 = ImageTk.PhotoImage(Image.open('images/red/54.png').resize((64, 45), Image.ANTIALIAS))
redbtn55 = ImageTk.PhotoImage(Image.open('images/red/55.png').resize((64, 45), Image.ANTIALIAS))
redbtn56 = ImageTk.PhotoImage(Image.open('images/red/56.png').resize((64, 45), Image.ANTIALIAS))
barriel = ImageTk.PhotoImage(Image.open('images/barriel.png').resize((40, 90), Image.ANTIALIAS))
#Seat Left Display
seatbtn1 = Button(seatleftframe, image=greenbtn1, borderwidth=0, command=changecolor1)
seatbtn1.grid(row=0, column=0)
seatbtn2 = Button(seatleftframe, image=greenbtn2, borderwidth=0, command=changecolor2)
seatbtn2.grid(row=1, column=0)
seatbtn3 = Button(seatleftframe, image=greenbtn3, borderwidth=0, command=changecolor3)
seatbtn3.grid(row=2, column=0)
seatbtn4 = Button(seatleftframe, image=greenbtn4, borderwidth=0, command=changecolor4)
seatbtn4.grid(row=3, column=0)
seatbtn5 = Button(seatleftframe, image=greenbtn5, borderwidth=0, command=changecolor5)
seatbtn5.grid(row=3, column=1)
seatbtn6 = Button(seatleftframe, image=greenbtn6, borderwidth=0, command=changecolor6)
seatbtn6.grid(row=2, column=1)
seatbtn7 = Button(seatleftframe, image=greenbtn7, borderwidth=0, command=changecolor7)
seatbtn7.grid(row=1, column=1)
seatbtn8 = Button(seatleftframe, image=greenbtn8, borderwidth=0, command=changecolor8)
seatbtn8.grid(row=0, column=1)
seatbtn9 = Button(seatleftframe, image=greenbtn9, borderwidth=0, command=changecolor9)
seatbtn9.grid(row=0, column=2)
seatbtn10 = Button(seatleftframe, image=greenbtn10, borderwidth=0, command=changecolor10)
seatbtn10.grid(row=1, column=2)
seatbtn11 = Button(seatleftframe, image=greenbtn11, borderwidth=0, command=changecolor11)
seatbtn11.grid(row=2, column=2)
seatbtn12 = Button(seatleftframe, image=greenbtn12, borderwidth=0, command=changecolor12)
seatbtn12.grid(row=3, column=2)
seatbtn13 = Button(seatleftframe, image=greenbtn13, borderwidth=0, command=changecolor13)
seatbtn13.grid(row=3, column=3)
seatbtn14 = Button(seatleftframe, image=greenbtn14, borderwidth=0, command=changecolor14)
seatbtn14.grid(row=2, column=3)
seatbtn15 = Button(seatleftframe, image=greenbtn15, borderwidth=0, command=changecolor15)
seatbtn15.grid(row=1, column=3)
seatbtn16 = Button(seatleftframe, image=greenbtn16, borderwidth=0, command=changecolor16)
seatbtn16.grid(row=0, column=3)
seatbtn17 = Button(seatleftframe, image=greenbtn17, borderwidth=0, command=changecolor17)
seatbtn17.grid(row=0, column=4)
seatbtn18 = Button(seatleftframe, image=greenbtn18, borderwidth=0, command=changecolor18)
seatbtn18.grid(row=1, column=4)
seatbtn19 = Button(seatleftframe, image=greenbtn19, borderwidth=0, command=changecolor19)
seatbtn19.grid(row=2, column=4)
seatbtn20 = Button(seatleftframe, image=greenbtn20, borderwidth=0, command=changecolor20)
seatbtn20.grid(row=3, column=4)
seatbtn21 = Button(seatleftframe, image=greenbtn21, borderwidth=0, command=changecolor21)
seatbtn21.grid(row=3, column=5)
seatbtn22 = Button(seatleftframe, image=greenbtn22, borderwidth=0, command=changecolor22)
seatbtn22.grid(row=2, column=5)
seatbtn23 = Button(seatleftframe, image=greenbtn23, borderwidth=0, command=changecolor23)
seatbtn23.grid(row=1, column=5)
seatbtn24 = Button(seatleftframe, image=greenbtn24, borderwidth=0, command=changecolor24)
seatbtn24.grid(row=0, column=5)
seatbtn25 = Button(seatleftframe, image=greenbtn25, borderwidth=0, command=changecolor25)
seatbtn25.grid(row=0, column=6)
seatbtn26 = Button(seatleftframe, image=greenbtn26, borderwidth=0, command=changecolor26)
seatbtn26.grid(row=1, column=6)
seatbtn27 = Button(seatleftframe, image=greenbtn27, borderwidth=0, command=changecolor27)
seatbtn27.grid(row=2, column=6)
seatbtn28 = Button(seatleftframe, image=greenbtn28, borderwidth=0, command=changecolor28)
seatbtn28.grid(row=3, column=6)
#Seat Mid Display
barriel1label = Label(seatmidframe, image=barriel, bg=lightedgrey, bd=0)
barriel2label = Label(seatmidframe, image=barriel, bg=lightedgrey, bd=0)
barriel1label.pack()
barriel2label.pack()
#Seat Right Display
seatbtn29 = Button(seatrightframe, image=greenbtn29, borderwidth=0, command=changecolor29)
seatbtn29.grid(row=0, column=0)
seatbtn30 = Button(seatrightframe, image=greenbtn30, borderwidth=0, command=changecolor30)
seatbtn30.grid(row=1, column=0)
seatbtn31 = Button(seatrightframe, image=greenbtn31, borderwidth=0, command=changecolor31)
seatbtn31.grid(row=2, column=0)
seatbtn32 = Button(seatrightframe, image=greenbtn32, borderwidth=0, command=changecolor32)
seatbtn32.grid(row=3, column=0)
seatbtn33 = Button(seatrightframe, image=greenbtn33, borderwidth=0, command=changecolor33)
seatbtn33.grid(row=3, column=1)
seatbtn34 = Button(seatrightframe, image=greenbtn34, borderwidth=0, command=changecolor34)
seatbtn34.grid(row=2, column=1)
seatbtn35 = Button(seatrightframe, image=greenbtn35, borderwidth=0, command=changecolor35)
seatbtn35.grid(row=1, column=1)
seatbtn36 = Button(seatrightframe, image=greenbtn36, borderwidth=0, command=changecolor36)
seatbtn36.grid(row=0, column=1)
seatbtn37 = Button(seatrightframe, image=greenbtn37, borderwidth=0, command=changecolor37)
seatbtn37.grid(row=0, column=2)
seatbtn38 = Button(seatrightframe, image=greenbtn38, borderwidth=0, command=changecolor38)
seatbtn38.grid(row=1, column=2)
seatbtn39 = Button(seatrightframe, image=greenbtn39, borderwidth=0, command=changecolor39)
seatbtn39.grid(row=2, column=2)
seatbtn40 = Button(seatrightframe, image=greenbtn40, borderwidth=0, command=changecolor40)
seatbtn40.grid(row=3, column=2)
seatbtn41 = Button(seatrightframe, image=greenbtn41, borderwidth=0, command=changecolor41)
seatbtn41.grid(row=3, column=3)
seatbtn42 = Button(seatrightframe, image=greenbtn42, borderwidth=0, command=changecolor42)
seatbtn42.grid(row=2, column=3)
seatbtn43 = Button(seatrightframe, image=greenbtn43, borderwidth=0, command=changecolor43)
seatbtn43.grid(row=1, column=3)
seatbtn44 = Button(seatrightframe, image=greenbtn44, borderwidth=0, command=changecolor44)
seatbtn44.grid(row=0, column=3)
seatbtn45 = Button(seatrightframe, image=greenbtn45, borderwidth=0, command=changecolor45)
seatbtn45.grid(row=0, column=4)
seatbtn46 = Button(seatrightframe, image=greenbtn46, borderwidth=0, command=changecolor46)
seatbtn46.grid(row=1, column=4)
seatbtn47 = Button(seatrightframe, image=greenbtn47, borderwidth=0, command=changecolor47)
seatbtn47.grid(row=2, column=4)
seatbtn48 = Button(seatrightframe, image=greenbtn48, borderwidth=0, command=changecolor48)
seatbtn48.grid(row=3, column=4)
seatbtn49 = Button(seatrightframe, image=greenbtn49, borderwidth=0, command=changecolor49)
seatbtn49.grid(row=3, column=5)
seatbtn50 = Button(seatrightframe, image=greenbtn50, borderwidth=0, command=changecolor50)
seatbtn50.grid(row=2, column=5)
seatbtn51 = Button(seatrightframe, image=greenbtn51, borderwidth=0, command=changecolor51)
seatbtn51.grid(row=1, column=5)
seatbtn52 = Button(seatrightframe, image=greenbtn52, borderwidth=0, command=changecolor52)
seatbtn52.grid(row=0, column=5)
seatbtn53 = Button(seatrightframe, image=greenbtn53, borderwidth=0, command=changecolor53)
seatbtn53.grid(row=0, column=6)
seatbtn54 = Button(seatrightframe, image=greenbtn54, borderwidth=0, command=changecolor54)
seatbtn54.grid(row=1, column=6)
seatbtn55 = Button(seatrightframe, image=greenbtn55, borderwidth=0, command=changecolor55)
seatbtn55.grid(row=2, column=6)
seatbtn56 = Button(seatrightframe, image=greenbtn56, borderwidth=0, command=changecolor56)
seatbtn56.grid(row=3, column=6)
#Blank Frame 2
seatblankframe2 = LabelFrame(findseatbodyframe, bg=grey, bd=0)
seatblankframe2.pack(fill=X, ipady=15)
#Find Seat Submit Button
findseatbtn = Button(findseatbodyframe, text="Next", fg="white", bg=blue, font=medium_font, command=userinfo)
findseatbtn.pack(ipadx=40)
#User Info Page Frame !!!!!!!!!!!!!!!!!!
userinfobodyframe = LabelFrame(containerframe, bd = 0, bg=grey)
#Blank Frame 1
customerinfoblankframe1 = LabelFrame(userinfobodyframe, bg=grey, bd=0)
customerinfoblankframe1.pack(fill=X, ipady=25)
userholderframe = LabelFrame(userinfobodyframe, highlightthickness=2, highlightbackground = blue, bg='white')
userholderframe.pack()
#Customer Info(1st Page)
firstpageframe = LabelFrame(userholderframe, bd=0, bg='white')
firstpageframe.pack()
#Progress Bar
progress1img = ImageTk.PhotoImage(Image.open('images/customerinfobar.png').resize((800, 100), Image.ANTIALIAS))
progresslabel = Label(firstpageframe, image=progress1img, bg='white')
progresslabel.grid(row=0, column=0, columnspan=3)
#Sub head 1 label
subhead1img = ImageTk.PhotoImage(Image.open('images/customerinfolabel.png').resize((160, 60), Image.ANTIALIAS))
subhead1label = Label(firstpageframe, image=subhead1img, bg='white')
subhead1label.grid(row=1, column=0, sticky='W', pady=5)
#Left-Mid-Right UserInfo Frame
userinfoleftframe = LabelFrame(firstpageframe, bg='white', bd=0)
userinfoleftframe.grid(row=2, column=0, pady=10)
userinfomidframe = LabelFrame(firstpageframe, bg='white')
userinfomidframe.grid(row=2, column=1, ipady=10, pady=10)
userinforightframe = LabelFrame(firstpageframe, bg='white', bd=0)
userinforightframe.grid(row=2, column=2, pady=10)
#Component
fullnamelabel = Label(userinfoleftframe, text="Full Name", bg='white', font=small_font)
fullnamelabel.grid(row=0, column=0)
fullnameentry = Entry(userinfoleftframe, font=small_font, highlightthickness=2, highlightbackground = blue)
fullnameentry.grid(row=0, column=1, ipady=5, pady=12)
emaillabel = Label(userinfoleftframe, text="Email", bg='white', font=small_font)
emaillabel.grid(row=1, column=0)
emailentry = Entry(userinfoleftframe, font=small_font, highlightthickness=2, highlightbackground = blue)
emailentry.grid(row=1, column=1, ipady=5, pady=12)
phonenumberlabel = Label(userinfoleftframe, text="Phone Number", bg='white', font=small_font)
phonenumberlabel.grid(row=2, column=0)
phonenumberentry = Entry(userinfoleftframe, font=small_font, highlightthickness=2, highlightbackground = blue)
phonenumberentry.grid(row=2, column=1, ipady=5, pady=12)
idpassportlabel = Label(userinforightframe, text="ID/Passport Number", bg='white', font=small_font)
idpassportlabel.grid(row=0, column=0)
idpassportentry = Entry(userinforightframe, font=small_font, highlightthickness=2, highlightbackground = blue)
idpassportentry.grid(row=0, column=1, ipady=5, pady=12)
emailconfirmlabel = Label(userinforightframe, text="Email Confirmation", bg='white', font=small_font)
emailconfirmlabel.grid(row=1, column=0)
emailconfirmentry = Entry(userinforightframe, font=small_font, highlightthickness=2, highlightbackground = blue)
emailconfirmentry.grid(row=1, column=1, ipady=5, pady=12)
userinfonextbtn = Button(firstpageframe, font=medium_font, text="Next", fg="white", bg=blue, command=payment)
userinfonextbtn.grid(row=3, column=0, columnspan=3, ipadx=15, pady=10)
#Payment Page(2nd Page)
secondpageframe = LabelFrame(userholderframe, bd=0, bg='white')
#Progress Bar
progress2img = ImageTk.PhotoImage(Image.open('images/paymentbar.png').resize((800, 100), Image.ANTIALIAS))
progress2label = Label(secondpageframe, image=progress2img, bg='white')
progress2label.grid(row=0, column=0)
#Sub head 2 label
subhead2img = ImageTk.PhotoImage(Image.open('images/paymentlabel.png').resize((160, 60), Image.ANTIALIAS))
subhead2label = Label(secondpageframe, image=subhead2img, bg='white')
subhead2label.grid(row=1, column=0, sticky='W', pady=5)
#Component page 2
r2 = IntVar()
Radiobutton(secondpageframe, text="Purchase offline(at gas station, postoffice)", font=medium_font, fg=blue, variable=r2, value=1, bg="white").grid(row=2, column=0, sticky='W', pady=5)
Radiobutton(secondpageframe, text='Purchase online by Naspas', font=medium_font, fg=blue, variable=r2, value=2, bg="white").grid(row=3, column=0, sticky='W', pady=5)
Radiobutton(secondpageframe, text='Purchase online by VNPay', font=medium_font, fg=blue, variable=r2, value=3, bg="white").grid(row=4, column=0, sticky='W', pady=5)
Radiobutton(secondpageframe, text='Purchase online by MOMO', font=medium_font, fg=blue, variable=r2, value=4, bg="white").grid(row=5, column=0, sticky='W', pady=5)
paymentnextbtn = Button(secondpageframe, font=medium_font, text="Next", fg="white", bg=blue, command=completed)
paymentnextbtn.grid(row=6, column=0, ipadx=15, pady=10)
#Completd Page(3rd Page)
thirdpageframe = LabelFrame(userholderframe, bd=0, bg='white')
#Progress Bar
progress3img = ImageTk.PhotoImage(Image.open('images/completedbar.png').resize((800, 100), Image.ANTIALIAS))
progress3label = Label(thirdpageframe, image=progress3img, bg='white')
progress3label.grid(row=0, column=0)
#Sub head 3 label
subhead3img = ImageTk.PhotoImage(Image.open('images/completedlabel.png').resize((160, 60), Image.ANTIALIAS))
subhead3label = Label(thirdpageframe, image=subhead3img, bg='white')
subhead3label.grid(row=1, column=0, sticky='W', pady=5)
#Component page 3
sucesspurchasedimg = ImageTk.PhotoImage(Image.open('images/successpurchased.png').resize((700, 70), Image.ANTIALIAS))
sucesspurchasedlabel = Label(thirdpageframe, image=sucesspurchasedimg, bg='white')
sucesspurchasedlabel.grid(row=2, column=0, pady=10)
endingpurchasesbtn = Button(thirdpageframe, font=medium_font, text="Back To Home Screen", fg="white", bg=blue, command=homepage)
endingpurchasesbtn.grid(row=3, column=0, pady=10)

#Display Fixed Frame
containerframe.pack(fill=BOTH, expand=YES)
headerframe.pack(fill=X, side=TOP)
blankframe1.pack(fill=X, ipady=17)
menuframe.pack(fill=X)
homebodyframe.pack(fill=X)
footerframe.pack(fill=X, side=BOTTOM)

root.mainloop()
