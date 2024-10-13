'''
Необходимо разрешение экрана 120%
'''



from tkinter import *
import math
from random import *

# Создание окна и холста
root = Tk()
root.title("Электростатическое поле")
root.geometry("1920x1080")
width = 1920
height = 1080
c = Canvas(root, width=width, height=height, bg='white')
c.pack()

# Меню


def menu(e):
    global c
    c.destroy()
    c = Canvas(root, width=1920, height=1080, bg="white")
    c.pack()
    c.create_text(960, 200, font="Verdana 68", justify="center", text="Меню")
    c.create_text(960, 900, font="Verdana 30", justify="center", text="Для перехода наведите курсор на кнопку\nи нажмите левую кнопку мыши",
                  fill="grey")
    Button(c, text="Условие", font='Verdana 30', command=task, relief=SOLID, bd=4).place(x=960, y=400, width=360, heigh=120, anchor="c")
    Button(c, text="Раб. поле", font='Verdana 30', command=work, relief=SOLID, bd=4).place(x=960, y=550, width=360, heigh=120, anchor="c")
    Button(c, text="Помощь", font='Verdana 30', command=help1, relief=SOLID, bd=4).place(x=960, y=700, width=360, heigh=120, anchor="c")

# Условие


def task():
    global c
    c.destroy()
    c = Canvas(root, width=1920, height=1080, bg="white")
    c.pack()
    c.create_text(960, 200, font="Verdana 36", justify="center", text="Условие")
    c.create_text(960, 500, font="Verdana 30", justify="left", text="   Составить программу,\
 моделирующую построение линий\nнапряженности электростатического поля.\
 Электростатиче-\nское поле создается неподвижными зарядами. Величины \nзарядов вводятся с клавиатуры в процессе диалога.\
Знак\nзарядов может быть как одинаковый,так и разный. Разме-\nщение зарядов на экране произвольное, задается с помо-\nщью мышки.")
    c.create_text(960, 900, font="Verdana 27", justify="center", text="Для возращения в меню нажмите ESCAPE или пробел", fill="grey")

# Помощь


def help1():
    global c
    c.destroy()
    c = Canvas(root, width=1920, height=1080, bg="white")
    c.pack()
    c.create_text(960, 100, font="Verdana 38", justify="center", text="Помощь")
    c.create_text(200, 200, font="Verdana 32", anchor="w", text="С помощью левой кнопки мыши можно переходить в подпункты меню")
    c.create_text(200, 272, font="Verdana 32", anchor="w", text="С помощью пробела и кнопки ESCAPE можно возвращаться в меню")
    c.create_text(200, 344, font="Verdana 32", anchor="w", text="Чтобы поставить заряд, кликните левой кнопкой мыши,")
    c.create_text(200, 416, font="Verdana 32", anchor="w", text="предварительно изменив величину заряда при желании")
    c.create_text(200, 488, font="Verdana 32", anchor="w", text="Чтобы удалить заряд, поставьте на него курсор и нажмите Delete")
    c.create_text(200, 590, font="Verdana 32", anchor="w", text="Чтобы переместить заряд, зажмите левую кнопку мыши\n\
и перетащите заряд")
    c.create_text(200, 706, font="Verdana 32", anchor="w", text="Чтобы изменить заряд, кликните правой кнопкой мыши, введите значение\nи\
 нажмите Enter")
    c.create_text(200, 790, font="Verdana 32", anchor="w", text='Чтобы очистить экран, нажмите "Очистить"')
    c.create_text(200, 850, font="Verdana 32", anchor="w", text='Чтобы начать построение, нажмите "Построить"')
    c.create_text(200, 920, font="Verdana 32", anchor="w", text='Для автозаполнения нажмите F3')
    c.create_text(960, 960, font="Verdana 23", justify="center", text="Для возращения в меню нажмите ESCAPE или пробел", fill="grey")

# Work
# Сетка


