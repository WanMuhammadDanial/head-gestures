import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

title_v ='Custom Title'
state = 0
# State Value
# 0 - main_menu
# 1 - living_room
# 2 - toilet
# 3 - kitchen
# 4 - master_bedroom
# 9 - confirmation 

living_room_count = 0
toilet_count = 0
kitchen_count = 0
master_bedroom_count = 0

#==============================Object Logic START============================
# Object structure, Room (object) with keys of appliance and status (on or off)
class Empty:
    pass

living_room = Empty()
living_room.fan = 0
living_room.tv = 0
living_room.light = 0
living_room.ac = 0

toilet = Empty()
toilet.fan = 1
toilet.tv = 0
toilet.light = 0
toilet.slides = 0

kitchen = Empty()
kitchen.fan = 1
kitchen.tv = 1
kitchen.light = 1
kitchen.slides = 0

master_bedroom = Empty()
master_bedroom.fan = 1
master_bedroom.tv = 1
master_bedroom.light = 1
master_bedroom.slides = 1

#counting total number of appliances that are on/active
def getCount (object, abb):
    global living_room_count, toilet_count, kitchen_count, master_bedroom_count
    if(abb == 'li'):
        living_room_count = 0
    elif(abb == 't'):
        toilet_count = 0
    elif(abb == 'k'):
        kitchen_count = 0
    elif(abb == 'mb'):
        master_bedroom_count = 0
    for attr, value in vars(object).items():
        #print('attr ' + str(attr) + " value " + str(value))
        if(value == 1):
            if(abb == 'li'):
                living_room_count = living_room_count + 1
            elif(abb == 't'):
                toilet_count = toilet_count + 1
            elif(abb == 'k'):
                kitchen_count = kitchen_count + 1
            elif(abb == 'mb'):
                master_bedroom_count = master_bedroom_count + 1

def resetRoom (object, abb):
    global living_room_count, toilet_count, kitchen_count, master_bedroom_count
    for attr, value in vars(object).items():
        if(value == 1):
            setattr(object,attr,0)



getCount(living_room,'li')
getCount(toilet,'t')
getCount(kitchen,'k')
getCount(master_bedroom,'mb')
    

#==============================Object Logic END============================

#==============================UI Logic START============================


# dpg.create_context()
# dpg.create_viewport(title=title_v, width=600, height=600)

# demo.show_demo()

# dpg.setup_dearpygui()
# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()

dpg.create_context()

with dpg.window(label="Example Window", width=300):
    dpg.add_text("Main Menu")
    dpg.add_button(label="Living Room")
    with dpg.group(horizontal = True):
        dpg.add_button(label="Kitchen")
        dpg.add_button(label="Toilet")
    dpg.add_button(label="Master Bedroom")
    # dpg.add_input_text(label="string", default_value="Quick brown fox")
    # dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

dpg.create_viewport(title='Custom Title', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()

# below replaces, start_dearpygui()
while dpg.is_dearpygui_running():
    # insert here any code you would like to run in the render loop
    # you can manually stop by using stop_dearpygui()
    print("this will run every frame")
    dpg.render_dearpygui_frame()

dpg.destroy_context()

# def startUI():
#     dpg.create_context()

#     with dpg.window(label="Example Window"):
#         dpg.add_text("Hello, world")
#         dpg.add_button(label="Save")
#         dpg.add_input_text(label="string", default_value="Quick brown fox")
#         dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

#     dpg.create_viewport(title='Custom Title', width=600, height=200)
#     dpg.setup_dearpygui()
#     dpg.show_viewport()

#     # below replaces, start_dearpygui()
#     while dpg.is_dearpygui_running():
#         # insert here any code you would like to run in the render loop
#         # you can manually stop by using stop_dearpygui()
#         print("this will run every frame")
#         dpg.render_dearpygui_frame()

#     #dpg.destroy_context()

# def stopUI():
#     dpg.destroy_context()



#==============================UI Logic END============================

