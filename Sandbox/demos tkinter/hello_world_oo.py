import tkinter as tk


class App(tk.Frame):

    def __init__(self, master = None):
        w = tk.Label(master, text = 'Hello, world!')
        w.pack()

        w = tk.Button(master, text = 'Click here', command=self.event_handler)
        w.pack()


    def event_handler(self):
        print('Clicked!!')


if __name__ == '__main__':
    
    root = tk.Tk()
    root.geometry('500x200+100+100')
    root.title('tkinter demo')
    
    app = App(root)

    root.mainloop()