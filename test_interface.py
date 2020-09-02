from tkinter import *

#creating window of class Tk
window = Tk()

#generating the label to display in the window
field_label=Label(window, text="Hello the zeros!")

#we display the label in the window
field_label.pack()

bouton_quitter = Button(window, text="Quitter", command=window.quit)
bouton_quitter.pack()

var_text=StringVar()
line_text=Entry(window, textvariable=var_text, width=10)
line_text.pack()

case = Checkbutton(window, text="Ne plus poser cette question")
case.pack()

liste = Listbox(window)
liste.insert(END, "Pierre")
liste.insert(END, "Ciseaux")
liste.pack()

#starting the loop Tkinter which never interrupts unless we close it
window.mainloop()



