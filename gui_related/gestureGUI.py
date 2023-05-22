import tkinter as tk
import gestureData as gd

#================================================== Variable Initialization START ==================================================

data = [
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
buttons = [] # 0 = top, 1 = left, 2 = right, 3 = bottom
room = 1
switchedOnAppl = 0
roomTitle = ''
secondRoomNames = gd.secondPageData
secondRoomItems = []
secondRoomValues = []

#================================================== Variable Initialization END ==================================================

#================================================== Function Initialization START ==================================================
def set_top_data(item):
    global data
    data[1][1] = item
def set_right_data(item):
    global data
    data[2][2] = item
def set_bottom_data(item):
    global data
    data[3][1] = item
def set_left_data(item):
    global data
    data[2][0] = item

def close_window():
    window.destroy()

def switchOn():
    global switchedOnAppl
    switchedOnAppl = switchedOnAppl + 1
    update_bottom_text()

def switchOff():
    global switchedOnAppl
    if(switchedOnAppl > 0): switchedOnAppl = switchedOnAppl - 1
    update_bottom_text()

def update_top_text(new_text):
    global roomTitle
    roomTitle = new_text
    top_text.config(text=new_text)

def update_bottom_text():
    global switchedOnAppl
    new_text = f"Number of switched on Appliance: {switchedOnAppl}"
    bottom_text.config(text=new_text)

def access_second_page(data):
    global room,secondRoomNames, secondRoomItems, secondRoomValues
    update_top_text(data)
    
    secondRoomData = secondRoomNames[data]
    
    for key, value in secondRoomData.items():
        secondRoomItems.append(key)
        secondRoomValues.append(value)
    update_all_button_names(
        secondRoomItems[0],
        secondRoomValues[0],
        secondRoomItems[1],
        secondRoomValues[1],
        secondRoomItems[2],
        secondRoomValues[2],
        secondRoomItems[3],
        secondRoomValues[3],
        )
    room = 2

def update_second_page():
    global room,secondRoomNames, secondRoomItems, secondRoomValues

def update_button_status(row, col, item, status):
    if(room == 2):
        if(row == 1 and col == 1): buttons[0].configure(text=f"{item}: {status}")
        elif(row == 2 and col == 2 ): buttons[2].configure(text=f"{item}: {status}")
        elif(row == 3 and col == 1 ): buttons[3].configure(text=f"{item}: {status}")
        elif(row == 2 and col == 0 ): buttons[1].configure(text=f"{item}: {status}")


def update_all_button_names(top,v_top,right,v_right,bottom,v_bottom,left,v_left):
    global buttons
    global data
    set_top_data(top)
    set_right_data(right)
    set_bottom_data(bottom)
    set_left_data(left)
    # 0 = top, 1 = left, 2 = right, 3 = bottom
    for counter, button in enumerate(buttons, start=0):
        if(counter == 0 ): button.configure(text=f"{top}: {v_top}")
        if(counter == 2 ): button.configure(text=f"{right}: {v_right}")
        if(counter == 3 ): button.configure(text=f"{bottom}")
        if(counter == 1 ): button.configure(text=f"{left}: {v_left}")

def reset_data():
    global buttons
    global room 
    update_top_text('Main Menu')
    room = 1
    # 0 = top, 1 = left, 2 = right, 3 = bottom
    set_top_data(gd.firstPageData[0])
    set_right_data(gd.firstPageData[1])
    set_bottom_data(gd.firstPageData[2])
    set_left_data(gd.firstPageData[3])
    for counter, button in enumerate(buttons, start=0):
        if(counter == 0 ): button.configure(text=gd.firstPageData[0])
        if(counter == 2 ): button.configure(text=gd.firstPageData[1])
        if(counter == 3 ): button.configure(text=gd.firstPageData[2])
        if(counter == 1 ): button.configure(text=gd.firstPageData[3])

def button_click(row, col):
    global data, secondRoomNames
    if (room == 1):
        access_second_page(data[row][col])
    elif (room == 2):
        if(data[row][col]=='cancel'):
            reset_data()
        else:
            if(secondRoomNames[roomTitle][data[row][col]] == 'off'):
                secondRoomNames[roomTitle][data[row][col]] = 'on'
                update_button_status(row,col,data[row][col],secondRoomNames[roomTitle][data[row][col]])
                switchOn()
            elif(secondRoomNames[roomTitle][data[row][col]] == 'on'):
                secondRoomNames[roomTitle][data[row][col]] = 'off'
                update_button_status(row,col,data[row][col],secondRoomNames[roomTitle][data[row][col]])
                switchOff()

#================================================== Function Initialization END ==================================================

#================================================== Code Execution START ==================================================

window = tk.Tk()
window.title("Head Gesture") 

top_text = tk.Label(window, font=("Arial", 16), justify="center", anchor="center")
top_text.grid(row=0, column=1)

bottom_text = tk.Label(window,text= 'Number of switched on Appliance: 0', font=("Arial", 12), justify="center", anchor="center")
bottom_text.grid(row=4, column=1)

for i in range(5):
    window.grid_rowconfigure(i, minsize=10)  
    window.grid_columnconfigure(i, minsize=10)  


    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=10, pady=10)

        # if(i == 0 and j == 1):
            

        if (i, j) in [(1, 1), (2, 0), (2, 2), (3, 1)]:
            button = tk.Button(
                master=frame,
                text=data[i][j],  
                command=lambda row=i, col=j: button_click(row, col)
            )
            button.pack(fill=tk.BOTH, expand=True)
            buttons.append(button)

reset_data()

# Start the Tkinter event loop
window.mainloop()
