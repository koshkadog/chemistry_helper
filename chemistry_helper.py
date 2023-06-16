import PySimpleGUI as sg
import windows
import functions

if __name__ == '__main__':
    window = windows.window_main()
    while True:
        event, close = window.read()
        if close == sg.WIN_CLOSED:
            break
        if event == '-RXN_B-':
            functions.rxn_b()
        if event == '-Substance_B-':
            functions.subs()
        if event == '-MASS_FRC-':
            functions.mass_frc()
    window.close()
