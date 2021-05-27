from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from datetime import datetime
from requestdata.train_requests import *
from requestdata.ticket_requests import *
from requestdata.route_requests import  *
from requestdata.station_requests import  *
root = Tk()
root.title('Good Job!')
root.geometry('1000x800') #wxh
root.maxsize(width=1200, height=1000)
root.minsize(width=1000, height=700)
#Mystyle MyColor
lightedblue = '#%02x%02x%02x' % (67, 86, 145)
blue = '#%02x%02x%02x' % (42,42,123)
weightedblue = '#%02x%02x%02x' % (0,0,102)
green = '#%02x%02x%02x' % (48, 191, 81)
grey = '#%02x%02x%02x' % (208,208,208)
lightedgrey = '#%02x%02x%02x' % (235, 235, 235)
weightedgrey = '#%02x%02x%02x' % (126, 128, 135)
lightblack = '#%02x%02x%02x' % (42,42,42)
bluegrey = '#%02x%02x%02x' % (125, 137, 181)
large_font = ('Verdana',23)
med_large_font = ('Verdana',17)
medium_font = ('Verdana',15)
small_font = ('Verdana',11)
#Stuff Function
def reduce_list(fields, poplist):
    a = []
    for i in range (len(fields)):
        arrtmp = list(fields[i].values())
        a.append(arrtmp)
    for i in range(0, len(a)):
        count = 0
        for pop in poplist:
            if count==0:
                remove=pop
                a[i].pop(remove)
                count = count + 1
            elif count!=0:
                remove=pop-count
                a[i].pop(remove)
                count = count + 1
    return a
def refresh_list(list):
    for i in range(0, len(list)):
        list.pop()
#Lists
resultlisttrain = reduce_list(get_all_train_info(), poplist=[])
trainsearch = reduce_list(get_all_train(), poplist=[])
customersearch = reduce_list(get_all_ticket(), poplist=[4,5,7,10])
route = reduce_list(get_all_route(), poplist=[])
userseated = []
chosenseat = []
getstation = get_all_station()
idstationlist = []
usertrainid= []
for i in range(0, len(getstation)):
    idstationlist.append(getstation[i]["id"])
print(usertrainid)
getalltrain = get_all_train()
#function homebodyframe/findbodyframe/findseatbodyframe
def homepage():
    findbodyframe.pack_forget()
    findseatbodyframe.pack_forget()
    userinfobodyframe.pack_forget()
    adminbodyframe.pack_forget()
    adminseatcontainerframe.pack_forget()
    firstpageframe.pack()
    secondpageframe.pack_forget()
    thirdpageframe.pack_forget()
    traininfodetailframe.pack_forget()
    homebodyframe.pack(fill=X)
def findtrip():
    homebodyframe.pack_forget()
    findseatbodyframe.pack_forget()
    userinfobodyframe.pack_forget()
    adminbodyframe.pack_forget()
    adminseatcontainerframe.pack_forget()
    firstpageframe.pack()
    secondpageframe.pack_forget()
    thirdpageframe.pack_forget()
    traininfodetailframe.pack_forget()
    trainsearch = reduce_list(get_all_train(), poplist=[])
    refresh_list(chosenseat)
    refresh_list(usertrainid)
    for i in range(0, len(trainsearch)):
        usertrainid.append(trainsearch[i][0])
    trainnamecombobox['values'] = usertrainid
    print(usertrainid)
    trainnamecombobox.grid_forget()
    trainnamecombobox.grid(row=8, column=1, pady=5)
    findbodyframe.pack(fill=X, ipady=50)
def userselecttrainname(event):
    global userseated
    id = trainnamecombobox.current()+1
    tmprecord = get_train_info(id)
    for i in range(0, len(userseatlist)):
        userseatlist[i].config(image=greenimg)
    refresh_list(userseated)
    for i in range (0, len(userseated)):
        userseated.pop()
    userseated = tmprecord['taken_seats']
    print(userseated)
def findseat():
    global userseated
    homebodyframe.pack_forget()
    findbodyframe.pack_forget()
    adminbodyframe.pack_forget()
    traininfodetailframe.pack_forget()
    adminseatcontainerframe.pack_forget()
    btnavailabel(userseated)
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
def usersubmit():
    request = {
    "customer_name": f"{fullnameentry.get()}",
    "customer_id": f"{idpassportentry.get()}",
    "customer_phone": f"{phonenumberentry.get()}",
    "ticket_type": "Return-trip",
    "train_id": trainnamecombobox.get(), #id is int
    "departing_id": startcombobox.get(), #id is int
    "destination_id": desticombobox.get(),    #id is int
    "seat_number": chosenseat # [4,6]
    }
    create_ticket(request)
    def clear_all_user_entry():
        startcombobox.delete(0, END)
        desticombobox.delete(0, END)
        trainnamecombobox.delete(0, END)
        fullnameentry.delete(0, END)
        emailentry.delete(0, END)
        phonenumberentry.delete(0, END)
        idpassportentry.delete(0, END)
        emailconfirmentry.delete(0, END)
    clear_all_user_entry()
    homepage()
