from tkinter import *

root = Tk()
root.title("Temperature Converter")
root.geometry("400x350")
#root.minsize(width= 400, height=100)
#root.maxsize(width= 400, height=100)
root.config(bg = "cyan")


def get_temp():
	Height = int(temp1.get())
	Weight = int(temp2.get())
	Height = Height/100
	BMI=Weight/(Height*Height)
	print(BMI)
	text = ''
	if(BMI>0):
		if(BMI<=16):
			text+=("you are severely underweight")
		elif(BMI<=18.5):
			text+=("you are underweight")
		elif(BMI<=25):
			text+=("you are Healthy")
		elif(BMI<=30):
			text+=("you are overweight")
		else:
			text+=("you are severely overweight")
	else:
		text+=("enter valid details")
	T=Label(text = round(BMI,2), bg  = "cyan",font = "comicsans 15")
	T.grid(row=3,column= 1,padx= 10,pady =10)
	e=Label(text = text, bg  = "cyan",font = "comicsans 15")
	e.grid(row=4,columnspan= 2,padx= 10,pady =10)



temp1 = StringVar()
temp2 = StringVar()

#Labels and Buttons
Height = Entry(root,textvariable = temp1)
Height.grid(row=0,padx= 10,pady =50)

label = Label(root,text = "Height in Cm", bg  = "cyan",font = "comicsans 15")
label.grid(row=0,column=1,padx= 10,pady =10)

Height = Entry(root,textvariable = temp2)
Height.grid(row=1,padx= 10,pady =10)

label = Label(root,text = "Weight in Kg", bg  = "cyan",font = "comicsans 15")
label.grid(row=1,column=1,padx= 10,pady =10)

button = Button(root,text = "CALCULATE",font = "comicsans",
							bg = "navajo white",command = get_temp)

button.grid(rows=2,column=0,padx= 10,pady =10)

root.mainloop()
