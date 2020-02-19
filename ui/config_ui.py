import PySimpleGUI as sg
import yaml
from utilities.helpers import load_config

#TODO write config changes back to config file

def config_ui():
    cfg = load_config()
    
    layout = []
    for k, v in cfg["URLs"].items():
        layout += [sg.Text(f'{k}'), sg.In(f'{v}', key=v)],
    for k, v in cfg["UI"].items():
        layout += [sg.Text(f'{k}'), sg.In(f'{v}', key=v)],
    layout += [[sg.Button('Save'), sg.Button('Exit')]]

    window = sg.Window('Alchymia Configuration', layout)
    event, values = window.read()
    window.close()