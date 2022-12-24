import tkinter as tk 
import tkinter.messagebox as tkmsgbox

# 4 rooms
# keep track of number of appliances that are on at the moment
# conformation screen
# track of each item


class MainUI():
    # def __init__(self):
    #     room = [
    #         {
    #             'name':'Main'
    #         },
    #         {
    #             'name':'toilet',
    #             'totalON':0,
    #             'fan':0,
    #             'lights':0,
    #             'tv':0,
    #             'aircond':0,
    #         },
    #         {
    #             'name':'kitchen',
    #             'totalON':0,
    #             'fan':0,
    #             'lights':0,
    #             'tv':0,
    #             'aircond':0,
    #         },
    #         {
    #             'name':'bedroom',
    #             'totalON':0,
    #             'fan':0,
    #             'lights':0,
    #             'tv':0,
    #             'aircond':0,
    #         },
    #         {
    #             'name':'hall',
    #             'totalON':0,
    #             'fan':0,
    #             'lights':0,
    #             'tv':0,
    #             'aircond':0,
    #         },
    #     ]
    #     location = 0

    root = tk.Tk()

    root.geometry("500x500")
    root.title("Test")
    #if location 0, user in main hall, else in some other room

    global btn1, btn2, btn3, btn4, location, room
    
    location = 0

    room = [
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

    

    def assignDefaultName():
        btn1.config(text=room[1]['name'])
        btn2.config(text=room[2]['name'])
        btn3.config(text=room[3]['name'])
        btn4.config(text=room[4]['name'])

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

    def buttonExit():
        btn1.config(text='fan')
        btn2.config(text='lights')
        btn3.config(text='tv')
        btn4.config(text='aircond')

    def buttonUp():
        global location
        # self.buttonPress('up')
        if location == 0:
            btn1.config(text='fan')
            btn2.config(text='lights')
            btn3.config(text='tv')
            btn4.config(text='aircond')
            location = 1
        else:
            tkmsgbox.showinfo("Confirmation",  "Are you sure you want to switch on Fan for " + room[location]['name'] + '?')
    
    def buttonLeft():
        # self.buttonPress('left')
        global location
        if location == 0:
            btn1.config(text='fan')
            btn2.config(text='lights')
            btn3.config(text='tv')
            btn4.config(text='aircond')
            location = 2
        else:
            tkmsgbox.showinfo("Confirmation",  "Are you sure you want to switch on Fan for " + room[location]['name'] + '?')

    def buttonRight():
        # self.buttonPress('right')
        global location
        if location == 0:
            btn1.config(text='fan')
            btn2.config(text='lights')
            btn3.config(text='tv')
            btn4.config(text='aircond')
            location = 3
        else:
            tkmsgbox.showinfo("Confirmation",  "Are you sure you want to switch on Fan for " + room[location]['name'] + '?')

    def buttonDown():
        # self.buttonPress('down')
        global location
        if location == 0:
            btn1.config(text='fan')
            btn2.config(text='lights')
            btn3.config(text='tv')
            btn4.config(text='aircond')
            location = 4
        else:
            tkmsgbox.showinfo("Confirmation",  "Are you sure you want to switch on Fan for " + room[location]['name'] + '?')
     

    

    label = tk.Label(root, text="Gesture Detection", font=('Arial', 18))
    label.place(x=0)
    label.pack()

    buttonFrame = tk.Frame(root)
    buttonFrame.columnconfigure(0, weight=1)
    buttonFrame.columnconfigure(1, weight=1)
    buttonFrame.columnconfigure(2, weight=1)
    buttonFrame.columnconfigure(3, weight=1)
    buttonFrame.columnconfigure(4, weight=1)


    mainPadding = 30
    subPadding = 70

    top_btn_txt =  ''
    bottom_btn_txt =''
    right_btn_txt = ''
    left_btn__txt = ''

    # BUTTON INITIALIZATOIN
    # btn1.grid(row=0, column=2, sticky=tk.W+tk.E)
    btn1 = tk.Button(buttonFrame, text='', font=('Arial',18), command=buttonUp)
    btn1.grid(row=0, column=2, pady=mainPadding)
    btn2 = tk.Button(buttonFrame,  text='', font=('Arial',18), command=buttonLeft)
    btn2.grid(row=2, column=0, pady=mainPadding)
    btn3 = tk.Button(buttonFrame, text='', font=('Arial',18), command=buttonRight)
    btn3.grid(row=2, column=4, pady=mainPadding)
    btn4 = tk.Button(buttonFrame, text='', font=('Arial',18),  command=buttonDown)
    btn4.grid(row=4, column=2, pady=mainPadding)


    buttonFrame.pack(fill='x')

    assignDefaultName()
    root.mainloop()






ui = MainUI
    







