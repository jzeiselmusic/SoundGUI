from soundgui_helpers import *
import PySimpleGUI as sg

#################################
sg.theme('Reddit')

number_rows = 1
layout = makewindow(number_rows)


window = sg.Window("Master",layout)
error = "window was terminated"
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "add_row":
        if number_rows < 13:
            layout = makewindow(number_rows)
            window1 = window
            window = sg.Window("Master",layout)
            window1.close()
            number_rows += 1
    elif event == "stop_1":
        try:
            play_obj1.stop()
        except:
            pass
    elif event == "stop_2":
        try:
            play_obj2.stop()
        except:
            pass
    elif event == "stop_3":
        try:
            play_obj3.stop()
        except:
            pass
    elif event == "stop_4":
        try:
            play_obj4.stop()
        except:
            pass
    elif event == "stop_5":
        try:
            play_obj5.stop()
        except:
            pass
    elif event == "stop_6":
        try:
            play_obj6.stop()
        except:
            pass
    elif event == "stop_7":
        try:
            play_obj7.stop()
        except:
            pass
    elif event == "stop_8":
        try:
            play_obj8.stop()
        except:
            pass
    elif event == "stop_9":
        try:
            play_obj9.stop()
        except:
            pass
    elif event == "stop_10":
        try:
            play_obj10.stop()
        except:
            pass
    elif event == "stop_11":
        try:
            play_obj11.stop()
        except:
            pass
    elif event == "stop_12":
        try:
            play_obj12.stop()
        except:
            pass
    elif event == "play_1":
        play_obj1 = ifplaypressed(1,values)
    elif event == "play_2":
        play_obj2 = ifplaypressed(2,values)
    elif event == "play_3":
        play_obj3 = ifplaypressed(3,values)
    elif event == "play_4":
        play_obj4 = ifplaypressed(4,values)
    elif event == "play_5":
        play_obj5 = ifplaypressed(5,values)
    elif event == "play_6":
        play_obj6 = ifplaypressed(6,values)
    elif event == "play_7":
        play_obj7 = ifplaypressed(7,values)
    elif event == "play_8":
        play_obj8 = ifplaypressed(8,values)
    elif event == "play_9":
        play_obj9 = ifplaypressed(9,values)
    elif event == "play_10":
        play_obj10 = ifplaypressed(10,values)
    elif event == "play_11":
        play_obj11 = ifplaypressed(11,values)
    elif event == "play_12":
        play_obj12 = ifplaypressed(12,values)
		
window.close()
print(error)
