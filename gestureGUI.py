import tkinter as tk
import gestureData as gd

# Sample data array
data = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

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



def initialize_data():
    fill_top_data(gd.firstPageData[0])
    fill_right_data(gd.firstPageData[1])
    fill_bottom_data(gd.firstPageData[2])
    fill_left_data(gd.firstPageData[3])

initialize_data()

def button_click(row, col):
    print(f"Button clicked: Row {row}, Column {col}, Data: {data[row][col]}")

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

# Start the Tkinter event loop
window.mainloop()
