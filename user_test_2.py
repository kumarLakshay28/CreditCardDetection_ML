import hist_credit
import cormat_credit
import plot_features
import tkinter
from tkinter import *

def trial_1():
    hist_credit.hist_disp()
    return
def trial_2():
    cormat_credit.cormat_disp()
    return
def trial_3():
    plot_features.plot_disp()
    return


def mainFrame():
    root = tkinter.Tk()
    root.wm_title("Access Allowed")

    but_hist = Button(root, font = ('arieal',18),text= " Histrogram ( features vs Class) ",bg = 'white' , fg = 'lightcoral', anchor = 'n', command = trial_1)
    but_hist.pack(side="top", fill= X,  padx=10, pady=10)

    but_cormat = Button(root, font=('arieal', 18), text=" Co-Relation ( features) ", bg = 'white' ,fg='blue', anchor='n',command = trial_2)
    but_cormat.pack(side="top", fill= X, padx=10, pady=10)

    but_feature = Button(root, font=('arieal', 18), text=" Features ", bg = 'white' ,fg='yellow', anchor='n',command = trial_3)
    but_feature.pack(side="top", fill= X, padx=10, pady=10)

    root.mainloop()
    return
