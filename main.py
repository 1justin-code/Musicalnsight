import tkinter as tk

def render():
    window = tk.Tk()
    window.title("Musicalnsight")
    window.geometry("600x400")
    newlabel = tk.Label(text = "TEST!")
    newlabel.grid(column=0,row=0)
    window.mainloop()


if __name__ == "__main__":
    print('welcome to main')
    render()


