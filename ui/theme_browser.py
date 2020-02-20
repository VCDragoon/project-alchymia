import PySimpleGUI as sg

def theme_list():
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
            
            exit(69)
        sg.theme(values['-LIST-'][0])
        sg.popup_get_text('This is {}'.format(values['-LIST-'][0]), default_text=values['-LIST-'][0])

    window.close()