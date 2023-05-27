import PySimpleGUI as sg
import chempy as cm
import windows

if __name__ == '__main__':
    window = windows.window_main()
    while True:
        event, close = window.read()
        if close == sg.WIN_CLOSED:
            break
        if event == '-RXN_B-':
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
                        for subs in reac:
                            if reac[subs] == 1:
                                reac[subs] = 1
                        for subs in prod:
                            if prod[subs] == 1:
                                prod[subs] = 1
                        rxn_balanced = cm.Reaction(reac, prod).string()
                        window_rxn['-OUTPUT-'].update(f'Сбалансированная реакцию: {rxn_balanced}')
                    except Exception:
                        sg.popup('Введите корректные данные', title='Error')
                        pass
        if event == '-Substance_B-':
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
    window.close()