def grid():
    c.create_line(520, 20, 520, 980, width=2, arrow="f")
    c.create_text(520, 1005, font="Verdana 11", anchor="s", text="0")
    for x in range(560, 1880, 40):
        c.create_line(x, 20, x, 980, width=1, fill="grey")
        c.create_text(x, 1005, font="Verdana 11", anchor="s", text=str(x - 520))
    c.create_line(520, 980, 1880, 980, width=2, arrow="l")
    for y in range(60, 980, 40):
        c.create_line(520, y, 1880, y, width=1, fill="grey")
        c.create_text(480, y, font="Verdana 11", anchor="w", text=str(980 - y))
    c.create_text(490, 25, font="Arial 22", anchor="w", text="y")
    c.create_text(1880, 1010, font="Arial 22", anchor="s", text="x")
    c.create_text(260, 980, font="Verdana 13", justify="center", text="Для возращения в меню\nнажмите ESCAPE или пробел", fill="grey")


def help2():
    help1()
    Button(c, text="Назад", font='Verdana 15', command=work, relief=SOLID, bd=4).place(x=200, y=100, width=200, heigh=60, anchor="c")

# Charge


class Charge:
    def __init__(self, q, x, y):
        self.q = q
        self.x = x
        self.y = y
        self.ov = c.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, width=3, fill="white")
        self.minus = c.create_line(self.x - 13, self.y, self.x + 13, self.y, width=3)
        if self.q[0] != "-":
            self.plus = c.create_line(self.x, self.y - 13, self.x, self.y + 13, width=3)
        else:
            self.plus = c.create_line(1, 1, 2, 2, fill="white")
        self.po = []

    def move_ch(self, e):
        global ch, ova, ov
        if e.x >= 540 and e.x <= 1860 and e.y >= 40 and e.y <= 960:
            if ova == 1:
                c.delete(ov)
                ova = 0
            self.x = e.x
            self.y = e.y
            c.coords(self.ov, self.x - 20, self.y - 20, self.x + 20, self.y + 20)
            c.coords(self.minus, self.x - 13, self.y, self.x + 13, self.y)
            if self.q[0] != "-":
                c.coords(self.plus, self.x, self.y - 13, self.x, self.y + 13)
            c.delete(ch[charges.index(self)].lab)
            c.coords(ch[charges.index(self)].text, self.x + 7, self.y + 7)
            if charges.index(self) < 12:
                ch[charges.index(self)].lab = c.create_text(130, 230 + 40 * charges.index(self), font="Verdana 15", anchor="w", text="q"
                                                            + unic[charges.index(self)] + ' = ' + self.q + ' (' + str(self.x - 520) + ', ' + str(980 - self.y) + ')')

    def stop(self, e):
        root.unbind('<Motion>')


# For coords of charges
unic = ['\u2081', '\u2082', '\u2083', '\u2084', '\u2085', '\u2086', '\u2087', '\u2088', '\u2089', '\u2081' + '\u2080', '\u2081' + '\u2081',
        '\u2081' + '\u2082']


class Text:
    def __init__(self, q, x, y):
        global n
        self.q = q
        self.x = x
        self.y = y
        if len(charges) <= 12:
            self.lab = c.create_text(130, 230 + 40 * (len(ch)), font="Verdana 17", anchor="w", text="q"
                                     + unic[len(ch)] + ' = ' + q + ' (' + str(self.x - 520) + ', ' + str(980 - self.y) + ')')
        else:
            self.lab = c.create_line(1, 1, 2, 2, fill="white")
        ch.append(self)
        self.text = c.create_text(self.x + 7, self.y + 7, font="Verdana 10", anchor="c", text=str(len(ch)))


def f(e):
    x = entr.get()
    s = ""
    n = 1
    for i in x:
        if i.isdigit() or (i == "-" and n == 1):
            s += i
        n += 1
    entr.delete(0, END)
    entr.insert(0, s)


charges = []
ch = []
sth = 0

# Deleting charges


def del_ch(e):
    global charges, ch, ova, ov
    for i in charges:
        if ((e.x - i.x)**2 + (e.y - i.y)**2)**0.5 <= 20:
            if ova == 1:
                c.delete(ov)
                ova = 0
            c.delete(ch[charges.index(i)].lab)
            c.delete(ch[charges.index(i)].text)
            ch.pop(charges.index(i))
            c.delete(i.ov)
            c.delete(i.plus)
            c.delete(i.minus)
            charges.remove(i)
            for j in ch:
                c.delete(j.lab)
                if ch.index(j) < 12:
                    j.lab = c.create_text(130, 230 + 40 * ch.index(j), font="Verdana 15", anchor="w", text="q"
                                          + unic[ch.index(j)] + ' = ' + charges[ch.index(j)].q + ' (' + str(j.x - 520) + ', ' + str(980 - j.y) + ')')
                c.delete(j.text)
                j.text = c.create_text(charges[ch.index(j)].x + 7, charges[ch.index(j)].y + 7, font="Verdana 10", anchor="c", text=str(ch.index(j) + 1))
            break
