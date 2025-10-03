import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
data = {
    "hello": "hii, how are you?",
    "how are you": "I'm good, thanks for asking..",
    "good": "Good to hear this.. How can i help you?",
    "what is your name": "i'm Goldy(R**)",
    "who is your owner": "my owner is Mr. Adarsh singh",
    "who is richest man on earth": "Elon musk",
    "who is founder of facebook": "mark juckerburg",
    "who is ceo of google": "sunder pichai",
    "who is pm of india": "shri Narendra damodar das modi",
    "what can you do": "I can give basic answers like Greetings, my name and some GK, ceo and etc...",
    "2+2": "4",
    "tell me a joke": "your life... ☠️",
    "tell me a dark joke": "dark humour is like food everyone can't gets it...☠️"
    #dont use question mark
}

def chatbot_response():
    user_input = input_field.get("1.0", "end-1c")
    if user_input in data:
        response = data[user_input].title()
        response_field.insert("1.0", response)
    elif user_input.lower() == "quit":
        messagebox.showinfo("Goodbye", "Have a nice day..")
        root.destroy()
    else:
        response_field.insert("1.0", "Sorry this is out of my dictionary...")
    input_field.delete("1.0", "end")

def set_background_image():
    background_image_path = "image/ball.jpg"
    image = Image.open(background_image_path)
    photo = ImageTk.PhotoImage(image)
    background_label = tk.Label(root, image=photo)
    background_label.image = photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

root = tk.Tk()
root.title("Chatbot")

set_background_image()

frame = tk.Frame(root, bg="#ffffff")
frame.pack(pady=100)

input_field = tk.Text(frame, height=10, width=40, bg="#f0f0f0")
input_field.pack(pady=10)

button = tk.Button(frame, text="Send", command=chatbot_response, width=10, height=1)
button.pack(pady=10)

response_field = tk.Text(frame, height=10, width=40, bg="#f0f0f0")
response_field.pack(pady=10)

root.mainloop()
