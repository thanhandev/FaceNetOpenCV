from tkinter import *
import os

window = Tk()
window.geometry('800x1000')
window.title('HỆ THỐNG NHẬN DIỆN KHUÔN MẶT')
window.configure(bg='lavender')


def detect():
	os.system('python3 face_lock.py')
	window.destroy()
def addface():
	os.system('python3 add_face.py')
	window.destroy()
def train():
	os.system('python3 training.py')
	window.destroy()
def diemdanh():
	os.system('python3 diemdanh.py')
	window.destroy()
Label(window, text='Mời chọn chương trình:',bg='skyblue').grid(row=0,column=0)

Button(window, text='NHẬN DIỆN KHUÔN MẶT', bg='red',height=5,width=100,command=detect).grid(row=2,column=0)
Button(window, text='THÊM KHUÔN MẶT', bg='blue',height=5,width=100,command=addface).grid(row=4,column=0)
Button(window, text='ĐÀO TẠO DATASET', bg='green',height=5,width=100,command=train).grid(row=6,column=0)
Button(window, text='ĐIỂM DANH', bg='yellow',height=5,width=100,command=diemdanh).grid(row=8,column=0)

window.mainloop()
