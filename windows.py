import PySimpleGUI as sg


def window_main():
    layout = [[sg.Text('Химический калькулятор', expand_x=True, justification='centre', font='Any 20', pad=20)],
              [sg.Button('Информация о веществе', size=(10, 5), pad=((73, 15), (0, 0)), key='-Substance_B-'),
               sg.Button('Химическая реакция', size=(10, 5), pad=((0, 0), (0, 0)), key='-RXN_B-'),
               sg.Button('Расчёт массовых долей', size=(10, 5), pad=((15, 73), (0, 0)), key='-MASS_FRC-')]]

    window = sg.Window('Chemistry Helper', layout,
                       # size=(550, 200),
                       font='Arial 12 bold',
                       background_color='lightgrey',
                       # icon='images/chemistry.ico',
                       return_keyboard_events=True,
                       grab_anywhere=True,
                       finalize=True)
    return window


def window_rxn():
    rxn_layout = [[sg.Text('Введите реакцию: '), sg.InputText(key='-RXN-')],
                  [sg.Button('Сбалансировать реакцию', key='-balance_stoichiometry-')],
                  [sg.Text('', background_color='lightgrey', text_color='black', key='-OUTPUT-')]]
    window = sg.Window('Реакция', rxn_layout,
                       size=(600, 200),
                       font='Arial 12 bold',
                       background_color='lightgrey',
                       grab_anywhere=True,
                       resizable=True)
    return window


def window_substance():
    substance_layout = [[sg.Text('Введите формулу вещества: '), sg.InputText(key='-Substance-'),
                         sg.Button('Вывести информацию о веществе', key='-SUB_INFO-')],
                        [sg.Text('', background_color='lightgrey', text_color='black',
                                 font='Any 15', key='-OUTPUT-')]]
    window = sg.Window('Вещество', substance_layout,
                       size=(990, 350),
                       font='Arial 12 bold',
                       background_color='lightgrey',
                       grab_anywhere=True)
    return window


def window_frc():
    mass_frc_layout = [[sg.Text('Введите вещества и их количественный состав (например, "H2:1;O2:1"): '),
                        sg.InputText(key='-MASS-')],
                       [sg.Button('Рассчитать массовые доли', key='-fractions-')],
                       [sg.Text('', background_color='lightgrey', text_color='black', key='-OUTPUT-')]]
    window = sg.Window('Массовые доли', mass_frc_layout,
                       size=(990, 350),
                       font='Arial 12 bold',
                       background_color='lightgrey',
                       grab_anywhere=True)
    return window
