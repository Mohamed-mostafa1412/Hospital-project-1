from tkinter import *


# main app window 
Hospital_GUI = Tk()

#title of the window using the title () function 
Hospital_GUI.title("Mohamed Hospital Project")

# Dimension of the window using geometry ()function

Hospital_GUI.geometry("500x300")

# greatings message using label() function 

text = Label(Hospital_GUI, text="Welcom to Mohamed Hospital!", font=("Cooper Black",16))
text.pack()



# loop to make the window working infinity 
Hospital_GUI.mainloop()