def admin():
    homebodyframe.pack_forget()
    findbodyframe.pack_forget()
    findseatbodyframe.pack_forget()
    userinfobodyframe.pack_forget()
    traininfodetailframe.pack_forget()
    adminseatcontainerframe.pack_forget()
    adminbodyframe.pack(fill=X, ipady=150)
def login():
    if usernameloginentry.get() == "admin" and passwordloginentry.get() == 'admin':
        centerframe.destroy()
        sidebarframe.pack(fill=BOTH, side=LEFT)
        dashboarddetailframe.pack(fill=BOTH, expand=YES, side=RIGHT)
        dashboard()
    else:
        erropassLabel.config(text='Wrong Input, Try Again!', bg="red")
traintripimg = ImageTk.PhotoImage(Image.open('images/traintrip.png').resize((240, 171), Image.ANTIALIAS))
def dashboard():
    adminseatcontainerframe.pack_forget()
    traininfodetailframe.pack_forget()
    dashboardbtn.config(bg=weightedblue)
    traininfobtn.config(bg=lightedblue)
    aboutbtn.config(bg=lightedblue)
    dashboarddetailframe.pack(fill=BOTH, expand=YES, side=RIGHT)
    my_canvas.pack(side = LEFT, fill = BOTH, expand = 1)
    my_scrollbar.pack(side = RIGHT, fill = Y)
    #refresh list
    resultlisttrain = reduce_list(get_all_train_info(), poplist=[])
    # Remove unused listtraincurrent
    for index, x in enumerate(listtraincurrent):
        x.frame.pack()
        temp1 = resultlisttrain[index][0]
        temp2 = resultlisttrain[index][2]
        temp3 = resultlisttrain[index][1]
        temp4 = resultlisttrain[index][3]
        x.trainnamelabel.config(text=temp1)
        x.traintimelabel.config(text=temp2)
        x.departlabel.config(text=temp3)
        x.availabel.config(text=temp4)
def adminfindseat(seated):
    my_canvas.pack_forget()
    my_scrollbar.pack_forget()
    for i in range(0, len(adminseatlist)):
        adminseatlist[i].button.config(image=greenimg)
    adminbtnavailabel(seated)
    adminseatcontainerframe.pack(fill=BOTH, expand=YES)
def traininfo():
    adminseatcontainerframe.grid_forget()
    dashboardbtn.config(bg=lightedblue)
    traininfobtn.config(bg=weightedblue)
    aboutbtn.config(bg=lightedblue)
    dashboarddetailframe.pack_forget()
    traininfodetailframe.pack(fill=BOTH, expand=YES, side=RIGHT)
    traintab()
def traintab():
    trainbtn.config(bg=weightedgrey)
    customerbtn.config(bg=bluegrey)
    customerfindingframe.pack_forget()
    trainfindingframe.pack(fill=BOTH, expand=YES)
