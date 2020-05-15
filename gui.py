import PySimpleGUI as sg
from autoDL import *

# setup layout for gui
col = [[sg.Text('If you have multiple topics to download separate them with a space', font=("Helvetica", 15))],
[sg.Text('Enter the topics that you want to download', font=("Helvetica", 15))],
[sg.Input()]]

layout = [[sg.Column(col)], [sg.B('Download'), sg.B('Cancel')]]

event, values = sg.Window('ENSC 225 videos to download', layout).read(close=True)

# convert topics to a list from a dictionary
topics = list(values.values())[0].split()
#########################debug#####################
#print(topics)
#print(event)
#########################debug#####################

# Terminate code:
if len(topics) != 0 and event == 'Download':
    autoDL(topics)
else:
    exit(0)