# Click to create or move a charge


def f1(e):
    global charges, ch, entr, ova, ov
    if ova == 1:
        c.delete(ov)
        ova = 0
    entr.bind("<KeyRelease>", f)
    n = 0
    if e.x >= 540 and e.x <= 1860 and e.y >= 40 and e.y <= 960:
        if len(charges) == 0:
            q = entr.get()
            charges.append(Charge(q=q, x=e.x, y=e.y))
            Text(q, e.x, e.y)
        else:
            for i in charges:
                if ((e.x - i.x)**2 + (e.y - i.y)**2)**0.5 <= 20:
                    root.bind('<Motion>', i.move_ch)
                    root.bind('<ButtonRelease-1>', i.stop)
                    n = 1
                    break
                elif ((e.x - i.x)**2 + (e.y - i.y)**2)**0.5 <= 40:
                    n = 1
            if n == 0:
                q = entr.get()
                charges.append(Charge(q=q, x=e.x, y=e.y))
                Text(q, e.x, e.y)


ova = 0
# Click to change:


def f2(e):
    global charges, ch, entr, ova, ov, cvet
    for i in charges:
        if ((e.x - i.x)**2 + (e.y - i.y)**2)**0.5 <= 20:
            if ova == 1:
                if c.coords(ov)[0] + 20 == i.x:
                    c.delete(ov)
                    ova = 0
                    entr.bind("<KeyRelease>", f)
                    break
                else:
                    c.delete(ov)
                    ova = 0
            ov = c.create_oval(i.x - 20, i.y - 20, i.x + 20, i.y + 20, width=3, outline="red")
            ova = 1
            entr.delete(0, END)
            entr.insert(0, i.q)            

            def read(e):
                s = ""
                x=entr.get()
                n=1
                for j in x:
                    if j.isdigit() or (j=="-" and n==1):
                        s += j
                    n+=1
                entr.delete(0, END)
                entr.insert(0, s) 
                if i.q[0] != "-" and entr.get()[0] == "-":
                    c.delete(i.plus)
                elif i.q[0] == "-" and entr.get()[0] != "-":
                    i.plus = c.create_line(i.x, i.y - 13, i.x, i.y + 13, width=3)
                i.q = s
                c.delete(ch[charges.index(i)].lab)
                if charges.index(i) < 12:
                    ch[charges.index(i)].lab = c.create_text(130, 230 + 40 * charges.index(i), font="Verdana 15", anchor="w", text="q"
                                                             + unic[charges.index(i)] + ' = ' + i.q + ' (' + str(i.x - 520) + ', ' + str(980 - i.y) + ')')
            entr.bind("<KeyRelease>", read)
            break


# DRAWING
colors = ["black", "red", "orange", "green", "light blue", "blue", "purple", "brown"]


