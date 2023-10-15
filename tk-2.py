import tkinter as tk

app = tk.Tk()
app.geometry("600x400")
app.title("This is my title")
app.configure(background="orange")

lbl = tk.Label(app, text = "This is my text", font=("open sans", 30, "bold"), fg = "red", bg = "yellow")

lbl.pack(fill="x", padx=20, pady=30, ipady=20, ipadx=20)
# lbl.pack(fill="x", padx=20, pady=30, ipady=20, ipadx=20, side="left")


app.mainloop()

