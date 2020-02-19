import PySimpleGUI as sg
import yaml

from ui.bar_graph import bar_graph
from ui.pandas_table_UI import table_example
from ui.scatterplot import scatterplot
from ui.config_ui import config_ui

def load_main_UI():
    # Load configuration from config/config.yaml

    def config_window():
    # Edit/View Configuration
        config_ui()

    def test_menus():
    #TODO remove test menus eventually
        
        sg.set_options(element_padding=(0, 0))

        # ------ Menu Definition ------ #
        menu_def = [['&File', ['&Open     Ctrl-O', '&Save       Ctrl-S', '&Configuration', 'E&xit']],
                    ['&Edit', ['&Paste', ['Special', 'Normal', ], 'Undo'], ],
                    ['&Toolbar', ['---', 'Command &1', 'Command &2',
                                '---', 'Command &3', 'Command &4']],
                    ['&Help', '&About...'], ]

        right_click_menu = ['Unused', ['Right', '!&Click', '&Menu', 'E&xit', 'Configuration']]

        # ------ GUI Defintion ------ #
        # Column layout
        col = [[sg.Button('Pub Stash Stream', pad=((5, 0), (5, 5)))],
            [sg.Button('Flipping Utilities', pad=((5, 0), (5, 5)))],
            [sg.Button('Data Science', pad=((5, 0), (5, 5)))],
            [sg.Button('Raw Data', pad=((5, 0), (5, 5)))],
            [sg.Button('Scatterplot', pad=((5, 0), (5, 5)))]]

        # The tab 1, 2, 3 layouts - what goes inside the tab
        tab1_layout = [[sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
            [sg.Text('Try out File -> Configuration!'),],
            [sg.Output(size=(60, 20)), 
            sg.Col(col)],]

        tab2_layout = [[sg.Text('Tab 2')]]
        tab3_layout = [[sg.Text('Tab 3')]]
        tab4_layout = [[sg.Text('Tab 3')]]

# The TabgGroup layout - it must contain only Tabs
        tab_group_layout = [[sg.Tab('Tab 1', tab1_layout, font='Courier 15', key='-TAB1-'),
                     sg.Tab('Tab 2', tab2_layout, key='-TAB2-'),
                     sg.Tab('Tab 3', tab3_layout, key='-TAB3-'),
                     sg.Tab('Tab 4', tab4_layout, key='-TAB4-'),
                     ]]

        # Window layout
        layout = [[sg.TabGroup(tab_group_layout,
                       enable_events=True,
                       key='-TABGROUP-')]]

        window = sg.Window("Project Alchymia",
                        layout,
                        default_element_size=(12, 1),
                        default_button_element_size=(12, 1),
                        right_click_menu=right_click_menu)

        tab_keys = ('-TAB1-','-TAB2-','-TAB3-', '-TAB4-')

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
            elif event == 'Raw Data':
                table_example()
            elif event == 'Data Science':
                bar_graph()
            elif event == 'Configuration':
                config_window()
            elif event == 'Scatterplot':
                scatterplot()

        window.close()


    test_menus()