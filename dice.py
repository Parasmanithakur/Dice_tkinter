import tkinter #library for the gui
from PIL import Image, ImageTk #library for image import
import random

root =tkinter.Tk() #root is the window name 
root.geometry('400x400')
root.title('Roll the Dice')

BlankLine = tkinter.Label(root, text="")
BlankLine.pack()
HeadingLabel =tkinter.Label(root, text='Hello Form Parasmani',
  fg= "light green",
    bg="dark green",
     font ="Helvetica 16 bold italic")
HeadingLabel.pack()

#images
dice =['die1.png','die2.png','die3.png',
 'die4.png','die5.png','die6.png']
DiceImage =ImageTk.PhotoImage(Image.open(random.choice(dice)))

ImageLabel =tkinter.Label(root,image=DiceImage)

ImageLabel.pack(expand=True)
# function activated by button
def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    ImageLabel.configure(image=DiceImage)
    # keep a reference
    ImageLabel.image = DiceImage
# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)
# pack a widget in the parent widget
button.pack( expand=True)
root.mainloop()