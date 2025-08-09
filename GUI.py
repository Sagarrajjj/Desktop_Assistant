# GUI.py
from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action

root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#6F8FAF")


#ask fun
def ask():
    user_val = speech_to_text.speech_to_text()
    if user_val is not None:  # Add this check
        bot_val = action.Action(user_val)
        text.insert(END , 'User------>'+ user_val+"\n")
        if bot_val is not None:
            text.insert(END , 'Bot------>'+str(bot_val)+"\n")
        if bot_val == "ok sir" :
            root.destroy()
    else:
        text.insert(END, "User------> (No speech detected)\n") # Optional: Inform the user

def send():
    user_input = entry.get()
    text.insert(END, 'User------>'+ user_input +"\n")
    entry.delete(0, END) # Clear the entry field after sending
    print("send")

def Delete():
    text.delete("1.0", END)

#frame
frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0, column=0, padx=55, pady=10, columnspan=3)


#text lable
text_label = Label(frame, text="AI Assistant", font=("comic Sans ms", 14, "bold"), bd=4, highlightbackground="#356696", highlightcolor="#356696") # corrected bd and added highlight color
text_label.grid(row=0, column=0, padx=20, pady=10)


#image
try:
    image = ImageTk.PhotoImage(Image.open("image/assitant.png"))
    image_label= Label(frame, image=image)
    image_label.grid(row =1, column = 0, pady = 20)
except FileNotFoundError:
    print("Error: Image file 'image/assitant.png' not found.")

# ADDING A TEXT widget
text = Text(root, font=('courier 10 bold '), bg ="#356696")
# Corrected the typo in 'column' and removed the grid() call to avoid layout conflicts with place()
text.grid(row= 2, column = 0)
text.place(x = 100, y = 375, width = 375, height= 100)


#entry widget

entry = Entry(root, justify=CENTER)
entry.place(x=100, y = 500, width = 350, height = 30)


#button 1

Button1 = Button(root, text="ASK", bg="#356696", pady=16, padx =40, borderwidth=3, relief=SOLID, command=ask)
Button1.place(x =70, y = 575)


#Button 2
Button2 = Button(root, text="Send", bg="#356696", pady=16, padx =40, borderwidth=3, relief=SOLID, command=send)
Button2.place(x =400, y = 575)


#Button3
Button3 = Button(root, text="Delete", bg="#356696", pady=16, padx =40, borderwidth=3, relief=SOLID, command=Delete)
Button3.place(x =225, y = 575)




root.mainloop()
