
from tkinter import *
from math import sqrt
import pyperclip


# In[226]:


root= Tk()
root.geometry('520x480+300+100')
root.resizable(False, False)
root.title('First Layer Height Calculator')

root.call('wm', 'iconphoto', root._w, PhotoImage(file='icon2.png')) 

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
    pyperclip.copy(dels)
    print('Layer height copied to clipboard')
    

def reset():
    empty= ''
    entryTextVelocity.set(empty)
    entryTextDensity.set(empty)
    entryTextViscosity.set(empty)
    entryTextLength.set(empty)
    entryTextYpus.set(empty)
    dataRe.set(empty)
    dataS.set(empty)
    

# Title
titleFrame= Frame(root)
titleFrame.grid()
lblTitle= Label(titleFrame, text= 'First Layer Height Calculator', font= ('Courier New', 20,'bold'), anchor= CENTER)
lblTitle.grid(padx=20, pady=20)
inputFrame= Frame(root)
inputFrame.grid()


# Velocty Input
velocityFrame= Frame(inputFrame)
velocityFrame.grid()
lblVelocity= Label(velocityFrame, text= 'Freestream Velocity (m/s)', padx= 17, font= ('Courier New',10))
lblVelocity.grid()
lblVelocity.grid()
entryTextVelocity= StringVar()
textInputVelocity= Entry(velocityFrame, textvariable= entryTextVelocity, font= ('Courier New',12))
textInputVelocity.grid(row= 0, column= 1, padx= 10, pady= 10)


# Denisty Input
densityFrame= Frame(inputFrame)
densityFrame.grid()
lblDensity= Label(densityFrame, text= 'Density (kg/m3)', padx= 55, font= ('Courier New',10))
lblDensity.grid()
entryTextDensity= StringVar()
textInputDenisty= Entry(densityFrame, textvariable= entryTextDensity, font= ('Courier New',12))
textInputDenisty.grid(row= 0, column= 1, padx= 10, pady= 10)

# Viscosity Input
viscosityFrame= Frame(inputFrame)
viscosityFrame.grid()
lblViscosity= Label(viscosityFrame, text= 'Dynamic Viscosity (kg/ms)', padx= 13, font= ('Courier New',10))
lblViscosity.grid()
entryTextViscosity= StringVar()
textInputViscosity= Entry(viscosityFrame, textvariable= entryTextViscosity, font= ('Courier New',12))
textInputViscosity.grid(row= 0, column= 1, padx= 10, pady= 10)

# Length Input
lengthFrame= Frame(inputFrame)
lengthFrame.grid()
lblLength= Label(lengthFrame, text= 'Reference Length (m)', padx= 30,  font= ('Courier New',10))
lblLength.grid()
entryTextLength= StringVar()
textInputLength= Entry(lengthFrame, textvariable= entryTextLength, font= ('Courier New',12))
textInputLength.grid(row= 0, column= 1, padx= 10, pady= 10)

# YPlus Input
yPlusFrame= Frame(inputFrame)
# yPlusFrame.pack()
yPlusFrame.grid()
lblYPlus= Label(yPlusFrame, text= 'Desired Y+', padx= 69,  font= ('Courier New',10))
lblYPlus.grid()
# lblYPlus.pack(side= LEFT)
entryTextYpus= StringVar()
textInputYPlus= Entry(yPlusFrame, textvariable= entryTextYpus, font= ('Courier New',12))
# textInputYPlus.pack(expand= True, fill= 'both')
textInputYPlus.grid(row= 0, column= 1, padx= 10, pady= 10)

# Calculate Button 

calcButton= Frame(inputFrame)
calcButton.grid()
dataRe= StringVar()
dataS= StringVar()
btn= Button(calcButton, text= 'Calculate wall distance', command= calculate, font= ('Courier New',10))
btn.grid(padx= 10, pady= 10)

# Reset Button
resetButton= Frame(inputFrame)
resetButton.grid()
btnreset= Button(resetButton, text= 'Reset', command= reset, font= ('Courier New',10))
btnreset.grid()


# Displaying output

# Reynolds Number
outputFrame= Frame(root)

outputFrame.grid()
ReFrame= Frame(outputFrame)
ReFrame.grid()
displayRe= Label(ReFrame, font= ('Courier New',12), text= 'Reynolds number: ')
displayRe.grid(pady= 20)

textOutput= Label(ReFrame, font= ('Courier New',12), textvariable= dataRe)
textOutput.grid(row= 0, column= 1)


distFrame= Frame(outputFrame)
distFrame.grid()
displayYp= Label(distFrame, font= ('Courier New',12), text= 'First layer height (m): ')
displayYp.grid()

textOutput= Label(distFrame, font= ('Courier New',12), textvariable= dataS)
textOutput.grid(row=0 ,column=1)




# Main Loop
root.mainloop()