def draw():
    global butt, pls, ova, ov
    if ova == 1:
        c.delete(ov)
        ova = 0
    root.unbind('<Delete>')
    c.unbind('<Button-1>')
    c.unbind('<Button-3>')
    root.unbind("<space>")
    root.unbind("<Escape>")
    butt["state"] = DISABLED
    pls["state"] = DISABLED
    global sth
    if sth > 7:
        clear(1)
        if len(charges) != 0:
            for i in charges:
                i.ov = c.create_oval(i.x - 20, i.y - 20, i.x + 20, i.y + 20, width=3, fill="white")
                i.minus = c.create_line(i.x - 13, i.y, i.x + 13, i.y, width=3)
                if i.q[0] != "-":
                    i.plus = c.create_line(i.x, i.y - 13, i.x, i.y + 13, width=3)
                else:
                    i.plus = c.create_line(1, 1, 2, 2, fill="white")
                Text(i.q, i.x, i.y)
    for i in charges:
        if abs(int(i.q)) < 23:
            step = 60
        elif abs(int(i.q)) <= 35:
            step = 360 / 7
        elif abs(int(i.q)) <= 48:
            step = 45
        elif abs(int(i.q)) <= 61:
            step = 40
        elif abs(int(i.q)) <= 74:
            step = 36
        elif abs(int(i.q)) <= 87:
            step = 360 / 11
        else:
            step = 30        
        if i.q[0] != '-':
            arr = 'l'
            sign = 1
        else:
            arr = 'f'
            sign = -1
        for p in range(0, 360, step):
            x = i.x + 20 * math.cos(p * math.pi / 180)
            y = i.y - 20 * math.sin(p * math.pi / 180)
            tre = 0
            if len(i.po) != 0:
                for hui in i.po:
                    hwlp = ((hui[0] - i.x)**2 + (hui[1] - i.y)**2 + (i.x - x)**2 + (i.y - y)**2 - (hui[0] - x)**2 - (hui[1] - y)**2
                            )/(2*((hui[0] - i.x)**2 + (hui[1] - i.y)**2)**0.5 * ((i.x - x)**2 + (i.y - y)**2)**0.5)
                    if hwlp > math.cos(step * math.pi / 180) and hwlp < 1:
                        tre = 1
            n = 1
            s = randint(0, 10000000)
            while True:
                if tre == 1:
                    break                
                ops = 0
                for j in charges:
                    if ((x - j.x)**2 + (y - j.y)**2)**0.5 > 20 and charges.index(j) != charges.index(i):
                        ops += 1
                    elif charges.index(j) != charges.index(i):
                        tired = j
                if ops == len(charges) - 1:
                    x0 = x
                    y0 = y
                    dx = 0
                    dy = 0
                    for b in charges:
                        r = ((b.x - x0)**2 + (b.y - y0)**2) ** 0.5  # радиус
                        e = sign * 2000 * int(b.q) / (r ** 2)  # напряженность
                        sin = (b.y - y0) / r
                        cos = (x0 - b.x) / r
                        dx1 = e * cos
                        dy1 = e * sin
                        dx += dx1
                        dy += dy1
                    if dx ** 2 + dy ** 2 < 0.001:
                        if x > 520 and y > 20 and x < 1880 and y < 980:
                            c.delete("J" + str(s))
                        break
                    if n >= 2000 and x > 520 and y > 20 and x < 1880 and y < 980:
                        c.delete("J" + str(s))
                        break
                    dxb = 2 * dx / (dx ** 2 + dy ** 2) ** 0.5
                    dyb = 2 * dy / (dx ** 2 + dy ** 2) ** 0.5
                    x = x0 + dxb
                    y = y0 - dyb
                    if x > 520 and y > 20 and x < 1880 and y < 980:
                        if n % 80 == 0:
                            c.create_line(x0, y0, x, y, width=3, arrow=arr, fill=colors[sth], tag="J" + str(s), arrowshape="8 16 8")
                        else:
                            c.create_line(x0, y0, x, y, width=3, fill=colors[sth], tag="J" + str(s))
                    n += 1
                else:
                    tired.po.append([x,y])
                    break
            c.update()
    sth += 1
    root.bind('<Delete>', del_ch)
    c.bind('<Button-1>', f1)
    c.bind('<Button-3>', f2)
    root.bind("<space>", menu)
    root.bind("<Escape>", menu)
    butt["state"] = NORMAL
    pls["state"] = NORMAL


def clear(a=0):
    global charges, ch, sth, ova, ov
    if ova == 1:
        c.delete(ov)
        ova = 0
    if pls["state"] == DISABLED:
        pls["state"] = NORMAL
    if butt["state"] == DISABLED:
        butt["state"] = NORMAL
    c.delete("all")
    grid()
    if a == 0:
        charges = []
    ch = []
    sth = 0
    root.bind('<Delete>', del_ch)
    c.bind('<Button-1>', f1)
    root.bind("<space>", menu)
    root.bind("<Escape>", menu)
    entr.bind("<KeyRelease>", f)


def auto(e):
    global charges, ch, entr, ova, ov
    if ova == 1:
        c.delete(ov)
        ova = 0
    entr.bind("<KeyRelease>", f)
    clear(0)
    xs = [867, 1345]
    ys = [550, 714]
    for i in range(2):
        charges.append(Charge(q='100', x=xs[i], y=ys[i]))
        Text('100', xs[i], ys[i])
    charges.append(Charge(q='-100', x=1345, y=198))
    Text('-100', 1345, 198)
