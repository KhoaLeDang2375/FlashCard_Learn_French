from tkinter import *
from pandas import*
import random
BACKGROUND_COLOR = "#B1DDC6"
BACK_COLOR="#92C5B1"
Current_card=[]
#--------------------------------Step 2 - Create New Flash Cards--\
try:
    data_word=read_csv("./data/words_to_learn.csv") #read file csv and convert to dataframe
except:
      original_data=read_csv("./data/french_words.csv")
      data_dict=original_data.to_dict(orient="records") # comvert to dictionary 
else:
    data_dict=data_word.to_dict(orient="records") # comvert to dictionary 
word_to_learn_dict=[]
def Flip_the_cards():
      pass
def New_Random_word():
    global Current_card,flip_timer
    windown.after_cancel(flip_timer)
    Current_card=random.choice(data_dict)
    Title_label.config(text="French")
    Current_word=Current_card["French"]
    Trouve_label.config(text=Current_word)
    canvas.itemconfig(canvas_image,image=img)
    Trouve_label.config(bg="white",fg="black")
    Title_label.config(bg="white",fg="black")
    flip_timer=windown.after(3000,func=Flip_the_cards)
    #------Step 3 - Flip the Cards!--------------------------------
def Flip_the_cards():
        canvas.itemconfig(canvas_image,image=new_img)
        Title_label.config(text="English",bg=BACK_COLOR,fg="white")
        Trouve_label.config(text=Current_card["English"],bg=BACK_COLOR,fg="white")
#----------------Step 4-Save_your_process--------------------------------
def is_know():
      data_dict.remove(Current_card)
      data= DataFrame(data_dict)
      data.to_csv("data/words_to_learn.csv",index=False)
      New_Random_word()
#----------------------------------------------------------------UI CREATE----------------------------------------------------------------
windown=Tk()
windown.title("Flashy")
windown.configure(padx= 50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=windown.after(3000,func=Flip_the_cards)
canvas=Canvas(width=800,height=528)
img=PhotoImage(file="./images/card_front.png")
new_img=PhotoImage(file="./images/card_back.png")
canvas_image=canvas.create_image(400,264,image=img)
canvas.grid(row=0,column=0,columnspan=2)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)

#Create label French
Title_label = Label(windown, text="French", font=("Ariel", 40, "italic"), bg="white")
Title_label.place(x=400, y=150, anchor="center")  # Centered at the specified x, y

#Create label trouve
Trouve_label=Label(windown,text="trouve",font=("Ariel",60,"bold"),bg="white")
Trouve_label.place(x=400,y=263,anchor="center")

#Red Cross line Insert btn
image_red_cross = PhotoImage(file="./images/wrong.png")
wrong_button= Button(image=image_red_cross, highlightthickness=0,bg=BACKGROUND_COLOR,command=New_Random_word)
wrong_button.grid(column=0,row=1)

#Insert rigth_button
image_green_tick = PhotoImage(file="./images/right.png")
right_button= Button(image=image_green_tick, highlightthickness=0,bg=BACKGROUND_COLOR,command=is_know)
right_button.grid(column=1,row=1)
New_Random_word()




windown.mainloop()