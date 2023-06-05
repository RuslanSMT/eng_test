from tkinter import *
from tkinter import messagebox


def callback(respond):
    global result, counter, addict
    if len(addict) == counter:
        messagebox.showwarning(title='ВЫ ЗАВЕРШИЛИ ТЕСТ', message=f'поздравляю вы завершили тест и набрали {result} очков')
        return
    arr_text = addict[counter]
    lbl.config(text=f'{arr_text[0]}')
    if arr_text[1] == respond:
        result += 1
    counter += 1



window = Tk()
window.title('eng test')
window.geometry('500x500')
result = 0
counter = 0
data = open('data.txt').read().split()
data = enumerate(data)
addict = {}
for item in data:
    value = item[1].split('-')
    addict[item[0]] = [value[0], int(value[1])]

# objects on form
text_frame = Frame(window, width=500, height=300, bg='grey')
text_frame.place(x=0, y=0)
lbl = Label(text_frame, text="Привет", font=("Arial Bold", 20))
lbl.pack()
btn1 = Button(window, width=20, text='YES', command=lambda: callback(1))
btn2 = Button(window, width=20, text='NO', command=lambda: callback(0))
btn1.place(x=50, y=400)
btn2.place(x=300, y=400)



window.mainloop()