# File


def save():
    fil = open('charges.txt', 'w+', encoding='utf-8')
    for i in charges:
        fil.write('q' + str(charges.index(i)) + ' = ' + i.q + ' (' + str(i.x - 520) + ', ' + str(980 - i.y) + ')\n')
    fil.close()


def download():
    global charges, pls, butt, ova, ov
    if ova == 1:
        c.delete(ov)
        ova = 0
    if pls["state"] == DISABLED:
        pls["state"] = NORMAL
    if butt["state"] == DISABLED:
        butt["state"] = NORMAL
    clear(0)
    fil = open('charges.txt', 'r', encoding='utf-8')
    for i in fil.readlines():
        i = i.split()
        charges.append(Charge(i[2], int(i[3][1:-1]) + 520, 980 - int(i[4][:-1])))
    for i in charges:
        Text(i.q, i.x, i.y)
    root.bind('<Delete>', del_ch)
    c.bind('<Button-1>', f1)
    root.bind("<space>", menu)
    root.bind("<Escape>", menu)

# Main


def work():
    global c, entr, ch, butt, pls
    c.destroy()
    c = Canvas(root, width=1920, height=1080, bg="white")
    c.pack()
    # Entry
    message = StringVar()
    entr = Entry(textvariable=message, font=("Verdana", 18), relief=SOLID, bd=4, width=21)
    entr.pack()
    entr.place(x=95, y=40)
    entr.insert(0, "100")
    Label(font="Verdana 18", anchor="w", text="q:", bg="white").place(x=50, y=40)

    # Recomended range
    Label(font="Verdana 15", anchor="c", text="Рекомендуеся брать значения зарядов,\nотличающиеся между собой\n по модулю менее, чем в 10 раз",
          bg="white").place(x=50, y=110)
    Label(font="Verdana 12", anchor="c", text="Поле ввода для будущего заряда или изменения",
          bg="white", fg="grey").place(x=40, y=85)

    entr.bind("<KeyRelease>", f)
    pls = Button(c, text="Построить", font='Verdana 15', command=draw, relief=SOLID, bd=4)
    pls.pack()
    pls.place(x=260, y=740, width=325, heigh=55, anchor="c")
    Button(c, text="Очистить", font='Verdana 15', command=clear, relief=SOLID, bd=4).place(x=260, y=800, width=325, heigh=55, anchor="c")
    butt = Button(c, text="Помощь", font='Verdana 15', command=help2, relief=SOLID, bd=4)
    butt.pack()
    butt.place(x=260, y=860, width=325, heigh=55, anchor="c")
    Button(c, text="Сохранить", font='Verdana 15', command=save, relief=SOLID, bd=4).place(x=179, y=920, width=160, heigh=55, anchor="c")
    Button(c, text="Загрузить", font='Verdana 15', command=download, relief=SOLID, bd=4).place(x=342, y=920, width=160, heigh=55, anchor="c")

    grid()
    if len(charges) != 0:
        ch = []
        for i in charges:
            i.ov = c.create_oval(i.x - 20, i.y - 20, i.x + 20, i.y + 20, width=3, fill="white")
            i.minus = c.create_line(i.x - 13, i.y, i.x + 13, i.y, width=3)
            if i.q[0] != "-":
                i.plus = c.create_line(i.x, i.y - 13, i.x, i.y + 13, width=3)
            else:
                i.plus = c.create_line(1, 1, 2, 2, fill="white")
            Text(i.q, i.x, i.y)
    root.bind('<Delete>', del_ch)
    c.bind('<Button-1>', f1)
    c.bind('<Button-3>', f2)
    root.bind('<F3>', auto)


# Заставка
c.create_text(960, 300, text='Построение линий напряжённости\nэлектростатического поля\nточечных зарядов', font="Verdana 54", justify="center")
c.create_text(960, 500, text='Троицкая Юна', font="Verdana 38", justify="center", fill="grey")
c.create_text(960, 580, text="Студент НИЯУ МИФИ, 2 курс", font="Verdana 38", justify="center", fill="grey")
c.create_text(960, 800, text="Нажмите на пробел, чтобы перейти в меню.", font="Verdana 40", justify="center")
root.bind("<space>", menu)
root.bind("<Escape>", menu)

root.mainloop()
