from tkinter import *
import requests


def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    data = response.json()[0]
    quote = data['q'] + ' - ' + data['a']
    canvas.itemconfig(quote_text, text=quote)

window = Tk()
window.title("")
window.config(padx=50, pady=50)

canvas = Canvas(width=380, height=450)
background_img = PhotoImage(file="filetextbox.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Click the Portrait Button for Quotes!", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="filepicjvg.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
