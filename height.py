#!/usr/bin/env python
# coding: utf-8

# In[64]:


from tkinter import *
from tkinter import messagebox
from math import sqrt


# In[226]:


root= Tk()
root.geometry('520x480+300+300')
root.resizable(False, False)
root.title('First Height Calculator')

def calculate():
    
    uinf= float(textInputVelocity.get())
    rho= float(textInputDenisty.get())
    mu= float(textInputViscosity.get())
    yP= float(textInputYPlus.get())
    l= float(textInputLength.get())
    
    Re= (rho*l*uinf)/mu
    cf= (0.026)/(Re**(1/7))
    tauWall= (cf*rho*uinf**2)/2
    uFric= sqrt(tauWall/rho)
#calculate first layer height
    dels= (yP*mu)/(uFric*rho)
    
    dataRe.set(Re)
    dataS.set(dels)
    
    
    

# Title
titleFrame= Frame(root)
titleFrame.grid()
lblTitle= Label(titleFrame, text= 'First Layer Height Calculator', font= ('Roboto', 20,'bold'), anchor= CENTER)
lblTitle.grid(padx=20, pady=20)
inputFrame= Frame(root)
inputFrame.grid()


# Velocty Input
velocityFrame= Frame(inputFrame)
velocityFrame.grid()
lblVelocity= Label(velocityFrame, text= 'Freestream Velocity (m/s)', padx= 20)
lblVelocity.grid()
lblVelocity.grid()
entryTextVelocity= StringVar()
textInputVelocity= Entry(velocityFrame, textvariable= entryTextVelocity, font= ('Roboto',12))
textInputVelocity.grid(row= 0, column= 1, padx= 10, pady= 10)
####################

# Denisty Input
densityFrame= Frame(inputFrame)
densityFrame.grid()
lblDensity= Label(densityFrame, text= 'Density (kg/m3)', padx= 44)
lblDensity.grid()
entryTextDensity= StringVar()
textInputDenisty= Entry(densityFrame, textvariable= entryTextDensity, font= ('Roboto',12))
textInputDenisty.grid(row= 0, column= 1, padx= 10, pady= 10)

# Viscosity Input
viscosityFrame= Frame(inputFrame)
viscosityFrame.grid()
lblViscosity= Label(viscosityFrame, text= 'Dynamic Viscosity (kg/ms)', padx= 15)
lblViscosity.grid()
entryTextViscosity= StringVar()
textInputViscosity= Entry(viscosityFrame, textvariable= entryTextViscosity, font= ('Roboto',12))
textInputViscosity.grid(row= 0, column= 1, padx= 10, pady= 10)

# Length Input
lengthFrame= Frame(inputFrame)
lengthFrame.grid()
lblLength= Label(lengthFrame, text= 'Reference Length (m)', padx= 28)
lblLength.grid()
entryTextLength= StringVar()
textInputLength= Entry(lengthFrame, textvariable= entryTextLength, font= ('Roboto',12))
textInputLength.grid(row= 0, column= 1, padx= 10, pady= 10)

# YPlus Input
yPlusFrame= Frame(inputFrame)
# yPlusFrame.pack()
yPlusFrame.grid()
lblYPlus= Label(yPlusFrame, text= 'Desired Y+', padx= 55)
lblYPlus.grid()
# lblYPlus.pack(side= LEFT)
entryTextYpus= StringVar()
textInputYPlus= Entry(yPlusFrame, textvariable= entryTextYpus, font= ('Roboto',12))
# textInputYPlus.pack(expand= True, fill= 'both')
textInputYPlus.grid(row= 0, column= 1, padx= 10, pady= 10)

# Calculate Button 

calcButton= Frame(inputFrame)
calcButton.grid()
dataRe= StringVar()
dataS= StringVar()
btn= Button(calcButton, text= 'Calculate wall distance', command= calculate)
btn.grid(padx= 10, pady= 10)



# Displaying output

# Reynolds Number
outputFrame= Frame(root)

outputFrame.grid()
ReFrame= Frame(outputFrame)
ReFrame.grid()
displayRe= Label(ReFrame, font= ('Roboto',12), text= 'Reynolds number: ')
displayRe.grid(pady= 20)

textOutput= Label(ReFrame, font= ('Roboto',12), textvariable= dataRe)
textOutput.grid(row= 0, column= 1)


distFrame= Frame(outputFrame)
distFrame.grid()
displayYp= Label(distFrame, font= ('Roboto',12), text= 'First layer height (m): ')
displayYp.grid()

textOutput= Label(distFrame, font= ('Roboto',12), textvariable= dataS)
textOutput.grid(row=0 ,column=1)



# Main Loop
root.mainloop()