def newtrain():
    #New Window for Add Train
    newtrainwindow = Tk()
    newtrainwindow.geometry('450x450')  # wxh
    newtrainwindow.resizable(False, False)

    def submitupdatetrain():
        request = {
        "route_id": f"{newroutecombobox.get()}",
        "train_name": f"{newnameentry.get()}",
        "departing_time": f"{newdeparttimeentry.get()}",
        "number_of_seats": 56
        }
        create_train(request)
        newtrainwindow.destroy()
    # Create a Label
    title_label = Label(newtrainwindow, text="Add Train", font=med_large_font)
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Create Main Form To Ente Data
    newnamelabel = Label(newtrainwindow, text="Name", font=medium_font)
    newnamelabel.grid(row=1, column=0, sticky=W, padx=10)

    newroutelabel = Label(newtrainwindow, text="Route", font=medium_font)
    newroutelabel.grid(row=2, column=0, sticky=W, padx=10)
    newdeparttimelabel = Label(newtrainwindow, text="Depature Time", font=medium_font)
    newdeparttimelabel.grid(row=3, column=0, sticky=W, padx=10)
    # Create Entry Boxes
    newnameentry = Entry(newtrainwindow, bd=0, highlightthickness=2, highlightbackground=blue, font=medium_font)
    newnameentry.grid(row=1, column=1, padx=10)
    trainname = StringVar()
    newroutecombobox = ttk.Combobox(newtrainwindow,  width = 18, font=medium_font, textvariable=trainname)
    idroute = []
    for i in range(0, len(route)):
        idroute.append(route[i][0])
    newroutecombobox['values'] = idroute
    newroutecombobox.current(0)
    newroutecombobox.grid(row=2, column=1, pady=5, padx=1)
    newdeparttimeentry = Entry(newtrainwindow, bd=0, highlightthickness=2, highlightbackground = blue, font=medium_font)
    newdeparttimeentry.grid(row=3, column=1, pady=5, padx=10)
    listrouteframe = LabelFrame(newtrainwindow, bg="white")
    listrouteframe.grid(row=4, columnspan=2,pady=10)
    for index, x in enumerate(route):
        rowindex = index + 1
        num = 0
        for y in x:
            route_label = Label(listrouteframe, text=y, bg='white', font=medium_font)
            route_label.grid(row=rowindex, column=num)
            num += 1
    # Create Buttons
    addcustomerbutton = Button(newtrainwindow, text="Submit", font=small_font, bg=green, bd=2, fg="white", command=submitupdatetrain)
    addcustomerbutton.grid(row=5, column=0, padx=10, pady=10, columnspan=2)
def edittrain(index):
    edittrain = Tk()
    edittrain.geometry('400x310')  # wxh
    edittrain.resizable(False, False)
    def trainupdate():
        idtrain = editidentry.get()
        request = {
            "route_id": f"{editrouteentry.get()}",  # Reference Route, use get_all_route
            "train_name": f"{editnameentry.get()}",
            "departing_time": f"{editdeptimeentry.get()}",
            "number_of_seats": 56
        }
        update_train(request, idtrain)
        edittrain.destroy()
    trainsearch = reduce_list(get_all_train(), poplist=[])
    editidlabel = Label(edittrain, text="ID", font=medium_font)
    editidlabel.grid(row=0, column=0, padx=5, pady=10)
    editidentry = Entry(edittrain, font=medium_font)
    editidentry.insert(0, trainsearch[index][0])
    editidentry.grid(row=0, column=1, padx=5, pady=10)
    editnamelabel = Label(edittrain, text="Name", font=medium_font)
    editnamelabel.grid(row=1, column=0, padx=5, pady=10)
    editnameentry = Entry(edittrain, font=medium_font)
    editnameentry.insert(0, trainsearch[index][1])
    editnameentry.grid(row=1, column=1, padx=5, pady=10)
    editroutelabel = Label(edittrain, text="Route", font=medium_font)
    editroutelabel.grid(row=2, column=0, padx=5, pady=10)
    editrouteentry = Entry(edittrain, font=medium_font)
    editrouteentry.insert(0, trainsearch[index][2])
    editrouteentry.grid(row=2, column=1, padx=5, pady=10)
    editdeptimelabel = Label(edittrain, text="Dep. Time", font=medium_font)
    editdeptimelabel.grid(row=3, column=0, padx=5, pady=10)
    editdeptimeentry = Entry(edittrain, font=medium_font)
    editdeptimeentry.insert(0, trainsearch[index][3])
    editdeptimeentry.grid(row=3, column=1, padx=5, pady=10)
    editnoseatlabel = Label(edittrain, text="No. Seat", font=medium_font)
    editnoseatlabel.grid(row=4, column=0, padx=5, pady=10)
    editnoseatentry = Entry(edittrain, font=medium_font)
    editnoseatentry.insert(0, trainsearch[index][4])
    editnoseatentry.grid(row=4, column=1, padx=5, pady=10)
    saveupdatebtn = Button(edittrain, text="Save", bg=green, fg='white', font=medium_font, command=trainupdate)
    saveupdatebtn.grid(row=5, columnspan=2, pady=10)

def listtrain():
    trainsearch = reduce_list(get_all_train(), poplist=[])
    editbtn = []
    for i in range (len(trainsearch)):
        button = Button(traintableframe, text="EDIT" , bg=blue, fg='white', font=small_font,
                    command=lambda: edittrain(i))
        editbtn.append((button))
    for index, x in enumerate(trainsearch):
        rowindex = index + 1
        num = 0
        editbtn[index].grid(row=rowindex, column=5)
        for y in x:
            trainlookup_label = Label(traintableframe, text=y, bg='white', font=medium_font)
            trainlookup_label.grid(row=rowindex, column=num)
            num += 1
