import tkinter as tk
import gestureData as gd

data = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
buttons = []
room = 1
switchedOnAppl = 0

def fill_top_data(item):
    global data
    data[0][1] = item
def fill_left_data(item):
    global data
    data[1][0] = item
def fill_bottom_data(item):
    global data
    data[2][1] = item
def fill_right_data(item):
    global data
    data[1][2] = item

def close_window():
    window.destroy()

def switchOnAppl():
    global switchedOnAppl
    switchedOnAppl = switchedOnAppl + 1

def switchOffAppl():
    global switchedOnAppl
    if(switchedOnAppl > 0): switchedOnAppl = switchedOnAppl - 1

def button_click(row, col):
    global data
    if (room == 1):
        print('access first page')
        access_second_page(data[row][col])
    if (room == 2):
        if(data[row][col]=='cancel'):
            reset_data()
        # else:


def access_second_page(data):
    global room
    room = 2
    secondRoomData = gd.secondPageData[data]
    secondRoomItems = []
    for key, value in secondRoomData.items():
        secondRoomItems.append(key)
    update_button_names(
        secondRoomItems[0],
        secondRoomItems[1],
        secondRoomItems[2],
        secondRoomItems[3],
        )


def update_button_names(top,right,bottom,left):
    global buttons
    fill_top_data(top)
    fill_right_data(right)
    fill_bottom_data(bottom)
    fill_left_data(left)
    # 0 = top, 1 = left, 2 = right, 3 = bottom
    for counter, button in enumerate(buttons, start=0):
        if(counter == 0 ): button.configure(text=top)
        if(counter == 2 ): button.configure(text=right)
        if(counter == 3 ): button.configure(text=bottom)
        if(counter == 1 ): button.configure(text=left)

def reset_data():
    global buttons
    global room 
    room = 1
    # 0 = top, 1 = left, 2 = right, 3 = bottom
    fill_top_data(gd.firstPageData[0])
    fill_right_data(gd.firstPageData[1])
    fill_bottom_data(gd.firstPageData[2])
    fill_left_data(gd.firstPageData[3])
    for counter, button in enumerate(buttons, start=0):
        if(counter == 0 ): button.configure(text=gd.firstPageData[0])
        if(counter == 2 ): button.configure(text=gd.firstPageData[1])
        if(counter == 3 ): button.configure(text=gd.firstPageData[2])
        if(counter == 1 ): button.configure(text=gd.firstPageData[3])

reset_data()
window = tk.Tk()
window.title("Head Gesture") 

for i in range(3):
    window.grid_rowconfigure(i, minsize=10)  
    window.grid_columnconfigure(i, minsize=10)  

    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=10, pady=10)

        # Add buttons at specific positions with data from the array
        if (i, j) in [(0, 1), (1, 0), (1, 2), (2, 1)]:
            button = tk.Button(
                master=frame,
                text=data[i][j],  # Set button text from the data array
                command=lambda row=i, col=j: button_click(row, col)
            )
            button.pack(fill=tk.BOTH, expand=True)
            buttons.append(button)
reset_data()
print(buttons)

# Start the Tkinter event loop
window.mainloop()
