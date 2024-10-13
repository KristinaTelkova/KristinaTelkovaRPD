#Обрабочик изображений

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk,ImageFilter,ImageEnhance


class App:
    def __init__(self):
        self.root = Tk()
        self.root.title('Обработка изображений')
        self.root.geometry('800x600')
        self.root.resizable(True,True)
        self.root.iconphoto(False, PhotoImage(file='icon.png'))
        self.label= Label(text='Работаем с картинками',
                          background='grey',
                          foreground='#ffffff',
                          font=('Verdana',18)
                          )
        self.label.pack() #раземещение надписи
        self.canvas= Canvas(bg='white', width=600, height=400)
        self.canvas.pack(anchor=CENTER, pady=20)
        self.btn= Button(text='Загрузить', fg="black", bg="grey")
        self.btn.pack(side=LEFT,anchor=N,padx=25, fill=X,expand=True)
        self.blur_btn = Button(text='Размыть', command=self.blur,fg="black", bg="grey")
        self.blur_btn.pack(side=LEFT, anchor=N,padx=25, fill=X, expand=True)
        self.sharp_btn = Button(text='Резкость', command=self.sharp,fg="black", bg="grey")
        self.sharp_btn.pack(side=LEFT, anchor=N, padx=25, fill=X, expand=True)
        #self.flp_btn = Button(text='Отражения', command=self.flip,fg="black", bg="grey")
        #self.flp_btn.pack(side=LEFT, anchor=N, padx=25, fill=X, expand=True)
        self.rtd_btn = Button(text='Перевернуть', command=self.rotate, fg="black", bg="grey")
        self.rtd_btn.pack(side=LEFT, anchor=N, padx=25, fill=X, expand=True)
        self.orig_btn = Button(text='Оригинал', command=self.orig,fg="black", bg="grey")
        self.orig_btn.pack(side=LEFT, anchor=N, padx=25, fill=X, expand=True)
        self.rect_btn = Button(text='Очистить', command=self.make_rect,fg="black", bg="grey")
        self.rect_btn.pack(side=LEFT, anchor=N,padx=25, fill=X, expand=True)
        self.save_btn = Button(text='Сохранить', fg="black", bg="grey", command=lambda: self.load_save('save'))
        self.save_btn.pack(side=LEFT, anchor=N, padx=25, fill=X, expand=True)
        self.save_btn['state'] =DISABLED
        self.btn.bind('<ButtonPress-1>', self.load)
        self.image= None
        self.left , self.top = 0,0
        self.ext =''
        self.empty = Image.new('RGB', (600,400),(255,255,255))
        self.root.mainloop()

    def load(self, event):
        try:
            fullpath=filedialog.askopenfilename(initialdir='./',
                                                filetypes=(
                                                    ('All', '*.*'),
                                                    ('JPEG','*jpg'),
                                                    ('PNG', '*png')
                                                )) #диалог открытия картинки
            self.exp = fullpath.split('.')[-1]
            print(self.exp)
            self.empty = Image.open(fullpath)
            mode = self.empty.mode #получаем световую схему
            if mode == 'P': #256 color indaxed
                self.empty = self.empty.convert('RGB')
            w,h = self.empty.size
            self.left, self.top = 0, 0
            if w > 600:
                ratio = w / 600
                self.empty = self.empty.resize((600, int(h / ratio)))
            else:
                self.left = (600 - w) // 2
                self.top = (400 - h) // 2
            self.image= ImageTk.PhotoImage(self.empty)
            self.canvas.create_image(self.left,self.top, anchor=NW, image=self.image)
        except AttributeError:
            self.image = ImageTk.PhotoImage(self.empty)
            self.canvas.create_image(0,0, anchor=NW, image=self.image)

    def blur(self):
        blur_img = self.empty.filter(ImageFilter.GaussianBlur(5))
        self.image = ImageTk.PhotoImage(blur_img)
        self.canvas.create_image(self.left, self.top, anchor =NW, image = self.image)
        self.save_btn['state'] = NORMAL

    def rotate(self):
        rotate_img = self.empty.rotate(90)
        self.image = ImageTk.PhotoImage(rotate_img)
        self.canvas.create_image(self.left, self.top, anchor=NW, image=self.image)
        self.save_btn['state'] = NORMAL

    def sharp(self):
        sharper = ImageEnhance.Sharpness(self.empty)
        sharp_img = sharper.enhance(5.0)
        self.image = ImageTk.PhotoImage(sharp_img)
        self.canvas.create_image(self.left, self.top, anchor=NW, image=self.image)
        self.save_btn['state'] = NORMAL

   # def flip(self):
    #    flp_img = self.empty.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
     #   self.image = ImageTk.PhotoImage(flp_img)
      #  self.canvas.create_image(self.left, self.top, anchor=NW, image=self.image)
       # self.save_btn['state'] = NORMAL

    def orig(self):
        self.image = ImageTk.PhotoImage(self.empty)
        self.canvas.create_image(self.left, self.top, anchor=NW, image=self.image)
        self.save_btn['state'] = DISABLED

    def load_save(self, *args):
        if len(args) == 1 and args[0] == 'save':
            #print(args[0])
            fullpath = filedialog.asksaveasfilename(initialfile= f'result.{self.ext}')
            if fullpath != '':
                if f'.{self.ext}' not in fullpath:
                    fullpath += f'. self.ext'
                res = ImageTk.getimage(self.image)
                if res.mode == 'RGBA' and 'jp' in self.ext:
                    res= res.convert('RGB')
                res.save(fullpath)
                self.save_btn['state'] = DISABLED


    def make_rect(self):
        self.canvas.create_rectangle(0,0,600,400, outline='#004D00',
                                                 fill='#7f8a55',
                                                 width=5)

app=App()

