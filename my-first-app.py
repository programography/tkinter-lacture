import tkinter as tk

app = tk.Tk()

app.geometry("500x500")
app.title("This is my title")
app.configure(background = "green")


lbl = tk.Label(app, text="Hellow word")
lbl.pack()


app.mainloop()


# pack()
# grid()
# place()