def editcustomer(index):
    editcustomer = Tk()
    editcustomer.geometry('420x330')  # wxh
    editcustomer.resizable(False, False)
    def customerupdate():
        idcustomer = editidentry.get()
        allticket = get_all_ticket()
        print(allticket[index])
        request = {
            "customer_name": f"{editnameentry.get()}",
            "customer_id": f"{editpassportentry.get()}",
            "customer_phone": f"{editcontactentry.get()}",
            "ticket_type": "Return-trip",
            "train_id" : allticket[index]['train_id'],
            "departing_id": allticket[index]['departing_id'],
            "destination_id":   allticket[index]['destination_id'],
            "seat_number": editseatentry.get()  # [4,6]
        }
        update_ticket(request, idcustomer)
        editcustomer.destroy()
    #Refresh list
    customersearch = reduce_list(get_all_ticket(), poplist=[4,5,7,10])
    editidlabel = Label(editcustomer, text="ID", font=medium_font)
    editidlabel.grid(row=0, column=0, padx=5, pady=10)
    editidentry = Entry(editcustomer, font=medium_font)
    editidentry.insert(0, customersearch[index][0])
    editidentry.grid(row=0, column=1, padx=5, pady=10)
    editnamelabel = Label(editcustomer, text="Name", font=medium_font)
    editnamelabel.grid(row=1, column=0, padx=5, pady=10)
    editnameentry = Entry(editcustomer, font=medium_font)
    editnameentry.insert(0, customersearch[index][1])
    editnameentry.grid(row=1, column=1, padx=5, pady=10)
    editpassportlabel = Label(editcustomer, text="ID/Passport", font=medium_font)
    editpassportlabel.grid(row=2, column=0, padx=5, pady=10)
    editpassportentry = Entry(editcustomer, font=medium_font)
    editpassportentry.insert(0, customersearch[index][2])
    editpassportentry.grid(row=2, column=1, padx=5, pady=10)
    editcontactlabel = Label(editcustomer, text="Contact", font=medium_font)
    editcontactlabel.grid(row=3, column=0, padx=5, pady=10)
    editcontactentry = Entry(editcustomer, font=medium_font)
    editcontactentry.insert(0, customersearch[index][3])
    editcontactentry.grid(row=3, column=1, padx=5, pady=10)
    editpricelabel = Label(editcustomer, text="Price", font=medium_font)
    editpricelabel.grid(row=4, column=0, padx=5, pady=10)
    editpriceentry = Entry(editcustomer, font=medium_font)
    editpriceentry.insert(0, customersearch[index][4])
    editpriceentry.grid(row=4, column=1, padx=5, pady=10)
    editseatlabel = Label(editcustomer, text="Seat", font=medium_font)
    editseatlabel.grid(row=4, column=0, padx=5, pady=10)
    editseatentry = Entry(editcustomer, font=medium_font)
    editseatentry.insert(0, customersearch[index][5])
    editseatentry.grid(row=4, column=1, padx=5, pady=10)
    saveupdatebtn = Button(editcustomer, text="Save", bg=green, fg='white', font=medium_font, command=customerupdate)
    saveupdatebtn.grid(row=5, columnspan=2, pady=10)
def listcustomer():
    customersearch = reduce_list(get_all_ticket(), poplist=[4, 5, 7, 10])
    editbtn = []
    for i in range(len(customersearch)):
        button = Button(customertableframe, text="EDIT", bg=blue, fg='white', font=small_font,
                      command=lambda: editcustomer(i))
        editbtn.append(button)
    for index, x in enumerate(customersearch):
        rowindex = index + 1
        num = 0
        editbtn[index].grid(row=rowindex, column=7)
        for y in x:
            customerlookup_label = Label(customertableframe, text=y, bg='white', font=medium_font)
            customerlookup_label.grid(row=rowindex, column=num)
            num += 1

def customertab():
    trainbtn.config(bg=bluegrey)
    customerbtn.config(bg=weightedgrey)
    trainfindingframe.pack_forget()
    customerfindingframe.pack(fill=BOTH, expand=YES)
def about():
    adminseatcontainerframe.grid_forget()
    dashboardbtn.config(bg=lightedblue)
    traininfobtn.config(bg=lightedblue)
    aboutbtn.config(bg=weightedblue)
    dashboarddetailframe.pack_forget()
userseatlist = []
def btnavailabel(seated):
    for i in seated:
        userseatlist[i-1].config(image=redimg)
def changecolor(seatno):
    userseatlist[seatno].button.config(image=redimg)
    print(userseatlist[seatno].button.cget("text"))
    chosenseat.append(userseatlist[seatno].button.cget("text"))
