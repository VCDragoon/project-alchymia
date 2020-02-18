import PySimpleGUI as sg
import yaml

from utilities.helpers import load_config

def load_main_UI():
    # Load configuration from config/config.yaml

    def config_window():
        cfg = load_config()
        # Edit/View Configuration
        layout = []
        for k, v in cfg["URLs"].items():
            layout += [sg.Text(f'{k}'), sg.In(f'{v}', key=v)],
        layout += [[sg.Button('Save'), sg.Button('Exit')]]

        window = sg.Window('Alchymia Configuration', layout)
        event, values = window.read()
        window.close()


    def test_menus():

        
        sg.set_options(element_padding=(0, 0))

        # ------ Menu Definition ------ #
        menu_def = [['&File', ['&Open     Ctrl-O', '&Save       Ctrl-S', '&Configuration', 'E&xit']],
                    ['&Edit', ['&Paste', ['Special', 'Normal', ], 'Undo'], ],
                    ['&Toolbar', ['---', 'Command &1', 'Command &2',
                                '---', 'Command &3', 'Command &4']],
                    ['&Help', '&About...'], ]

        right_click_menu = ['Unused', ['Right', '!&Click', '&Menu', 'E&xit', 'Configuration']]

        # ------ GUI Defintion ------ #
        layout = [
            [sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
            [sg.Text('Try out File -> Configuration!\n\nThe canvas below shows outputs, but can be expanded with loads of cool stuff.')],
            [sg.Output(size=(60, 20))],
        ]

        window = sg.Window("Project Alchymia",
                        layout,
                        default_element_size=(12, 1),
                        default_button_element_size=(12, 1),
                        right_click_menu=right_click_menu)

        # ------ Loop & Process button menu choices ------ #
        while True:
            event, values = window.read()
            if event in (None, 'Exit'):
                break
            print(event, values)
            # ------ Process menu choices ------ #
            if event == 'About...':
                window.disappear()
                sg.popup('About this program', 'Project Alchymia', 'Version 0.0.4',
                        'Made by Chaz Vollmer and Brandon Harris',  grab_anywhere=True)
                window.reappear()
            elif event == 'Open':
                filename = sg.popup_get_file('file to open', no_window=True)
                print(filename)
            elif event == 'Configuration':
                config_window()

        window.close()


    test_menus()