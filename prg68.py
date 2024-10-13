# Доп. библиотека PIL (pillow)
from PIL import Image, ImageDraw

# создаём и рисуем
# 1 холст
canvas = Image.new("RGB", (200, 200), (128, 128, 128))

# создаём рисовальщик
draw = ImageDraw.Draw(canvas)

# рисуем линию
draw.line((0, 0, 200, 200), fill=(255, 0, 0), width=3)

#рисуем прямоугольник
draw.rectangle((0,0,50,50), fill=(255,0,0))
draw.ellipse((0,0,200,200), outline = 'black', width = 5)

#рисуем полигон(треугольник)
draw.polygon(
    xy =(
         (200,200)
         (150,200)
         (200,150)
    ), fill ='red', outline = (0,0,0)
)

canvas = Image.new("RGB", (200, 200), (128, 128, 128))
draw.rectangle((0,0,200,200), fill='blue' , outline = 'black')
draw.line((0, 100, 100, 0), fill='black', width=3)
draw.line((100, 0, 0, 100), fill='black', width=3)

# сохраняем
canvas.save('line.png', 'PNG')