from tkinter import *
import sys
import math
Cmu= 0.09
def turbKE(uInf, turbInt):
    return 1.5*(uInf*(turbInt/100))**2
    

def epsilonLength(lengthScale, turbKE):
    return (Cmu)*(turbKE**1.5/lengthScale)

def epsilonVisc(turbVisc, turbKE, nu):
    return Cmu*((turbKE**2)/nu)*(turbVisc**-1)
    
def omegaLength(lengthScale, turbKE):
    return math.sqrt(turbKE)/lengthScale

def omegaVisc(turbKE,nu, turbVisc):
    return (turbKE/nu)*(turbVisc)**-1


def main():
    empty= ''
    if v.get()==0:
        Uinf= float(velocityEntry.get())
        turbInt= float(turbIntEntry.get())
        lengthScale= float(lengthEntry.get())

        tKE= turbKE(Uinf, turbInt)
        eps= epsilonLength(lengthScale, tKE)
        omg= omegaLength(lengthScale, tKE)

        datake.set(tKE)
        datae.set(eps)
        dataw.set(omg)
        
        if (turbViscEntry.get()) or (kViscEntry.get())!= '':
            
            entryTextVelocity.set(empty)
            entryTextTurbInt.set(empty)
            entryTextLength.set(empty)
            entryTextKVisc.set(empty)
            entryTextTurbVisc.set(empty)
            datake.set(empty)
            datae.set(empty)
            dataw.set(empty)
            
    
    elif v.get()==1:
        Uinf= float(velocityEntry.get())
        turbVisc= float(turbViscEntry.get())
        nu= float(kViscEntry.get())
        turbInt= float(turbIntEntry.get())
        
        tKE= turbKE(Uinf, turbInt)
        eps= epsilonVisc(turbVisc, tKE, nu)
        omg= omegaVisc(tKE, nu, turbVisc)
        
        datake.set(tKE)
        datae.set(eps)
        dataw.set(omg)
        
        if lengthEntry.get()!='':
            entryTextVelocity.set(empty)
            entryTextTurbInt.set(empty)
            entryTextLength.set(empty)
            entryTextKVisc.set(empty)
            entryTextTurbVisc.set(empty)
            datake.set(empty)
            datae.set(empty)
            dataw.set(empty)

def reset():
    
    empty= ''
    entryTextVelocity.set(empty)
    entryTextTurbInt.set(empty)
    entryTextLength.set(empty)
    entryTextKVisc.set(empty)
    entryTextTurbVisc.set(empty)
    datake.set(empty)
    datae.set(empty)
    dataw.set(empty)
    
    
################
root= Tk()
root.geometry('520x640+500+100')
root.resizable(False, False)
root.title('Turbulence Properties Calculator')

# Title
titleFrame= Frame(root)
titleFrame.grid()
lblTitle= Label(titleFrame, text= 'Turbulence Properties Calculator', font= ('Courier New', 18,'bold'), anchor= CENTER)
lblTitle.grid(padx=20, pady=20)
inputFrame= Frame(root)
inputFrame.grid()

# Frames
choiceFrame= Frame(root)
choiceFrame.grid()
inputFrame= Frame(root)
inputFrame.grid()
outputFrame= Frame(root)
outputFrame.grid()

# Radio Buttons 
v = IntVar()
v.set(0) 
choices= [('Calculate k, \u03B5 and \u03C9 from Uinf, Tu and Tl',0), 
          ('Calculate k, \u03B5 and \u03C9 from Uinf, Tu and \u03BCt/\u03BC',1)]
    
# Label(choiceFrame, text= 'Select one', justify= LEFT, padx= 20).grid()

for choice, val in choices:
    Radiobutton(choiceFrame, text= choice, padx= 20, variable=v, value= val).grid()

# Input values
velocityFrame= Frame(inputFrame)
velocityFrame.grid()
lblVelocity= Label(velocityFrame, text= 'Freestream Velocity (Uinf)', padx= 17, font= ('Courier New',10))
lblVelocity.grid()
entryTextVelocity= StringVar()
velocityEntry= Entry(velocityFrame, textvariable= entryTextVelocity, font= ('Courier New',12))
velocityEntry.grid(row= 0, column= 1, padx= 10, pady= 10)

turbIntFrame= Frame(inputFrame)
turbIntFrame.grid()
lblturbInt= Label(turbIntFrame, text= 'Turbulent Intensity (Tu)', padx= 17, font= ('Courier New',10))
lblturbInt.grid()
entryTextTurbInt= StringVar()
turbIntEntry= Entry(turbIntFrame, textvariable= entryTextTurbInt, font= ('Courier New',12))
turbIntEntry.grid(row= 0, column= 1, padx= 10, pady= 10)

lengthFrame= Frame(inputFrame)
lengthFrame.grid()
lbllength= Label(lengthFrame, text= 'Length Scale (Tl)', padx= 17, font= ('Courier New',10))
lbllength.grid()
entryTextLength= StringVar()
lengthEntry= Entry(lengthFrame, textvariable= entryTextLength, font= ('Courier New',12))
lengthEntry.grid(row= 0, column= 1, padx= 10, pady= 10)

turbViscFrame= Frame(inputFrame)
turbViscFrame.grid()
lblturbVisc= Label(turbViscFrame, text= 'Turbulent Viscosity ratio (\u03BCt/\u03BC)', padx= 17, font= ('Courier New',10))
lblturbVisc.grid()
entryTextTurbVisc= StringVar()
turbViscEntry= Entry(turbViscFrame, textvariable= entryTextTurbVisc, font= ('Courier New',12))
turbViscEntry.grid(row= 0, column= 1, padx= 10, pady= 10)

kViscFrame= Frame(inputFrame)
kViscFrame.grid()
lblkVisc= Label(kViscFrame, text= 'Kinematic Viscosity (\u03BD)', padx= 17, font= ('Courier New',10))
lblkVisc.grid()
entryTextKVisc= StringVar()
kViscEntry= Entry(kViscFrame, textvariable= entryTextKVisc, font= ('Courier New',12))
kViscEntry.grid(row= 0, column= 1, padx= 10, pady= 10)


# Calculate Button 

calcButton= Frame(inputFrame)
calcButton.grid()
datake= StringVar()
datae= StringVar()
dataw= StringVar()
btn= Button(calcButton, text= 'Calculate',  font= ('Courier New',10), command= main)
btn.grid()

resetButton= Frame(inputFrame)
resetButton.grid()
btnreset= Button(resetButton, text= 'Reset', command= reset, font= ('Courier New',10))
btnreset.grid(pady= 20)


# Output Frame

outputFrame.grid()
keFrame= Frame(outputFrame)
keFrame.grid()
displayke= Label(keFrame, font= ('Courier New',12), text= 'k (m2/s2) = ')
displayke.grid(pady= 10)

textOutput= Label(keFrame, font= ('Courier New',12), textvariable= datake)
textOutput.grid(row= 0, column= 1)


epsFrame= Frame(outputFrame)
epsFrame.grid()
displayeps= Label(epsFrame, font= ('Courier New',12), text= '\u03B5 (m2/s3)= ')
displayeps.grid(pady= 10)

textOutput= Label(epsFrame, font= ('Courier New',12), textvariable= datae)
textOutput.grid(row=0 ,column=1)

omFrame= Frame(outputFrame)
omFrame.grid()
displayom= Label(omFrame, font= ('Courier New',12), text= '\u03C9 (1/s)= ')
displayom.grid(pady= 10)

textOutput= Label(omFrame, font= ('Courier New',12), textvariable= dataw)
textOutput.grid(row=0 ,column=1)


root.mainloop()
