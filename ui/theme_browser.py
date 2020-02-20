import PySimpleGUI as sg
from utilities.helpers import load_config, save_config

def theme_list():
    restart = False
    layout = [[sg.Text('Look and Feel Browser')],
            [sg.Text('Click a look and feel color to see demo window')],
            [sg.Listbox(values=sg.theme_list(),
                        size=(20, 20), key='-LIST-', enable_events=True)],
            [sg.Button('Save'), sg.Button('Exit')]]

    window = sg.Window('Look and Feel Browser', layout)

    while True:  # Event Loop
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        if event in (None, 'Save'):
            #print(values['-LIST-'][0])
            cfg = load_config()
            cfg['theme'] = values['-LIST-'][0]
            save_config(cfg)
            restart = True
            break
        sg.theme(values['-LIST-'][0])
        sg.popup('This is {}'.format(values['-LIST-'][0]))


    window.close()
    if restart:
        return "restart"