adminseatlist = []
def adminbtnavailabel(seated):
    for i in seated:
        adminseatlist[i-1].button.config(image=redimg)
#Container
containerframe = LabelFrame(root, bg=blue)
#Header
headerframe = LabelFrame(containerframe, bg=blue)
brandframe = LabelFrame(headerframe, bd=0, bg=blue)
dateframe = LabelFrame(headerframe, bd=0, bg=blue)
trainbrandlabel = Label(brandframe, text='TRAIN MANAGEMENT SYSTEM', bg=blue, fg='white', font=large_font)
now = datetime.now()
day = datetime.today().strftime('%A')
dt_string = now.strftime(f"{day} %H:%M %d/%m/%Y")
trainbrandlabel2 = Label(dateframe, text=dt_string, bg=blue, fg='white', font=small_font)
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
adminbtn = Button(menuframe, text="Admin", fg='white', font=small_font, bg=blue, bd=2, highlightbackground = "white", command=admin)
#Display Menu
homebtn.grid(row=0, column=0, ipadx=25)
findticketbtn.grid(row=0, column=1, ipadx=25)
reservebtn.grid(row=0, column=2, ipadx=25)
checkticketbtn.grid(row=0, column=3, ipadx=25)
regulationbtn.grid(row=0, column=4, ipadx=25)
guidesbtn.grid(row=0, column=5, ipadx=15)
adminbtn.grid(row=0, column=6, ipadx=25)
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
startlabel = Label(marginframe2, text='Starting Station', font=medium_font, fg=blue, bg=lightedgrey)
startlabel.grid(row=1, column=0, sticky=W, columnspan=3)
startcombobox = ttk.Combobox(marginframe2, font=small_font, value=idstationlist)
startcombobox.grid(row=2, column=0, ipadx=270, ipady=5, columnspan=3)
#Blank Frame 4
findblankframe4 = LabelFrame(marginframe2, bg=lightedgrey, bd=0)
findblankframe4.grid(row=3, column=0, ipady=7, columnspan=3)
#Destination Station
destilabel = Label(marginframe2, text='Destination', font=medium_font, fg=blue, bg=lightedgrey)
destilabel.grid(row=4, column=0, sticky=W, columnspan=3)
desticombobox = ttk.Combobox(marginframe2, font=small_font, value=idstationlist)
desticombobox.grid(row=5, column=0, ipadx=270, ipady=5, columnspan=3)
stationframe = LabelFrame(marginframe2)
stationframe.grid(row=6, column=0, ipady=7, columnspan=3, pady=10)
for i in range(0, len(getstation)):
    stations = str(getstation[i]["id"]) + "." + str(getstation[i]["station_name"])
    stationlabel = Label(stationframe, text=stations, font= medium_font)
    stationlabel.grid(row=i)
#Blank Frame 5
findblankframe5 = LabelFrame(marginframe2, bg=lightedgrey, bd=0)
findblankframe5.grid(row=7, column=0, ipady=7, columnspan=3)
trainamelabel = Label(marginframe2, text="Train", font=medium_font, bg=lightedgrey, fg=blue)
trainamelabel.grid(row=8, column=0, pady=5)
usertrainname = StringVar()
trainnamecombobox = ttk.Combobox(marginframe2, width=18, font=medium_font, textvariable=usertrainname)
trainnamecombobox.bind("<<ComboboxSelected>>", userselecttrainname)
trainnamecombobox.grid(row=8, column=1, pady=5)
trainframe = LabelFrame(marginframe2)
trainframe.grid(row=8, column=2, ipady=7, pady=10)
for i in range(0, len(getalltrain)):
    trains = str(getalltrain[i]["id"]) + "." + str(getalltrain[i]["train_name"])
    trainlabel = Label(trainframe, text=trains, font= medium_font)
    trainlabel.grid(row=i)
#Find Button
submitfindbtn = Button(marginframe2, text="FIND", font=medium_font, fg="white", bg=blue, command=findseat)
submitfindbtn.grid(row=9, ipadx=40, columnspan=3, pady=15)

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
#56 Seats
#Left-Mid-Right Part Frame
seatleftframe = LabelFrame(seatcontainerframe, bd=0, bg=lightedgrey)
seatmidframe = LabelFrame(seatcontainerframe, bd=0, bg=lightedgrey)
seatrightframe = LabelFrame(seatcontainerframe, bd=0, bg=lightedgrey)
seatleftframe.grid(row=0, column=0)
seatmidframe.grid(row=0, column=1)
seatrightframe.grid(row=0, column=2)
#Import Image
greenimg = ImageTk.PhotoImage(Image.open('images/green.png').resize((54, 41), Image.ANTIALIAS))
redimg = ImageTk.PhotoImage(Image.open('images/red.png').resize((54, 41), Image.ANTIALIAS))
barriel = ImageTk.PhotoImage(Image.open('images/barriel.png').resize((40, 90), Image.ANTIALIAS))
#Seat Left Display
class userleftseat():
    def __init__(self, index):
        self.button = Button(seatleftframe, image=greenimg, borderwidth=0, text=i + 1, fg='white', font=medium_font, compound=CENTER, command=lambda: changecolor(index))
