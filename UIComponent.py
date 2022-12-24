import tkinter as tk 
import tkinter.messagebox as tkmsgbox

# 4 rooms
# keep track of number of appliances that are on at the moment
# conformation screen
# track of each item


class MainUI():
    def __init__(self):
        self.room = [
            {
                'name':'Main'
            },
            {
                'name':'toilet',
                'totalON':0,
                'fan':0,
                'lights':0,
                'tv':0,
                'aircond':0,
            },
            {
                'name':'kitchen',
                'totalON':0,
                'fan':0,
                'lights':0,
                'tv':0,
                'aircond':0,
            },
            {
                'name':'bedroom',
                'totalON':0,
                'fan':0,
                'lights':0,
                'tv':0,
                'aircond':0,
            },
            {
                'name':'hall',
                'totalON':0,
                'fan':0,
                'lights':0,
                'tv':0,
                'aircond':0,
            },
        ]
        self.location = 0
        # self.btn1
        # self.btn2
        # self.btn3
        # self.btn4
        mainPadding = 30
        subPadding = 70


        self.root = tk.Tk()

        self.root.geometry("500x500")
        self.root.title("Test")

        self.label = tk.Label(self.root, text="Gesture Detection", font=('Arial', 18))
        self.label.place(x=0)
        self.label.pack()

        self.buttonFrame = tk.Frame(self.root)
        self.buttonFrame.columnconfigure(0, weight=1)
        self.buttonFrame.columnconfigure(1, weight=1)
        self.buttonFrame.columnconfigure(2, weight=1)
        self.buttonFrame.columnconfigure(3, weight=1)
        self.buttonFrame.columnconfigure(4, weight=1)

        self.btn1 = tk.Button(self.buttonFrame, text='', font=('Arial',18), command=self.buttonUp)
        self.btn1.grid(row=0, column=2, pady=mainPadding)
        self.btn2 = tk.Button(self.buttonFrame,  text='', font=('Arial',18), command=self.buttonLeft)
        self.btn2.grid(row=2, column=0, pady=mainPadding)
        self.btn3 = tk.Button(self.buttonFrame, text='', font=('Arial',18), command=self.buttonRight)
        self.btn3.grid(row=2, column=4, pady=mainPadding)
        self.btn4 = tk.Button(self.buttonFrame, text='', font=('Arial',18),  command=self.buttonDown)
        self.btn4.grid(row=4, column=2, pady=mainPadding)

        self.buttonFrame.pack(fill='x')

   
    #if location 0, user in main hall, else in some other room

    # global btn1, btn2, btn3, btn4, location, room
    
    # location = 0


    def assignDefaultName(self):
        self.btn1.config(text=self.room[1]['name'])
        self.btn2.config(text=self.room[2]['name'])
        self.btn3.config(text=self.room[3]['name'])
        self.btn4.config(text=self.room[4]['name'])

    # def assignApplianceName(self):
    #     btn1.config(text='fan')
    #     btn2.config(text='lights')
    #     btn3.config(text='tv')
    #     btn4.config(text='aircond')

    # def buttonPress(self,button):
    #     if button == 'exit':
    #         self.assignDefaultName()
    #     elif location == 0:
    #         if button == 'up':
    #             location = room[1]['name']
    #             self.assignApplianceName()
    #         elif button == 'down':
    #             location = room[2]['name']
    #             self.assignApplianceName()
    #         elif button == 'left':
    #             location = room[3]['name']
    #             self.assignApplianceName()
    #         elif button == 'right':
    #             location = room[4]['name']
    #             self.assignApplianceName()
        # else:

    def buttonExit(self):
        self.btn1.config(text='fan')
        self.btn2.config(text='lights')
        self.btn3.config(text='tv')
        self.btn4.config(text='aircond')

    def buttonUp(self):
        # global location
        # self.buttonPress('up')
        if self.location == 0:
            self.btn1.config(text='fan')
            self.btn2.config(text='lights')
            self.btn3.config(text='tv')
            self.btn4.config(text='aircond')
            self.location = 1
        else:
            tkmsgbox.showinfo("Confirmation",  "Are you sure you want to switch on Fan for " + self.room[self.location]['name'] + '?')
    
    def buttonLeft(self):
        # self.buttonPress('left')
        # global location
        if self.location == 0:
            self.btn1.config(text='fan')
            self.btn2.config(text='lights')
            self.btn3.config(text='tv')
            self.btn4.config(text='aircond')
            self.location = 2
        else:
            tkmsgbox.showinfo("Confirmation",  "Are you sure you want to switch on Fan for " + self.room[self.location]['name'] + '?')

    def buttonRight(self):
        # self.buttonPress('right')
        # global location
        if self.location == 0:
            self.btn1.config(text='fan')
            self.btn2.config(text='lights')
            self.btn3.config(text='tv')
            self.btn4.config(text='aircond')
            self.location = 3
        else:
            tkmsgbox.showinfo("Confirmation",  "Are you sure you want to switch on Fan for " + self.room[self.location]['name'] + '?')

    def buttonDown(self):
        # self.buttonPress('down')
        # global self.location
        if self.location == 0:
            self.btn1.config(text='fan')
            self.btn2.config(text='lights')
            self.btn3.config(text='tv')
            self.btn4.config(text='aircond')
            self.location = 4
        else:
            tkmsgbox.showinfo("Confirmation",  "Are you sure you want to switch on Fan for " + self.room[self.location]['name'] + '?')
     

    assignDefaultName()
    self.root.mainloop()
    

    

    


    

    

    # BUTTON INITIALIZATOIN
    # btn1.grid(row=0, column=2, sticky=tk.W+tk.E)
    # btn1 = tk.Button(buttonFrame, text='', font=('Arial',18), command=buttonUp)
    # btn1.grid(row=0, column=2, pady=mainPadding)
    # btn2 = tk.Button(buttonFrame,  text='', font=('Arial',18), command=buttonLeft)
    # btn2.grid(row=2, column=0, pady=mainPadding)
    # btn3 = tk.Button(buttonFrame, text='', font=('Arial',18), command=buttonRight)
    # btn3.grid(row=2, column=4, pady=mainPadding)
    # btn4 = tk.Button(buttonFrame, text='', font=('Arial',18),  command=buttonDown)
    # btn4.grid(row=4, column=2, pady=mainPadding)


    

   


    







