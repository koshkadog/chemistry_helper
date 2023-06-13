import PySimpleGUI as sg
import chempy as cm
import windows


def subs():
    window_substance = windows.window_substance()
    while True:
        event_substance, substance = window_substance.read()
        if event_substance == sg.WIN_CLOSED:
            break
        if event_substance == '-SUB_INFO-':
            try:
                subs = cm.Substance.from_formula(substance['-Substance-'])
                window_substance['-OUTPUT-'].update(f'Информация о веществе: {subs.unicode_name}\n\n'
                                                    f'Формула в формате latex: {subs.latex_name}\n\n'
                                                    f'Формула в формате html: {subs.html_name}\n\n'
                                                    f'Заряд: {subs.charge}\n\n'
                                                    f'Молярная масса {subs.unicode_name} = {subs.molar_mass()}')
            except Exception:
                sg.popup('Введите корректные данные', title='Error')
                pass
