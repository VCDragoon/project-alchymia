import PySimpleGUI as sg
import yaml
from utilities.helpers import load_config

def config_ui():
    cfg = load_config()
    
    layout = []
    for k, v in cfg.items():
        layout += [sg.Text(f'{k}'), sg.In(f'{v}', key=k)],
    layout += [[sg.Button('Save'), sg.Button('Exit')]]

    window = sg.Window('Alchymia Configuration', layout)
    event, values = window.read()
    while True:
            event, values = window.read()
            print(event, values)
            if event in (None, 'Exit'):
                break
            # ------ Process save ------ #
            if event == 'Save':
                cfg = values
                with open('config/config.yaml', 'w') as outfile:
                    yaml.dump(cfg, outfile)
                print("CFG================",cfg)
    window.close()