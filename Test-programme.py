#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 18:08:43 2021

@author: macbook
"""
from tkinter import *
import csv
import tkinter.font as tkFont
import random
from datetime import datetime
import numpy as np
import time

breaktime = False
fix1 = False
fix2 = False
saveIndicator = "pre"
filename = ""
Subjectnumber = ""



demotime = 6
democounter = 6
stresstime = 3
stresscounter = 3
originalTimer = 0
BFtime = 0

initiate = 1
demoscore,demoproblemcount = 0, 0
stressscore, stressproblemcount = 0, 0
rightoption = 100

randomStressOrder = random.randrange(2)
randomBreakOrder = random.randrange(2)

def save_info():
    global saveIndicator, starttime, filename, Subjectnumber,stressscore,stressproblemcount
     
    Subjectnumber = no.get()
    filename = "Subject%s.csv" % Subjectnumber
    
    if saveIndicator == "pre":
        gender_info = gender.get()
        worktype_info = worktype.get()
        age_info = age.get()
        BFexperience_info = BFexperience.get()
        Q1_info = Q1.get()
        Q2_info = Q2.get()
        Q3_info = Q3.get()
        Q4_info = Q4.get()
         
        with open(filename,"w",newline="") as f:
            write = csv.writer(f)
            write.writerow(["Subjectnumber","starttime","gender","worktype","age","BFexp","Q1","Q2","Q3","Q4"])
            write.writerow([Subjectnumber,starttime,gender_info,worktype_info,age_info,BFexperience_info,Q1_info,Q2_info,Q3_info,Q4_info])

    else:     
        with open(filename,"a",newline="") as f:
            write = csv.writer(f)
            #write.writerow(["Subjectnumber","starttime","gender","worktype","age","BFexp","Q1","Q2","Q3","Q4"])
            write.writerow([Subjectnumber,saveIndicator,stressscore,stressproblemcount,starttime,BQ1.get(),BQ2.get(),BQ3.get(),BQ4.get(),BQ5.get(),BQ6.get(),BQ7.get(),BQ8.get(),BQ9.get(),BQ10.get(),BQ11.get(),BQ12.get(),BQ12.get(),BQ13.get(),BQ14.get(),BQ15.get(),BQ16.get(),SART1.get(),SART2.get(),TLXMDemand.get(),TLXTDemand.get(),TLXEffort.get(),TLXPerformance.get(),TLXFrustration.get()])
          
    print("successfully saved " + saveIndicator)

  #gender_entry.delete(0, END)
  #worktype_entry.delete(0, END)
  #age_entry.delete(0, END)
  
def changepage():
    global pagenum, screen, initiate, continuousTimer, starttime, saveIndicator, randomBreakOrder, randomStressOrder, fix1, fix2

    for widget in screen.winfo_children():
        widget.destroy()
    
    if initiate == 2:
        fix1 = False
        fix2 = True
        Breakquestions(continuousTimer)
        print("Will this work?")
        return
    if initiate == 3:
        fix2 = False
        Breakquestionspage2(continuousTimer)
        print("Maybe even this?")
        return
    
    initiate = 1
    print("what is going on?")
    if pagenum == 1:
        page2(screen)
        pagenum = 2
    elif pagenum == 2:
        page3(10)
        pagenum = 3
    elif pagenum == 3:
        starttime = datetime.now()
        save_info()
        page4(30) #demo session
        pagenum = 4
    elif pagenum == 4:
        page5(10) #stress introduction
        pagenum = 5
        
    elif pagenum == 5:
        starttime = datetime.now()
        if randomStressOrder == 0:
            Stress1(180)                     #180
            saveIndicator = "Stress1"
            print("Are we here?")
        else:
            Stress3(240)                     #240
            saveIndicator = "Stress3"
            print("Or is it here?")
        pagenum = 6  
        
    elif pagenum == 6:
        fix1=True
        Break(150)                           #150
        pagenum = 7
        
    elif pagenum == 7:
        save_info()
        starttime = datetime.now()
        if randomBreakOrder == 0:
            Relax1(180)                      #180
            saveIndicator = "Relax1"
        else:
            Relax2(180)                      #180
            saveIndicator = "Relax2"
        pagenum = 8

    elif pagenum == 8:
        fix1=True
        Break(120)                           #120
        pagenum = 9
    
    elif pagenum == 9:
        save_info()
        page5(10) #Stress introduction
        pagenum = 10
        
    elif pagenum == 10:
        
        starttime = datetime.now()
        if randomStressOrder == 1:
            Stress1(180)                     #180
            saveIndicator = "Stress1"
        else:
            Stress3(240)                     #240
            saveIndicator = "Stress3"
        pagenum = 11  
        
    elif pagenum == 11:
        fix1=True
        Break(120)                           #120
        pagenum = 12
        
    elif pagenum == 12:
        save_info()
        starttime = datetime.now()
        if randomBreakOrder == 1:
            Relax1(180)                      #180
            saveIndicator = "Relax1"
        else:
            Relax2(180)                      #180
            saveIndicator = "Relax2"
        pagenum = 13 
        
    elif pagenum == 13:
        fix1=True
        Break(120)                           #120
        pagenum = 14

    elif pagenum == 14:
        save_info()
        end(1000)
        pagenum = 15  
        
    else:
        page1(screen)
        pagenum = 1


def mathproblem():
    mathtype=random.randrange(1,3)
    space_buttons = []    
    global ButtonState
    if mathtype == 1:
        while True:
            sumofproduct=random.randrange(11,17)
            firstnumber = random.randrange(3,8)
            secondnumber = sumofproduct - firstnumber
            answer = firstnumber*secondnumber
            wronganswer1 = (firstnumber*secondnumber)+random.randrange(-11,11)
            wronganswer2 = (firstnumber*secondnumber)+random.randrange(-11,11)
            
            if firstnumber%10 == 0 or secondnumber%10 == 0 or answer == wronganswer1 or answer == wronganswer2 or wronganswer1 == wronganswer2:
                firstnumber = random.randrange(3,13)
                secondnumber = sumofproduct - firstnumber
            else:
                break
            
        Label(text=f'{firstnumber} * {secondnumber} =         ',font=("Helvetica",60),justify=LEFT).place(x=100,y=260)

    
    if mathtype == 2:
        while True:
            firstnumber = random.randrange(60,99)
            secondnumber = random.randrange(30,60)
            answer = firstnumber-secondnumber
            wronganswer1 = (firstnumber-secondnumber)+random.randrange(-14,14)
            wronganswer2 = (firstnumber-secondnumber)+random.randrange(-14,14)
            
            if firstnumber%10 != 0 and secondnumber%10 != 0 and answer != wronganswer1 and answer != wronganswer2 and wronganswer1 != wronganswer2:
                break
        
        Label(text=f'{firstnumber} - {secondnumber} =         ',font=("Helvetica",60),justify=LEFT).place(x=100,y=260)


    if mathtype == 3:
        while True:
            firstnumber = random.randrange(40,110)
            secondnumber = random.randrange(40,110)
            answer = firstnumber+secondnumber
            wronganswer1 = (firstnumber+secondnumber)+random.randrange(-24,24)
            wronganswer2 = (firstnumber+secondnumber)+random.randrange(-24,24)
            
            if answer != wronganswer1 and answer != wronganswer2 and wronganswer1 != wronganswer2:
                break
        
        Label(text=f'{firstnumber} + {secondnumber} =         ',font=("Helvetica",60),justify=LEFT).place(x=100,y=260)
    
    #while space_buttons: #same as while len(space_buttons)>0:
        #space_buttons.pop().destroy() #remove existing buttons
    #ButtonState = DISABLED      
    rightopt = random.randrange(1,3)    
    if rightopt == 1:
        space_button=Radiobutton(screen,text=f"   {answer}   ",font=("Helvetica",30), variable=opt, value=1,state="disabled")
        space_button.place(x=100,y=370)
        space_buttons.append(space_button)
        
        space_button=Radiobutton(screen,text=f"   {wronganswer1}   ",font=("Helvetica",30), variable=opt, value=2,state="disabled")
        space_button.place(x=100,y=420)
        space_buttons.append(space_button)
        space_button=Radiobutton(screen,text=f"   {wronganswer2}   ",font=("Helvetica",30), variable=opt, value=3,state="disabled")
        space_button.place(x=100,y=470)
        space_buttons.append(space_button)
    elif rightopt == 2:
        space_button=Radiobutton(screen,text=f"   {wronganswer1}   ",font=("Helvetica",30), variable=opt, value=1,state="disabled")
        space_button.place(x=100,y=370)
        space_buttons.append(space_button)
        space_button=Radiobutton(screen,text=f"   {answer}   ",font=("Helvetica",30), variable=opt, value=2,state="disabled")
        space_button.place(x=100,y=420)
        space_buttons.append(space_button)
        space_button=Radiobutton(screen,text=f"   {wronganswer2}   ",font=("Helvetica",30), variable=opt, value=3,state="disabled")
        space_button.place(x=100,y=470)
        space_buttons.append(space_button)
    elif rightopt == 3:
        space_button=Radiobutton(screen,text=f"   {wronganswer2}",font=("Helvetica",30), variable=opt, value=1,state="disabled")
        space_button.place(x=100,y=370)
        space_buttons.append(space_button)
        space_button=Radiobutton(screen,text=f"   {wronganswer1}",font=("Helvetica",30), variable=opt, value=2,state="disabled")
        space_button.place(x=100,y=420)
        space_buttons.append(space_button)
        space_button=Radiobutton(screen,text=f"   {answer}",font=("Helvetica",30), variable=opt, value=3,state="disabled")
        space_button.place(x=100,y=470)
        space_buttons.append(space_button)
    
    for button in space_buttons:
        button.config(state="disabled")

    screen.after(800,activateButtons,space_buttons)
    #for button in space_buttons:
        #button.configure(state="normal")
        
    return rightopt

def activateButtons(space_buttons):
    for button in space_buttons:
        button.configure(state="normal")
    


def page1(screen):
    screen.geometry("1280x800")
    page = Frame(screen)
    #Label(page, text = 'This is page 1').grid(row = 0)
    #Button(page, text = 'To page 2', command = changepage).grid(row = 1)
    heading = Label(text = "PRE-QUESTIONNAIRE", fg = "black", width = "500", height = "3", font=('Helvatical bold',20))
    heading.pack()

    
    genderframe = LabelFrame(screen, text='What is your gender?',font=("Helvetica",16,"bold"))
    genderframe.pack(padx=30, side=LEFT)
    genderframe.place(x = 15, y = 90)
    Radiobutton(genderframe, text='Female', variable=gender, value=1).pack(anchor=W)
    Radiobutton(genderframe, text="Male", variable=gender, value=2).pack(anchor=W)
    Radiobutton(genderframe, text="Prefer not to specify", variable=gender, value=3).pack(anchor=W)
    
    workframe = LabelFrame(screen, text='What type of work do you do?',font=("Helvetica",16,"bold"))
    workframe.pack(padx=30, side=LEFT)
    workframe.place(x = 15, y = 210)
    Radiobutton(workframe, text="Student", variable=worktype, value=1).pack(anchor=W)
    Radiobutton(workframe, text='Information work (mostly computer)', variable=worktype, value=2).pack(anchor=W)
    Radiobutton(workframe, text="Manual work (mostly physical)", variable=worktype, value=3).pack(anchor=W)
    
    BFframe = LabelFrame(screen, text='How familiar are you with reading data on your healt and behaviour? Do you\nhave a great deal of relevant experience (high) or is it a new situation (low)', font=("Helvetica",16,"bold"))
    BFframe.pack(padx=30, side=LEFT)
    BFframe.place(x = 15, y = 330)
    
    Radiobutton(BFframe, text="1  Not very familiar", variable=BFexperience, value=1,justify=LEFT).pack(anchor=W)
    Radiobutton(BFframe, text='2', variable=BFexperience, value=2,justify=LEFT).pack(anchor=W)
    Radiobutton(BFframe, text='3', variable=BFexperience, value=3,justify=LEFT).pack(anchor=W)
    Radiobutton(BFframe, text='4  I sometimes look at basic health data (e.g. step\ncounts, heart rate, or similar)', variable=BFexperience, value=4,justify=LEFT).pack(anchor=W)
    Radiobutton(BFframe, text='5', variable=BFexperience, value=5,justify=LEFT).pack(anchor=W)
    Radiobutton(BFframe, text='6', variable=BFexperience, value=6,justify=LEFT).pack(anchor=W)
    Radiobutton(BFframe, text="7  I’m very used to tracking data on myself(e.g. graphs\non sleep patterns, sports performance or similar)", variable=BFexperience, value=7,justify=LEFT).pack(anchor=W)
    
    
    
    age_text = Label(text = "Age",font=("Helvetica",16,"bold"))
    age_text.place(x = 15, y = 610)
    age_entry = Entry(textvariable = age, width = "20")
    age_entry.place(x = 15, y = 640)
    
    Label(text = "Subject no.").place(x = 1100, y = 90)
    Entry(textvariable = no, width = "10").place(x = 1100, y = 115)
 
    
    Next = Button(screen,text = "Next", width = "30", height = "2", command = changepage, bg = "grey")
    Next.place(x = 900, y = 670)

def page2(screen):
    screen.geometry("1280x800")
    page = Frame(screen)
    
    #Label(page, text = 'This is page 1').grid(row = 0)
    #Button(page, text = 'To page 2', command = changepage).grid(row = 1)
    #heading = Label(screen, text = " ", fg = "black", width = "500", height = "2", font=('Helvatical bold',20))
    #heading.pack()
    

    #genderframe = LabelFrame(screen, text='something else')
    #genderframe.pack(padx=30, side=LEFT)
    #genderframe.place(x = 15, y = 90)
    Label(screen, text ="Never").grid(row=0, column=2, padx=3)
    Label(screen, text ="Almost\nNever").grid(row=0, column=3, padx=3)
    Label(screen, text ="Sometimes").grid(row=0, column=4, padx=3)
    Label(screen, text ="Fairly\noften").grid(row=0, column=5, padx=3)
    Label(screen, text ="Very\noften").grid(row=0, column=6, padx=3)
   
    Label(screen, text = "In the last month, how often have you\nfelt that you were unable to control\nthe important things in your life?", justify=LEFT).grid(row=1, column=0, columnspan=2, padx=10,pady=20, sticky=W)
    Radiobutton(screen, variable=Q1, value=0).grid(row=1, column=2)
    Radiobutton(screen, variable=Q1, value=1).grid(row=1, column=3)
    Radiobutton(screen, variable=Q1, value=2).grid(row=1, column=4)
    Radiobutton(screen, variable=Q1, value=3).grid(row=1, column=5)
    Radiobutton(screen, variable=Q1, value=4).grid(row=1, column=6)
    
    Label(screen, text = "In the last month, how often have you\nfelt confident about your ability to\nhandle your personal problems?", justify=LEFT).grid(row=2, column=0, columnspan=2, padx=10,pady=20, sticky=W)
    Radiobutton(screen, variable=Q2, value=0).grid(row=2, column=2)
    Radiobutton(screen, variable=Q2, value=1).grid(row=2, column=3)
    Radiobutton(screen, variable=Q2, value=2).grid(row=2, column=4)
    Radiobutton(screen, variable=Q2, value=3).grid(row=2, column=5)
    Radiobutton(screen, variable=Q2, value=4).grid(row=2, column=6)
    
    Label(screen, text = "In the last month, how often have you\nfelt that things were going your way?", justify=LEFT).grid(row=3, column=0, columnspan=2, padx=10,pady=20, sticky=W)
    Radiobutton(screen, variable=Q3, value=0).grid(row=3, column=2)
    Radiobutton(screen, variable=Q3, value=1).grid(row=3, column=3)
    Radiobutton(screen, variable=Q3, value=2).grid(row=3, column=4)
    Radiobutton(screen, variable=Q3, value=3).grid(row=3, column=5)
    Radiobutton(screen, variable=Q3, value=4).grid(row=3, column=6)
    
    Label(screen, text = "In the last month, how often have you\nfelt difficulties were piling up so\nhigh that you could not overcome them?", justify=LEFT).grid(row=4, column=0, columnspan=2, padx=10,pady=20, sticky=W)
    Radiobutton(screen, variable=Q4, value=0).grid(row=4, column=2)
    Radiobutton(screen, variable=Q4, value=1).grid(row=4, column=3)
    Radiobutton(screen, variable=Q4, value=2).grid(row=4, column=4)
    Radiobutton(screen, variable=Q4, value=3).grid(row=4, column=5)
    Radiobutton(screen, variable=Q4, value=4).grid(row=4, column=6)
    #workframe = LabelFrame(screen, text='What type of work do you do?')
    #workframe.pack(padx=30, side=LEFT)
    #workframe.place(x = 15, y = 210)
    #Radiobutton(workframe, text="Student", variable=worktype, value=1).pack(anchor=W)
    #Radiobutton(workframe, text='Information work (mostly computer)', variable=worktype, value=2).pack(anchor=W)
    #Radiobutton(workframe, text="Manual work (mostly physical)", variable=worktype, value=3).pack(anchor=W)
    
    
    Next = Button(screen,text = "Next", width = "30", height = "2", command = changepage, bg = "grey")
    Next.place(x = 900, y = 670)

def page3(timer):
    screen.geometry("1280x800")
    page = Frame(screen)
    Label(text="DEMO-SESSION",font=("Helvetica",60),justify=LEFT).place(x=100,y=260)
    Label(text="This session will demonstrate the test format. Complete the\nmath problems - you have a maximum of 6 seconds\nfor each.The demo-exercise will start shortly.",font=("Helvetica",20),justify=LEFT).place(x=100,y=340)
    #Label(text=f'Next slide in: {timer} sec    ').place(x=15,y=700)
    timer -= 1
    if timer != -1:
        screen.after(1000, page3, timer)
    else:
        changepage()
        return
    
    
def page4(timer):
    screen.geometry("1280x800")
    page = Frame(screen)
    Label(text=f'Next slide in: {timer} sec     ').place(x=15,y=700)
    global democounter
    global demotime
    global demoscore
    global rightoption
    global initiate
    global demoproblemcount
    option=opt.get()   
    
    if initiate == 1:
        rightoption = mathproblem()
        initiate = 0
    
    if option == rightoption:
        demoscore += 1
        demoproblemcount += 1
        print("right. Demoscore: ",demoscore)
        democounter = demotime
        opt.set(0)
        rightoption = mathproblem()
        
    elif option != rightoption and option > 0:
        demoproblemcount += 1
        print("wrong")
        democounter = demotime
        opt.set(0)
        rightoption = mathproblem()
        
    else:
        democounter -= 1
        opt.set(0)
        
    if democounter == 0:
        demoproblemcount += 1
        democounter = demotime
        rightoption = mathproblem()
        
    timer -= 1 
    if timer != -1:
        screen.after(1000,page4,timer)
    else:
        changepage()
        return

def page5(timer):
    screen.geometry("1280x800")
    page = Frame(screen)
    Label(text="EXERCISE",font=("Helvetica",60),justify=LEFT).place(x=100,y=260)
    Label(text="Complete as many problems as you can, while trying to\nstay as relaxed as possible. You now have 3 seconds\nfor each question. The exercises will start shortly.",font=("Helvetica",20),justify=LEFT).place(x=100,y=340)
    #Label(text=f'Next slide in: {timer} sec    ').place(x=15,y=700)
    timer -= 1
    if timer != -1:
        screen.after(1000, page5, timer)
    else:
        changepage()
        return

def end(timer):
    screen.geometry("1280x800")
    page = Frame(screen)
    Label(text="THAT'S IT! :)",font=("Helvetica",60),justify=LEFT).place(x=100,y=260)
    Label(text="Thank you so much for participating! Please head out and call the facilitator.",font=("Helvetica",20),justify=LEFT).place(x=100,y=340)
    #Label(text=f'Next slide in: {timer} sec    ').place(x=15,y=700)
    timer -= 1
    if timer != -1:
        screen.after(1000, end, timer)
    else:
        changepage()
        return    
    
    
def Break(timer):
    global continuousTimer, initiate, fix1, originalTimer
    if fix1:
        screen.geometry("1280x800")
        page = Frame(screen)
        Label(text="BREAK-SESSION",font=("Helvetica",60),justify=LEFT).place(x=100,y=260)
        Label(text="Answer how much you agree with the following statements\nabout the activity you just finished. When finished,\nrelax until the timer runs out.",font=("Helvetica",20),justify=LEFT).place(x=100,y=340)
        
        if initiate == 1:
            resetvalues()
            originalTimer = timer
            initiate = 2
        
        Next = Button(screen,text = "NEXT", width = "30", height = "2", command = changepage, bg = "grey")
        Next.place(x = 900, y = 670)
        
        timer -= 1
        continuousTimer = timer
        screen.after(1000,Break, timer)
        
        if timer < originalTimer-12:
            changepage()
            return
          
    
def Breakquestions(timer):
    global fix2, initiate, continuousTimer
    if fix2:
        screen.geometry("1280x800")
        page = Frame(screen)
        
        if initiate == 2:
            
            screen.geometry("1280x800")
            page = Frame(screen)
            heading = Label(screen, text = "For each of the following statements, please indicate how true it is for you, using the following scale:", font=('Helvatical bold',20)).grid(row=0, column=0, columnspan=8,pady=10,padx=10, sticky=W)
            
            Label(screen, text ="Not at\nall true").grid(row=1, column=2, padx=3)
            Label(screen, text =" ").grid(row=1, column=3, padx=3)
            Label(screen, text =" ").grid(row=1, column=4, padx=3)
            Label(screen, text ="Somewhat true").grid(row=1, column=5, padx=3)
            Label(screen, text =" ").grid(row=1, column=6, padx=3)
            Label(screen, text =" ").grid(row=1, column=7, padx=3)
            Label(screen, text ="Very true").grid(row=1, column=8, padx=3)
            
            spacing = 5
            Label(screen, text = "I felt very tense while doing this activity.", justify=LEFT).grid(row=2, column=0, columnspan=2, padx=10,pady=spacing, sticky=W)
            Label(screen, text = "I think I did pretty well at keeping my stress low, compared to other participants.", justify=LEFT).grid(row=3, column=0, columnspan=2, padx=10,pady=spacing, sticky=W)
            Label(screen, text = "I put a lot of effort into lowering my stress.", justify=LEFT).grid(row=4, column=0, columnspan=2, padx=10,pady=spacing, sticky=W)
            Label(screen, text = "I am satisfied with my performance in staying relaxed.", justify=LEFT).grid(row=5, column=0, columnspan=2, padx=10,pady=spacing, sticky=W)
            Label(screen, text = "I was anxious while working on this task.", justify=LEFT).grid(row=6, column=0, columnspan=2, padx=10,pady=spacing, sticky=W)
            Label(screen, text = "I didn't try very hard to keep my stress levels low at this activity.", justify=LEFT).grid(row=7, column=0, columnspan=2, padx=10,pady=spacing, sticky=W)
            Label(screen, text = "This was an activity that I couldn't do very well.", justify=LEFT).grid(row=8, column=0, columnspan=2, padx=10,pady=spacing, sticky=W)
            Label(screen, text = "I was very relaxed in doing this.", justify=LEFT).grid(row=9, column=0, columnspan=2, padx=10,pady=spacing, sticky=W)
            
            Label(screen, text = "It was important to me to do well at lowering my stress.", justify=LEFT).grid(row=10, column=0, columnspan=2, padx=10,pady=spacing, sticky=W)
            Label(screen, text = "I think I am pretty good at regulating my stress.", justify=LEFT).grid(row=11, column=0, columnspan=2, padx=10,pady=spacing, sticky=W)
            Label(screen, text = "I didn't put much energy into staying relaxed.", justify=LEFT).grid(row=12, column=0, columnspan=2, padx=10,pady=spacing, sticky=W)
            Label(screen, text = "I felt pressured while doing this.", justify=LEFT).grid(row=13, column=0, columnspan=2, padx=10,pady=spacing, sticky=W)
            Label(screen, text = "After working on lowering my stress for awhile, I felt pretty competent.", justify=LEFT).grid(row=14, column=0, columnspan=2, padx=10,pady=spacing, sticky=W)
            Label(screen, text = "I tried very hard to stay relaxed.", justify=LEFT).grid(row=15, column=0, columnspan=2, padx=10,pady=spacing, sticky=W)
            Label(screen, text = "I did not feel nervous at all while doing this. ", justify=LEFT).grid(row=16, column=0, columnspan=2, padx=10,pady=spacing, sticky=W)
            Label(screen, text = "I was pretty skilled at keeping my stress levels low.", justify=LEFT).grid(row=17, column=0, columnspan=2, padx=10,pady=spacing, sticky=W)
            
            Label(screen, text = "Press NEXT when done.", justify=LEFT, font=('Helvatical bold',16,"italic")).grid(row=18, column=0, columnspan=2, padx=10,pady=spacing, sticky=W)
            
        
            for x in range(1,8):
                Radiobutton(screen, variable=BQ1, value=x).grid(row=2, column=(x+1),padx=25)
                Radiobutton(screen, variable=BQ2, value=x).grid(row=3, column=(x+1),padx=25)
                Radiobutton(screen, variable=BQ3, value=x).grid(row=4, column=(x+1),padx=25)
                Radiobutton(screen, variable=BQ4, value=x).grid(row=5, column=(x+1),padx=25)
                Radiobutton(screen, variable=BQ5, value=x).grid(row=6, column=(x+1),padx=25)
                Radiobutton(screen, variable=BQ6, value=x).grid(row=7, column=(x+1),padx=25)
                Radiobutton(screen, variable=BQ7, value=x).grid(row=8, column=(x+1),padx=25)
                Radiobutton(screen, variable=BQ8, value=x).grid(row=9, column=(x+1),padx=25)
                Radiobutton(screen, variable=BQ9, value=x).grid(row=10, column=(x+1),padx=25)
                Radiobutton(screen, variable=BQ10, value=x).grid(row=11, column=(x+1),padx=25)
                Radiobutton(screen, variable=BQ11, value=x).grid(row=12, column=(x+1),padx=25)
                Radiobutton(screen, variable=BQ12, value=x).grid(row=13, column=(x+1),padx=25)
                Radiobutton(screen, variable=BQ13, value=x).grid(row=14, column=(x+1),padx=25)
                Radiobutton(screen, variable=BQ14, value=x).grid(row=15, column=(x+1),padx=25)
                Radiobutton(screen, variable=BQ15, value=x).grid(row=16, column=(x+1),padx=25)
                Radiobutton(screen, variable=BQ16, value=x).grid(row=17, column=(x+1),padx=25)
            
            initiate = 3
        
            
        Next = Button(screen,text = "NEXT", width = "30", height = "2", command = changepage, bg = "grey")
        Next.place(x = 900, y = 670)
        
        
        #Label(text=f'Time left of break: {timer} sec     ').grid(row=20, column=(0),padx=10)
        Label(text=f'Time left of break: {timer} sec     ').place(x=10,y=700)
        
        timer -= 1 
        continuousTimer = timer
        #print(continuousTimer)
        if timer != -1:
            screen.after(1000,Breakquestions,timer)
        else:
            initiate = 1
            changepage()
            return
        
    else:
        return

def Breakquestionspage2(timer):
    screen.geometry("1280x800")
    global initiate

    if initiate == 3:

        initiate = 0   
        spacing = 5
        
        
        heading2 = Label(screen, text = "Please indicate your experience, using the following scale:", font=('Helvatical bold',20)).grid(row=0, column=0, columnspan=8,pady=10,padx=10, sticky=W)
        
        
        Label(screen, text ="1").grid(row=1, column=2, padx=3)
        Label(screen, text ="2").grid(row=1, column=3, padx=3)
        Label(screen, text ="3").grid(row=1, column=4, padx=3)
        Label(screen, text ="4").grid(row=1, column=5, padx=3)
        Label(screen, text ="5").grid(row=1, column=6, padx=3)
        Label(screen, text ="6").grid(row=1, column=7, padx=3)
        Label(screen, text ="7").grid(row=1, column=8, padx=3)
        
        
        Label(screen, text = "How much information have you gained about your\nstress levels? Have you received and understood a\ngreat deal of knowledge (high) or very little (low)", justify=LEFT).grid(row=2, column=0, columnspan=2, padx=10,pady=spacing, sticky=W)
        Label(screen, text = "How good is the information you have gained about\nyour stress levels? Is the knowledge communicated\nvery useful (high) or is it insufficient (low)", justify=LEFT).grid(row=3, column=0, columnspan=2, padx=10,pady=spacing, sticky=W)        
        
        for x in range(1,8):
            Radiobutton(screen, variable=SART1, value=x).grid(row=2, column=(x+1),padx=5)
            Radiobutton(screen, variable=SART2, value=x).grid(row=3, column=(x+1),padx=5) 
        
        
        space = Label(screen, text = " ").grid(row=4, column=0,pady=10)
        Label(screen, text = "Drag and drop the sliders to describe how much you felt the following", font=('Helvatical bold',20)).grid(row=5, column=0, columnspan=8,pady=10,padx=10, sticky=W)
    
        
        Label(screen, text = "Mental demand", font=('Helvatical bold',18), justify=LEFT).grid(row=6, column=0, padx=10,pady=spacing, sticky=W)
        Label(screen, text = "LOW", justify=RIGHT).grid(row=6, column=1, padx=10,pady=spacing, sticky=E)
        Label(screen, text = "HIGH", justify=LEFT).grid(row=6, column=9, padx=10,pady=spacing, sticky=W)
        Label(screen, text = "How much mental and perceptual activity was required\n(eg., thinking, deciding, calculating, remembering)?\nWas the task easy or demanding, simple or complex?", font=('Helvatica',14, "italic"), justify=LEFT).grid(row=6, column=10, padx=5,pady=spacing, sticky=W)

        Label(screen, text = "Temporal demand", font=('Helvatical bold',18), justify=LEFT).grid(row=7, column=0, padx=10,pady=spacing, sticky=W)
        Label(screen, text = "LOW", justify=RIGHT).grid(row=7, column=1, padx=10,pady=spacing, sticky=E)
        Label(screen, text = "HIGH", justify=LEFT).grid(row=7, column=9, padx=10,pady=spacing, sticky=W)
        Label(screen, text = "How much time pressure did you feel due to the rate\nor pace at which the tasks or task elements occurred?\nWas the pace slow and leisurely or rapid and frantic?", font=('Helvatica',14, "italic"), justify=LEFT).grid(row=7, column=10, padx=5,pady=spacing, sticky=W)

        Label(screen, text = "Effort", font=('Helvatical bold',18), justify=LEFT).grid(row=8, column=0, padx=10,pady=spacing, sticky=W)
        Label(screen, text = "LOW", justify=RIGHT).grid(row=8, column=1, padx=10,pady=spacing, sticky=E)
        Label(screen, text = "HIGH", justify=LEFT).grid(row=8, column=9, padx=10,pady=spacing, sticky=W)
        Label(screen, text = "How hard did you have to work to accomplish your\nlevel of performance?", font=('Helvatica',14, "italic"), justify=LEFT).grid(row=8, column=10, padx=5,pady=spacing, sticky=W)

        Label(screen, text = "Performance", font=('Helvatical italic',18), justify=LEFT).grid(row=9, column=0, padx=10,pady=spacing, sticky=W)
        Label(screen, text = "GOOD", justify=RIGHT).grid(row=9, column=1, padx=10,pady=spacing, sticky=E)
        Label(screen, text = "POOR", justify=LEFT).grid(row=9, column=9, padx=10,pady=spacing, sticky=W)
        Label(screen, text = "How successful do you think you were in accomplishing\nthe goals of the task? How satisfied were you with\nyour performance in accomplishing these goals?", font=('Helvatica',14, "italic"), justify=LEFT).grid(row=9, column=10, padx=5,pady=spacing, sticky=W)

        Label(screen, text = "Frustration", font=('Helvatical bold',18), justify=LEFT).grid(row=10, column=0, padx=10,pady=spacing, sticky=W)
        Label(screen, text = "LOW", justify=RIGHT).grid(row=10, column=1, padx=10,pady=spacing, sticky=E)
        Label(screen, text = "HIGH", justify=LEFT).grid(row=10, column=9, padx=10,pady=spacing, sticky=W)
        Label(screen, text = "How insecure, discouraged, irritated, stressed, and\nannoyed versus secure, gratified, content,\nand relaxed did you feel during the task?", font=('Helvatica',14, "italic"), justify=LEFT).grid(row=10, column=10, padx=5,pady=spacing, sticky=W)

        #  slider
        NASA1 = Scale(screen, from_=0, to=100, length=300, orient=HORIZONTAL, variable=TLXMDemand).grid(row=6,column=2,columnspan=7,pady=spacing)
        NASA2 = Scale(screen, from_=0, to=100, length=300, orient=HORIZONTAL).grid(row=7,column=2,columnspan=7,pady=spacing)
        NASA3 = Scale(screen, from_=0, to=100, length=300, orient=HORIZONTAL).grid(row=8,column=2,columnspan=7,pady=spacing)
        NASA4 = Scale(screen, from_=0, to=100, length=300, orient=HORIZONTAL).grid(row=9,column=2,columnspan=7,pady=spacing)
        NASA5 = Scale(screen, from_=0, to=100, length=300, orient=HORIZONTAL).grid(row=10,column=2,columnspan=7,pady=spacing)
        
        Label(screen, text = " ").grid(row=11, column=0,pady=2)
        heading3 = Label(screen, text = "When finished, please relax until the timer runs out", font=('Helvatical bold',20)).grid(row=12, column=0, columnspan=8,pady=10,padx=10, sticky=W)
      
   
    
    Label(text=f'Time left of break: {timer} sec     ').place(x=10,y=700)

    timer -= 1 
    #print(continuousTimer)
    if timer != -1:
        screen.after(1000,Breakquestionspage2,timer)
        
    else:
        fix = True
        changepage()
        


def Stress1(timer):
    screen.geometry("700x800+0+0")
    #page = Frame(screen)
    Label(screen, text=f'Next slide in: {timer} sec     ').place(x=15,y=700)
    global stresscounter, stresstime, rightoption, initiate, stressscore, stressproblemcount
    option=opt.get()   
    
    if initiate == 1:
        rightoption = mathproblem()
        stressscore, stressproblemcount = 0, 0
        initiate = 0
        
        top = Toplevel()
        top.geometry("580x400+700+0")
        Label(top,text="Please don't move this window (it will close automatically)",font=("Helvetica",20,"italic"),justify=LEFT,fg="snow3").place(x=30,y=20)
    
    if option == rightoption:
        stressscore += 1
        stressproblemcount += 1

        stresscounter = stresstime
        opt.set(0)
        rightoption = mathproblem()
        
    elif option != rightoption and option > 0:
        stressproblemcount += 1
        print("wrong")
        stresscounter = stresstime
        opt.set(0)
        rightoption = mathproblem()
        
    else:
        stresscounter -= 1
        opt.set(0)
        
    if stresscounter == 0:
        stressproblemcount += 1
        stresscounter = stresstime
        rightoption = mathproblem()
        
    timer -= 1 
    if timer != -1:
        screen.after(1000, Stress1,timer)
    else:
        changepage()
        print("what up?")
    
def Stress3(timer):
    screen.geometry("1280x800")
    page = Frame(screen)
    Label(text=f'Next slide in: {timer} sec     ').place(x=15,y=700)
    global stresscounter, stresstime, rightoption, initiate, stressscore, stressproblemcount, breaktime, breaklength, originalTimer
    option=opt.get()   
    
    if breaktime == False:
        screen.geometry("1280x800")
        page = Frame(screen)
        
        if initiate == 1:
            rightoption = mathproblem()
            stressscore, stressproblemcount = 0, 0
            breaklength = timer/4
            originalTimer = timer
            print(breaklength)
            initiate = 0
        
        if option == rightoption:
            stressscore += 1
            stressproblemcount += 1
    
            stresscounter = stresstime
            opt.set(0)
            rightoption = mathproblem()
            
        elif option != rightoption and option > 0:
            stressproblemcount += 1
            print("wrong")
            stresscounter = stresstime
            opt.set(0)
            rightoption = mathproblem()
            
        else:
            stresscounter -= 1
            opt.set(0)
            
        if stresscounter == 0:
            stressproblemcount += 1
            stresscounter = stresstime
            rightoption = mathproblem()
    
    else: 
        screen.geometry("700x800")
        page = Frame(screen)
        Label(text="Mid-break",font=("Helvetica",60),justify=LEFT).place(x=100,y=260)
        lbl1 = Label(screen,text="Relax and match your breathing with the guide to the\nright. The exercises will resume afterwards. \n                                      \n                                      \n                                      \n                                      \n                                      \n                                      \n",font=("Helvetica",20),justify=LEFT)
        lbl1.place(x=100,y=340)
    
    if timer == (originalTimer/2)+(breaklength/2):
        breaktime = True
        print("breaktime")
    elif timer == (originalTimer/2)-(breaklength/2):
        breaktime = False
        Label(text="                    ",font=("Helvetica",60),justify=LEFT).place(x=100,y=260)
        lbl1 = Label(screen,text="                                                                                                     \n                                                                                         ",font=("Helvetica",20),justify=LEFT)
        lbl1.place(x=100,y=340)
        print("we back!")
    
    timer -= 1 
    if timer != -1:
        screen.after(1000, Stress3,timer)
    else:
        changepage()  
"""        
def Stress3Break(timer):
    screen.geometry("700x800")
    page = Frame(screen)
    Label(text="Mid-break",font=("Helvetica",60),justify=LEFT).place(x=100,y=260)
    Label(text="Relax and match your breathing with the guide to the\nright. The exercises will resume afterwards.",font=("Helvetica",20),justify=LEFT).place(x=100,y=340)
   
    timer -= 1
    if timer != -1:
        screen.after(1000, Stress3Break, timer)
    else:
        global breaktime
        breaktime = False
        Stress3(90)         
