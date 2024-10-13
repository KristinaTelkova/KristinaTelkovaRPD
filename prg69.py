# GUI - Grafic User Interface
#PyQt6
import tkinter
from PIL import Image, ImageTk

class App:
    def __init__(self):
        #корневой элемент приложения
        self.root = tkinter.Tk()

        #рабочая область
        self.frame = tkinter.Frame(self.root)
        self.frame.grid()

        #добавляем ярлык
        self.label = tkinter.Label(self.frame, text='GUI').grid(row=1,column=1)

        self.but= tkinter.Button(self.frame,
                                 text='Заменить',
                                 command=self.change).grid(row=1,column=2)

        self.canvas = tkinter. Canvas(self.root,height = 200, width= 200)

        self.image = Image.open('original.jpg')
        self.photo = ImageTk.PhotoImage(self.image)
        self.image = self.canvas.create_image(0,0,anchor='nw', image= self.photo)
        self.canvas.grid(row=2,column=1)


        self.root.mainloop()

  #функция change
    def change(self):
        print('Кнопка нажата')
        self.image = Image.open('original2.jpg')
        self.photo = ImageTk.PhotoImage(self.image)
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid(row=2, column=1)

app= App()