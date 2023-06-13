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
                for subs in reac:
                    if reac[subs] == 1:
                        reac[subs] = 1
                for subs in prod:
                    if prod[subs] == 1:
                        prod[subs] = 1
                rxn_balanced = cm.Reaction(reac, prod).string()
                window_rxn['-OUTPUT-'].update(f'Сбалансированная реакция: {rxn_balanced}')
            except Exception:
                sg.popup('Введите корректные данные', title='Error')
                pass
