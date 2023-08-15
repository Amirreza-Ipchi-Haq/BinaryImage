#!/bin/python3
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import cv2
import numpy
import tkinter
def save(file): #Define the file saver
	if len(file): #Proceed if user didn't press 'Cancel'
		global saveImage
		cv2.imwrite(file,saveImage)
	return
gui=tkinter.Tk()
gui.title("Binary Image")
class xy:
	def __init__(self,name):
		self.frame,self.x,self.y=tkinter.LabelFrame(gui,text=name),tkinter.IntVar(),tkinter.IntVar()
		self.frame.grid(column=0 if name=="Size" else 1,row=0)
		tkinter.Label(self.frame,text="X: ").grid(column=0,row=0)
		tkinter.Spinbox(self.frame,from_=1,to=1000,increment=1,justify=tkinter.CENTER,textvariable=self.x).grid(column=1,row=0)
		tkinter.Label(self.frame,text="Y: ").grid(column=0,row=1)
		tkinter.Spinbox(self.frame,from_=1,to=1000,increment=1,justify=tkinter.CENTER,textvariable=self.y).grid(column=1,row=1)
entry,preview,scale,size=tkinter.Text(gui),tkinter.Label(gui),xy("Scale"),xy("Size")
entry.grid(column=0,row=1),preview.grid(column=1,row=1)
tkinter.Button(gui,text="Save",command=lambda:save(filedialog.asksaveasfilename(title="Save",filetypes=(("JPEG files","*.jpg"),("All files","*.*"))))).grid(row=2,column=0,columnspan=2)
def main():
	global image,saveImage
	image=numpy.zeros((scale.y.get()*size.y.get(),scale.x.get()*size.x.get()),dtype="uint8")
	height,width=0,0
	for i in entry.get("0.0","end-1c"):
		if width==scale.x.get()*size.x.get() or i=='\n':
			height,width=height+scale.y.get(),0
		if height==scale.y.get()*size.y.get():
			break
		elif i=='0' or i=='1':
			if i=='1':
				image[height:height+scale.y.get(),width:width+scale.x.get()]=255
			width+=scale.x.get()
	saveImage=image
	image=ImageTk.PhotoImage(Image.fromarray(image))
	preview.config(image=image)
	gui.after(1,main)
	return
gui.after(1,main)
gui.mainloop()
