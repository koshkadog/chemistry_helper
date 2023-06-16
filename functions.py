import PySimpleGUI as sg
import chempy as cm
import windows


def rxn_b():
    window_rxn = windows.window_rxn()
    while True:
        event_rxn, rxn = window_rxn.read()
        if event_rxn == sg.WIN_CLOSED:
            break
        if event_rxn == '-balance_stoichiometry-':
            try:
                rxn['-RXN-'] = rxn['-RXN-'].split('=')
                left = ''.join(rxn['-RXN-'][0].split('+'))
                right = ''.join(rxn['-RXN-'][1].split('+'))
                reac, prod = left.split(), right.split()
                reac, prod = cm.balance_stoichiometry(reac, prod)
                reac, prod = dict(reac), dict(prod)
                for sub in reac:
                    if reac[sub] == 1:
                        reac[sub] = 1
                for sub in prod:
                    if prod[sub] == 1:
                        prod[sub] = 1
                rxn_balanced = cm.Reaction(reac, prod).string()
                window_rxn['-OUTPUT-'].update(f'Сбалансированная реакция: {rxn_balanced}')
            except Exception:
                sg.popup('Введите корректные данные', title='Error')
                pass


def subs():
    window_substance = windows.window_substance()
    while True:
        event_substance, substance = window_substance.read()
        if event_substance == sg.WIN_CLOSED:
            break
        if event_substance == '-SUB_INFO-':
            try:
                sub = cm.Substance.from_formula(substance['-Substance-'])
                window_substance['-OUTPUT-'].update(f'Информация о веществе: {sub.unicode_name}\n\n'
                                                    f'Формула в формате latex: {sub.latex_name}\n\n'
                                                    f'Формула в формате html: {sub.html_name}\n\n'
                                                    f'Заряд: {sub.charge}\n\n'
                                                    f'Молярная масса {sub.unicode_name} = {sub.molar_mass()}')
            except Exception:
                sg.popup('Введите корректные данные', title='Error')
                pass


def mass_frc():
    window_fractions = windows.window_frc()
    while True:
        event_frc, mass = window_fractions.read()
        if event_frc == sg.WIN_CLOSED:
            break
        if event_frc == '-fractions-':
            try:
                sub = mass['-MASS-'].split(';')
                moles = []
                comp = []
                for i in sub:
                    i = i.split(':')
                    comp.append(i[0])
                    moles.append(int(i[1]))
                sub_dict = dict(zip(comp, moles))
                mass_frac = cm.mass_fractions(sub_dict)
                for i in range(len(mass_frac.keys())):
                    window_fractions['-OUTPUT-'].update(
                        window_fractions['-OUTPUT-'].get() + f'Доля {list(mass_frac.keys())[i]} = '
                                                             f'{list(mass_frac.values())[i]: g} %\n')
            except Exception:
                sg.popup('Введите корректные данные', title='Error')
                pass
