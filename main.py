from tkinter import *
from tkinter import messagebox as msg
#from KEEpydb import KEEpydb
from PIL import ImageTk, Image

class All_FUNCTION:
    def about(self):
       print("rajat")
    def ITEMS(self):
        #msg.showinfo('INFO','This is RAJAT\'s BAKERY')

        print('\titems\n')
        product=self.items.keys()
        for i in product:
            print(i+'\t'+str(self.items[i][0])+'\t'+str(self.items[i][1]))


    
        

class Main(All_FUNCTION):
    def __init__(self,root):
        self.yellow='white'
        self.height='500'
        self.width='500'
        self.root=root
        self.root.geometry('500x500')
        self.root.config(bg=self.yellow)
        self.root.title('rajat')
        #database initialise
        self.query=KEEpydb.query('bakeryshop','rajat','rajat@143')
        
        #load items
        self.img=ImageTk.PhotoImage(Image.open('bakeryimg\\rajat.jpg').resize((800,700), Image.ANTIALIAS))
        self.items={
            "white forest1 kg": [10,400],
            "black forest1 kg": [10,350],

            "pinp cake250 gm":  [10,250],
            "butter scotch250 gm  ":[10,250],
            "chocolate250 gm ": [10,200],
            "antique4 lts":  [10,862],
            "antique1 lts":    [20,223],
            "shyne20 lts":      [10,2411],
            "shyne10 lts":      [10,1273],
            "shyne4 lts":     [10,546],
            "shyne1 lts":      [25,144],
            "classic20 lts":    [15,1857],
            "classic10 lts":    [10,979],
            "classic4 lts":    [12,424],
            "classic1 lts":    [14,114]}

        self.home()
        
    def home(self):
        frame=Frame(self.root,width=self.width,
                    height=self.height,bg='white').place(x=0,y=0)
        a=Label(frame,image=self.img)
        a.image=self.img
        a.place(x=-100,y=-100)
        Label(frame,text='SRI GANESH BAKERY  !',font='verdana 20 bold',bg=self.yellow).place(x=20,y=70)
        Button(frame,text='  ABOUT',bg='white',padx=50,command=self.about).place(x=50,y=150)
        Button(frame,text='BUY',bg='white',padx=60,command=self.showitems).place(x=50,y=190)
        Button(frame,text='ITEMS',bg='white',padx=54,command=self.showitems).place(x=50,y=230)
        Button(frame,text='PAYMENT',bg='white',padx=45).place(x=50,y=270)
        Button(frame,text='CUSTOMER DETAILS',bg='white',padx=20).place(x=50,y=310)
        Button(frame,text='EXIT',bg='white',padx=57).place(x=50,y=350)
        
    def showitems(self):
        self.img=ImageTk.PhotoImage(Image.open('bakeryimg\\i.jpg').resize((800,700), Image.ANTIALIAS))
        frame=Frame(self.root,width=self.width,
                    height=self.height,bg='white').place(x=0,y=0)
        l=Listbox(frame)
        Label(frame,text='Select Items',font='verdana 15 bold',bg='white',fg='grey50').place(x=20,y=20)
        l.place(x=20,y=60,width=200,height=400)
        for i in self.items.keys():
            l.insert(END,i)

        Button(frame,text='Add TO Cart',bg='yellow').place(x=300,y=50,width=100)
        Button(frame,text='Next',bg='yellow',command=self.bookings).place(x=300,y=80,width=100)
    
    def bookings(self):
        frame=Frame(self.root,width=self.width,
                    height=self.height,bg='white').place(x=0,y=0)
        Button(frame,text='back',bg='red',command=self.home).place(x=20,y=475)
        Label(frame,text='Booking Screen',font='verdana 15 bold',bg='white',fg='grey50').place(x=20,y=20)
        name=StringVar()
        address=StringVar()
        number=StringVar()
        a1=Entry(frame,textvariable=name)
        a1.place(x=20,y=100)
        a2=Entry(frame,textvariable=address)
        a2.place(x=20,y=100+50)
        a3=Entry(frame,textvariable=number)
        a3.place(x=20,y=100+100)
        
        name.set('name')
        address.set('address')
        number.set('number')

        a1.bind('<Button-1>',lambda e:name.set(''))
        a2.bind('<Button-1>',lambda e:address.set(''))
        a3.bind('<Button-1>',lambda e:number.set(''))

        Button(frame,text='Submit').place(x=20,y=445)
        
        
if __name__=='__main__':
    root=Tk()
    Main(root)
    root.mainloop()