for i in range(28):
    button = userleftseat(i)
    userseatlist.append(button)
barriel1label = Label(seatmidframe, image=barriel, bg=lightedgrey, bd=0)
barriel2label = Label(seatmidframe, image=barriel, bg=lightedgrey, bd=0)
barriel1label.pack()
barriel2label.pack()
#Seat Right Display
class userrightseat():
    def __init__(self, index):
        self.button = Button(seatrightframe, image=greenimg, borderwidth=0, text=i + 1, fg='white', font=medium_font, compound=CENTER, command=lambda: changecolor(index))
for i in range(28,56):
    button = userrightseat(i)
    userseatlist.append(button)
#Function Seated Button
def arrange_list(userseatlist, start, end):
    k = 0
    j = 0
    for i in range(start, end):
        userseatlist[i].button.grid(row=i%4, column=j)
        k += 1
        if k == 4:
            j += 1
            k = 0

        if j == 7:
            k = 0
            j = 0
arrange_list(userseatlist, 0, 28)
arrange_list(userseatlist, 28, 56)

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
endingpurchasesbtn = Button(thirdpageframe, font=medium_font, text="Back To Home Screen", fg="white", bg=blue, command=usersubmit)
endingpurchasesbtn.grid(row=3, column=0, pady=10)

#Start Admin Page!!!!!!!!!!!!!!!!
adminbodyframe = LabelFrame(containerframe, bg=grey, bd=0)
#Blank Frame 1
adminblankframe1 = LabelFrame(adminbodyframe, bg=grey, bd=0)
adminblankframe1.pack(fill=X, ipady=20)
#Holder
adminholderframe = LabelFrame(adminbodyframe, bg=grey, bd=0)
adminholderframe.pack(fill=BOTH, expand=YES)
#Blank Frame 2
adminblankframe2 = LabelFrame(adminbodyframe, bg=grey, bd=0)
adminblankframe2.pack(fill=X, ipady=20)
#Login
centerframe = LabelFrame(adminholderframe, bg='white')
centerframe.place(in_=adminholderframe, anchor="c", relx=.5, rely=.45)
labeladmin = Label(centerframe, text='Wellcome to Train Management System!', font=medium_font, bg="white")
labeladmin.grid(row=0, column=0, columnspan=2, padx=20, pady=(100, 0))
usernameloginlabel = Label(centerframe, text="Username", font=medium_font, bg='white')
usernameloginlabel.grid(row=1, column=0, pady=10)
usernameloginentry = Entry(centerframe, width=15, relief=RIDGE, font=medium_font, highlightthickness=1, highlightbackground = "blue")
usernameloginentry.grid(row=1, column=1, pady=10)
passwordloginlabel = Label(centerframe, text="Password", font=medium_font, bg='white')
passwordloginlabel.grid(row=2, column=0, pady=10)
passwordloginentry = Entry(centerframe, width=15, show='*', relief=RIDGE, font=medium_font, highlightthickness=1, highlightbackground = "blue")
passwordloginentry.grid(row=2, column=1, pady=10)
loginButton = Button(centerframe, text="Login", width=10, command=login, font=small_font)
loginButton.grid(row=3, column=0, columnspan=2, pady=10)
erropassLabel = Label(centerframe, text="", bg='white', fg='white', bd=0, font=medium_font)
erropassLabel.grid(row=4, column=0, columnspan=2, pady=10)
#Binding Press Enter to Login
usernameloginentry.bind('<Return>', lambda x:login())
passwordloginentry.bind('<Return>', lambda x:login())

#♥♥ Main Admin Page ♥♥
sidebarframe = LabelFrame(adminholderframe, bd=0, bg=lightedblue, width=150, height=500)
dashboardbtn = Button(sidebarframe, text="Dashboard", fg='white', bg=weightedblue, bd=0, font=med_large_font, command=dashboard)
dashboardbtn.pack(fill=X, pady=10)
traininfobtn = Button(sidebarframe, text="Train Infor", fg='white', bg=lightedblue, bd=0, font=med_large_font, command=traininfo)
traininfobtn.pack(fill=X, pady=10)
aboutbtn = Button(sidebarframe, text="About", fg='white', bg=lightedblue, font=med_large_font, bd=0, command=about)
aboutbtn.pack(fill=X, pady=10)

