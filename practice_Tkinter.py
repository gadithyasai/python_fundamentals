#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Tkinter:
    Tkinter in Python GUI Programming is standard Python GUI library it gives us an object oriented interface to the 
    Tk GUI toolkit.


# In[ ]:





# In[10]:


import tkinter as tk

window = tk.Tk()

window.title('My first Tkinter')

window.mainloop()


# In[ ]:





# In[ ]:


Fundamentals of Tkinter:
    
    the sequesnce of operations in hamdling the Tkinter
    
    1. Import the Tkinter module
    
    2. Create the GUI application main window
        It is this window that we are performing the functions and displaying the visuals and everything
    
    3. Add widgets 
        (a widget is an element of GUI that display the information provided or provides a system to interacts with
         operating system or an application)
    
    4. Enter the main event loop 
        (An event loop is telling a code to display the window untill we close it manually)


# In[ ]:





# In[ ]:


Widgets:
    1.Label
    2.Button
    3.Entry
    4.Combo Box
    5.Check Button
    6.Radio
    7.Scrolled Text
    8.Spin Box
    9.Menu Bar
    10.Notebook


# In[ ]:





# In[ ]:


1. Label:
    Labels are used to create the Text or images on the window, but they have to be in a single line.


# In[25]:


import tkinter as tk

window = tk.Tk()

window.title('My first Tkinter')

label1=tk.Label(window, text='Hello World! Adithya.\n Good to see you here.', font=('times new roman',18,'bold'))

label1.grid(column=0,row=2) #will decide the location of display

window.geometry('300x200') #by defalut will display of 300x300 pixels sixe and can be stretched.

window.mainloop()


# In[ ]:





# In[ ]:


2. Button:
    it is similar to Label, but here we create a variable and widget syntax to define what the button has to do.
    we use grid funtion to set the position of button on window.


# In[6]:


import tkinter as tk

window = tk.Tk()

window.title('My first Tkinter')

label1=tk.Label(window, text='Hello World! Adithya.\n Good to see you here.', font=('times new roman',18,'bold'))

label1.grid(column=0,row=2) #will decide the location of display

btn1=tk.Button(window, text='Enter')

btn1.grid(column=1,row=2)

window.geometry('300x200') #by defalut will display of 300x300 pixels sixe and can be stretched.

window.mainloop()


# In[ ]:


""""Enchancement of button:
we can also define the foregroung(fg) and background(bg) colours of a button.
syntax: button(window,text='message',fg='color1',bg='color2')


# In[31]:


import tkinter as tk

window = tk.Tk()

window.title('My first Tkinter')

label1=tk.Label(window, text='Hello World! Adithya.\n Good to see you here.', font=('times new roman',18,'bold'))

label1.grid(column=0,row=2) #will decide the location of display

btn1=tk.Button(window, text='Enter',fg='black',bg='blue')

btn1.grid(column=1,row=2)

window.geometry('300x200') #by defalut will display of 300x300 pixels sixe and can be stretched.

window.mainloop()


# In[ ]:





# In[29]:


#Clickable button:

window =tk.Tk()

window.title('My Dash Board')

label2=tk.Label(window,text='Enter your number:',font=('times new roman',18,'bold'))

label2.grid(column=3,row=3)

btn1=tk.Button(window, text='Enter', command = clicked(), fg='black',bg='blue')

def clicked():
        
    Label2.configure(text='button clicked!')
    
btn1.grid(column=4,row=3)

window.geometry('300x200') #by defalut will display of 300x200 pixels sixe and can be stretched.

window.mainloop()


# In[ ]:





# In[ ]:


3. Entry :
    It is simple create input fields in GUI


# In[79]:


window =tk.Tk()

window.title('My Dash Board')

label2=tk.Label(window,text='Enter your number:',font=('times new roman',18,'bold'))

label2.grid(column=3,row=3)

txt = tk.Entry(window,width=10)

txt.grid(column=4,row=3)

def clicked():
    
    res= 'welcome to'+ txt.get()
    
    label2.configure(text=res) 

btn1=tk.Button(window, text='Enter', command = clicked(), fg='black',bg='blue')
  
btn1.grid(column=5,row=3)

window.geometry('300x200') #by defalut will display of 300x200 pixels size and can be stretched.

window.mainloop()


# In[ ]:





# In[ ]:


4. ComboBox:
    It is just a drop down menu with options


# In[47]:


from tkinter.ttk import*

window=tk.Tk()

combo=Combobox(window)

window.title('My Dash Board')

label2=tk.Label(window,text='Enter your number:',font=('times new roman',18,'bold'))

label2.grid(column=4,row=3)

combo['values']=(1,2,3,4,5,'Text')

combo.grid(column=5,row=3)

combo.current(0)

window.mainloop()


# In[ ]:





# In[ ]:


5. CheckButton:
    we use check button class to create check button widget.


# In[78]:


from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text="male", variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text="female", variable=var2).grid(row=1, sticky=W)
mainloop()


# In[77]:


from tkinter import *

window=tk.Tk()

window.title('My Dash Board')

label2=tk.Label(window,text='Enter your number:',font=('times new roman',18,'bold'))

label2.grid(column=4,row=3)

chk_status = IntVar()

chk_status.set(1)

chk=Checkbutton(window,text='choose',var=chk_status).grid(column=5,row=3)

window.mainloop()


# In[ ]:





# In[ ]:


6. RadioButton:
    


# In[63]:


from tkinter import *

window=tk.Tk()

window.title('My Dash Board')

radbtn1=Radiobutton(window,text='Java',value=1)

radbtn2=Radiobutton(window,text='C++',value=2)

radbtn3=Radiobutton(window,text='Python',value=3)

radbtn1.grid(column=0,row=0)

radbtn2.grid(column=1,row=1)

radbtn3.grid(column=2,row=2)

window.mainloop()


# In[ ]:





# In[ ]:


7. Scrolled Text:
    


# In[67]:





# In[72]:


#Create Scrolled Text widget in Python GUI Application  

import tkinter as tk  

from tkinter import ttk 

from tkinter import scrolledtext 

win = tk.Tk()  

win.title("My Dash Board")  

ttk.Label(win, text="This is Scrolled Text Area").grid(column=0,row=0)  

#Create Scrolled Text  

scrolW=30  

scrolH=4  

scr=scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD) 

# to isert the text in to scrolled region

scr.insert(INSERT,'welcome to python programming')

scr.grid(column=0, columnspan=3)  

win.geometry('300x200')

#Calling Main() 

win.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




