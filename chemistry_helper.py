import PySimpleGUI as sg
import windows
import rxn_balance
import substance

if __name__ == '__main__':
    window = windows.window_main()
    while True:
        event, close = window.read()
        if close == sg.WIN_CLOSED:
            break
        if event == '-RXN_B-':
            rxn_balance.rxn_b()
        if event == '-Substance_B-':
            substance.subs()
    window.close()