"""

def Relax1(timer):
    global initiate, originalTimer, BFtime, breaktime#,topper
    if initiate == 1:
        BFtime = 15
        originalTimer = timer
        initiate = 0
        #topper = Toplevel()
        #topper.geometry("580x400+700+0")
    
    if timer > originalTimer-BFtime or (timer <= originalTimer/2 and timer > (originalTimer/2)-BFtime):
        breaktime = True
        #if timer == originalTimer/2:
            #topper = Toplevel()
            #topper.geometry("580x400+700+0")
    else:
        breaktime = False
        #topper.destroy()
        
        
        
   
    
    if breaktime:
        screen.geometry("700x800")
        page = Frame(screen)
        Label(text="Relaxation",font=("Helvetica",60),justify=LEFT).place(x=100,y=260)
        Label(text="Have a look at your stress levels,        \nand try to relax the best you can.",font=("Helvetica",20),justify=LEFT).place(x=100,y=340)
        
        
        #Label(topper,text="Please don't move this window (it will close automatically)",font=("Helvetica",20,"italic"),justify=LEFT,fg="snow3").place(x=30,y=20)

    else:
        screen.geometry("1280x800")
        page = Frame(screen)
        Label(text="Relaxation",font=("Helvetica",60),justify=LEFT).place(x=100,y=260)
        Label(text="Without looking at your stress levels,\ntry to relax the best you can.      ",font=("Helvetica",20),justify=LEFT).place(x=100,y=340)
        
        
    timer -= 1
    Label(text=f'Next slide in: {timer} sec    ').place(x=15,y=700)
    if timer != -1:
        screen.after(1000, Relax1, timer)
    else:
        changepage()
        return

def Relax2(timer):
    screen.geometry("700x800")
    page = Frame(screen)
    Label(text="Relaxation",font=("Helvetica",60),justify=LEFT).place(x=100,y=260)
    Label(text="Try to relax, and match your breathing\nwith the guide to the right.",font=("Helvetica",20),justify=LEFT).place(x=100,y=340)
    
        
    timer -= 1
    Label(text=f'Next slide in: {timer} sec    ').place(x=15,y=700)
    if timer != -1:
        screen.after(1000, Relax2, timer)
    else:
        changepage()
        return    


def resetvalues():
    BQ1.set(0)
    BQ2.set(0)
    BQ3.set(0)
    BQ4.set(0)
    BQ5.set(0)
    BQ6.set(0)
    BQ7.set(0)
    BQ8.set(0)
    BQ9.set(0)
    BQ10.set(0)
    BQ11.set(0)
    BQ12.set(0)
    BQ13.set(0)
    BQ14.set(0)
    BQ15.set(0)
    BQ16.set(0)
    
    SART1.set(0)
    SART2.set(0)
    
    TLXMDemand.set(0)
    TLXTDemand.set(0)
    TLXPerformance.set(0)
    TLXEffort.set(0)
    TLXFrustration.set(0)
    
screen = Tk()
screen.geometry("1280x800")
screen.title("Biofeedback experiment")
  
default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size=15)

#BFscreen = Tk()
#BFscreen.geometry("640x800")
#BFscreen.title("Biofeedback experiment")

no = StringVar()
BFexperience = IntVar()
gender = IntVar()
worktype = IntVar()
age = IntVar()
Q1 = IntVar(None,2)
Q2 = IntVar(None,2)
Q3 = IntVar(None,2)
Q4 = IntVar(None,2)
opt = IntVar(None,0)

BQ1 = IntVar(None,0)
BQ2 = IntVar(None,0)
BQ3 = IntVar(None,0)
BQ4 = IntVar(None,0)
BQ5 = IntVar(None,0)
BQ6 = IntVar(None,0)
BQ7 = IntVar(None,0)
BQ8 = IntVar(None,0)
BQ9 = IntVar(None,0)
BQ10 = IntVar(None,0)
BQ11 = IntVar(None,0)
BQ12 = IntVar(None,0)
BQ13 = IntVar(None,0)
BQ14 = IntVar(None,0)
BQ15 = IntVar(None,0)
BQ16 = IntVar(None,0)

SART1 = IntVar(None,0)
SART2 = IntVar(None,0)

TLXMDemand = DoubleVar(0)
TLXTDemand = DoubleVar(0)
TLXPerformance = DoubleVar(0)
TLXEffort = DoubleVar(0)
TLXFrustration = DoubleVar(0)

AdjustableLabel = StringVar()

pagenum = 0
#changepage()
Stress3(40)
screen.mainloop()