#Dashboard
dashboarddetailframe = LabelFrame(adminholderframe, bd=0, bg='white', width=850, height=500)
# Create A Canvas
my_canvas = Canvas(dashboarddetailframe, bg='white')
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
# Add A Scrollbar To The Canvas
my_scrollbar = ttk.Scrollbar(dashboarddetailframe, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
# Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
currenttrainframe = LabelFrame(my_canvas, bd=0, bg='white')
# Add that New frame To a Window In The Canvas
my_canvas.create_window((300,0), window=currenttrainframe, anchor="nw")
currenttrainlabel = Label(currenttrainframe, text='Current train running', font=med_large_font, bg='white', fg=blue)
currenttrainlabel.pack()
#Train Current
class Train():
  def __init__(self, index):
    self.frame = LabelFrame(currenttrainframe, bg='white', bd=0)
    self.traintripbtn = Button(self.frame, image=traintripimg, bg='white', bd=0, command=lambda :adminfindseat(resultlisttrain[index][4]))
    self.traintripbtn.pack()
    self.trainnamelabel = Label(self.frame, text='', font=small_font, bg='white')
    self.trainnamelabel.place(x=20, y=5)
    self.traintimelabel = Label(self.frame, text='', font=small_font, bg='white')
    self.traintimelabel.place(x=100, y=5)
    self.departlabel = Label(self.frame, text='', font=small_font, bg='white')
    self.departlabel.place(x=100, y=40)
    self.availabel = Label(self.frame, text='', font=small_font, bg='white')
    self.availabel.place(x=100, y=100)
listtraincurrent = []
for i in range(0, len(resultlisttrain)):
    train = Train(i)
    listtraincurrent.append(train)
#Seat Holder Container Frame
adminseatcontainerframe = LabelFrame(dashboarddetailframe, highlightthickness=2, highlightbackground = blue)
#56 Seats (VERY LAZY THIS PART!!!!)
#Left-Mid-Right Part Frame
adminseatleftframe = LabelFrame(adminseatcontainerframe, bd=0, bg=lightedgrey)
adminseatmidframe = LabelFrame(adminseatcontainerframe, bd=0, bg=lightedgrey)
adminseatrightframe = LabelFrame(adminseatcontainerframe, bd=0, bg=lightedgrey)
adminseatleftframe.grid(row=0, column=0)
adminseatmidframe.grid(row=0, column=1)
adminseatrightframe.grid(row=0, column=2)
class adminleftseat():
    def __init__(self, index):
        self.button = Button(adminseatleftframe, image=greenimg, borderwidth=0, text=i + 1, fg='white', font=medium_font, compound=CENTER)
for i in range(28):
    button = adminleftseat(i)
    adminseatlist.append(button)
class adminrightseat():
    def __init__(self, index):
        self.button = Button(adminseatrightframe, image=greenimg, borderwidth=0, text=i + 1, fg='white', font=medium_font, compound=CENTER)
for i in range(28,56):
    button = adminrightseat(i)
    adminseatlist.append(button)
def arrange_list(adminseatlist, start, end):
    k = 0
    j = 0
    for i in range(start, end):
        adminseatlist[i].button.grid(row=i%4, column=j)
        k += 1
        if k == 4:
            j += 1
            k = 0

        if j == 7:
            k = 0
            j = 0
arrange_list(adminseatlist, 0, 28)
arrange_list(adminseatlist, 28, 56)
#Seat Mid Display
adminbarriel1label = Label(adminseatmidframe, image=barriel, bg=lightedgrey, bd=0)
adminbarriel2label = Label(adminseatmidframe, image=barriel, bg=lightedgrey, bd=0)
adminbarriel1label.pack()
adminbarriel2label.pack()

#Train Info
traininfodetailframe = LabelFrame(adminholderframe, bg='black', width=850, height=500, bd=0)
leftsidebarinfoframe = LabelFrame(traininfodetailframe, bg=bluegrey, width=150, height=500, bd=0)
leftsidebarinfoframe.pack(fill=BOTH, expand=YES, side=LEFT)
rightinfoframe = LabelFrame(traininfodetailframe, bg='red', width=700, height=500, bd=0)
rightinfoframe.pack(fill=BOTH, expand=YES, side=RIGHT)
#Sidebar Info
trainbtn = Button(leftsidebarinfoframe, text="Train", fg="black", bg=bluegrey, bd=0, font=med_large_font, command=traintab)
trainbtn.pack(fill=X, pady=10)
customerbtn = Button(leftsidebarinfoframe, text="Customer", fg='black', bg=bluegrey, bd=0, font=med_large_font, command=customertab)
customerbtn.pack(fill=X, pady=10)
#Train Finding
trainfindingframe = LabelFrame(rightinfoframe, bd=0, bg='white', width=700, height=500)
typeoneormultiplelabel = Label(trainfindingframe, bd=0, bg='white', font=medium_font, text='Type one or multiple information below to for your search')
typeoneormultiplelabel.grid(row=0, column=0, columnspan=4, pady=15)
trainnamelabel = Label(trainfindingframe, bd=0, bg='white', font=small_font, text='Train Name')
trainnamelabel.grid(row=1, column=0, pady=15)
trainnameentry = Entry(trainfindingframe, bd=0, highlightthickness=2, highlightbackground = blue, font=medium_font)
trainnameentry.grid(row=1, column=1, pady=15)
routelabel = Label (trainfindingframe, bd=0, bg='white', font=small_font, text='Route')
routelabel.grid(row=1, column=2, padx=(20,0))
routeentry = Entry(trainfindingframe, bd=0, highlightthickness=2, highlightbackground = blue, font=medium_font)
routeentry.grid(row=1, column=3, pady=15)
confirmfindbtn = Button(trainfindingframe, text='CONFIRM', font=small_font, width=15, bg=lightedblue, bd=2, fg="white", command=listtrain)
confirmfindbtn.grid(row=2, column=0, columnspan=2, pady=15)
newtrainbtn = Button(trainfindingframe, text='NEW TRAIN', font=small_font, width=15, bg=green, bd=2, fg="white", command=newtrain)
newtrainbtn.grid(row=2, column=3, columnspan=2, pady=15)
#Train Table Frame
traintableframe = LabelFrame(trainfindingframe, bd=2, bg='white', highlightthickness=3, highlightbackground = "black")
traintableframe.grid(row=3, columnspan=4)
traintableimg = ImageTk.PhotoImage(Image.open('images/traintable.png').resize((650,45), Image.ANTIALIAS))
columntablelabel = Label(traintableframe, image=traintableimg, bg='white', bd=0)
columntablelabel.grid(row=0, column=0, columnspan=6)

#Customer Finding
customerfindingframe = LabelFrame(rightinfoframe, bd=0, bg='white', width=700, height=500)
typeoneormultiplelabel = Label(customerfindingframe, bd=0, bg='white', font=medium_font, text='Type one or multiple information below to for your search')
typeoneormultiplelabel.grid(row=0, column=0, columnspan=4, pady=15)
customernamelabel = Label(customerfindingframe, bd=0, bg='white', font=small_font, text='Name')
customernamelabel.grid(row=1, column=0, pady=15)
customernameentry = Entry(customerfindingframe, bd=0, highlightthickness=2, highlightbackground = blue, font=medium_font)
customernameentry.grid(row=1, column=1, pady=15)
customeridlabel = Label (customerfindingframe, bd=0, bg='white', font=small_font, text='ID/Passport')
customeridlabel.grid(row=1, column=2, padx=(20,0))
customeridentry = Entry(customerfindingframe, bd=0, highlightthickness=2, highlightbackground = blue, font=medium_font)
customeridentry.grid(row=1, column=3, pady=15)
customerconfirmfindbtn = Button(customerfindingframe, text='CONFIRM', font=small_font, width=15, bg=lightedblue, bd=2, fg="white", command=listcustomer)
customerconfirmfindbtn.grid(row=2, column=0, columnspan=2, pady=15)
#Customer Table Frame
customertableframe = LabelFrame(customerfindingframe, bd=2, bg='white', highlightthickness=3, highlightbackground = "black")
customertableframe.grid(row=3, columnspan=4)
customertableimg = ImageTk.PhotoImage(Image.open('images/customertable.png').resize((650,45), Image.ANTIALIAS))
customercolumntablelabel = Label(customertableframe, image=customertableimg, bg='white', bd=0)
customercolumntablelabel.grid(row=0, column=0, columnspan=8)

#Display Fixed Frame
containerframe.pack(fill=BOTH, expand=YES)
headerframe.pack(fill=X, side=TOP)
blankframe1.pack(fill=X, ipady=17)
menuframe.pack(fill=X)
homebodyframe.pack(fill=X)
footerframe.pack(fill=X, side=BOTTOM)

root.mainloop()
