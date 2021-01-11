from pygame import mixer
import time
from tkinter import *
from tkinter import messagebox
import random
from tkinter.ttk import *
from time import strftime
import calendar
import datetime
import sys
a=0
b=0
x=0
y=0
f=""
s="";
gr=0
test=('0','1','2','3','4','5','6','7','8','9')
from tkinter import *
import time
def cal():
    if sys.version[0] == '2':
        import Tkinter as tk
    else:
        import tkinter as tk
 
    class Calendar:
        def __init__(self, parent, values):
            self.values = values
            self.parent = parent
            self.cal = calendar.TextCalendar(calendar.SUNDAY)
            self.year = datetime.date.today().year
            self.month = datetime.date.today().month
            self.wid = []
            self.day_selected = 1
            self.month_selected = self.month
            self.year_selected = self.year
            self.day_name = ''
         
            self.setup(self.year, self.month)
         
        def clear(self):
            for w in self.wid[:]:
                w.grid_forget()
                #w.destroy()
                self.wid.remove(w)
     
        def go_prev(self):
            if self.month > 1:
                self.month -= 1
            else:
                self.month = 12
                self.year -= 1
            #self.selected = (self.month, self.year)
            self.clear()
            self.setup(self.year, self.month)
 
        def go_next(self):
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1
         
            #self.selected = (self.month, self.year)
            self.clear()
            self.setup(self.year, self.month)
         
        def selection(self, day, name):
            self.day_selected = day
            self.month_selected = self.month
            self.year_selected = self.year
            self.day_name = name
         
            #data
            self.values['day_selected'] = day
            self.values['month_selected'] = self.month
            self.values['year_selected'] = self.year
            self.values['day_name'] = name
            self.values['month_name'] = calendar.month_name[self.month_selected]
         
            self.clear()
            self.setup(self.year, self.month)
         
        def setup(self, y, m):
            left = tk.Button(self.parent, text='<', command=self.go_prev)
            self.wid.append(left)
            left.grid(row=0, column=1)
         
            header = tk.Label(self.parent, height=2, text='{}   {}'.format(calendar.month_abbr[m], str(y)))
            self.wid.append(header)
            header.grid(row=0, column=2, columnspan=3)
         
            right = tk.Button(self.parent, text='>', command=self.go_next)
            self.wid.append(right)
            right.grid(row=0, column=5)
         
            days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
            for num, name in enumerate(days):
                t = tk.Label(self.parent, text=name[:3])
                self.wid.append(t)
                t.grid(row=1, column=num)
         
            for w, week in enumerate(self.cal.monthdayscalendar(y, m), 2):
                for d, day in enumerate(week):
                    if day:
                        #print(calendar.day_name[day])
                        b = tk.Button(self.parent, width=1, text=day, command=lambda day=day:self.selection(day, calendar.day_name[(day-1) % 7]))
                        self.wid.append(b)
                        b.grid(row=w, column=d)
                     
            sel = tk.Label(self.parent, height=2, text='{} {} {} {}'.format(
                self.day_name, calendar.month_name[self.month_selected], self.day_selected, self.year_selected))
            self.wid.append(sel)
            sel.grid(row=8, column=0, columnspan=7)
         
            ok = tk.Button(self.parent, width=5, text='OK', command=self.kill_and_save)
            self.wid.append(ok)
            ok.grid(row=9, column=2, columnspan=3, pady=10)
         
        def kill_and_save(self):
            self.parent.destroy()
     
 
    if __name__ == '__main__':
 
        class Control:
            def __init__(self, parent):
                self.parent = parent
                self.choose_btn = tk.Button(self.parent, text='Choose',command=self.popup)
                self.show_btn = tk.Button(self.parent, text='Show Selected',command=self.print_selected_date)
                self.choose_btn.grid()
                self.show_btn.grid()
                self.data = {}
             
            def popup(self):
                child = tk.Toplevel()
                cal = Calendar(child, self.data)
             
            def print_selected_date(self):
                print(self.data)
             
 
        root = tk.Tk()
        app = Control(root)
        root.mainloop()
def remainder():
        def invoke2(i1,i2,i3,i4):
            a=int(i1)
            b=int(i2)
            print(a,b)
            if (((i3=="pm")or(i3=="PM")) and a<12 ):
                a=a+12;
        
   
        
            elif(a==12 and ((i3=="am")or(i3=="AM"))):
                    a=0;
            
      
            while 1==1:
                time.localtime()
                x=time.localtime().tm_hour
                y=time.localtime().tm_min
                if a==x and b==y :
                    print(i4)
                    sound()
                    def off():
                            mixer.music.stop()
                            my_windowm.destroy()
                    
            

                    my_windowm= Tk()
                    my_windowm.config(bg="yellow")
                    label= Label(my_windowm,text=i4 )
                    alarmoff = Button(my_windowm,text='Remainder off',command= off)
 
                    label.grid(row=0,column=0)


                    alarmoff.grid(row=1,column=0)
                    my_windowm.mainloop()
                    break
            
            




        def show():
   
            f=entry_1.get()
            s=entry_2.get()
            t=entry_3.get()
            r=entry_4.get()
            j=" remainder created at " + f+":"+ s + t
            messagebox.showinfo("remainder", j)
   
            invoke2(f,s,t,r)

     


        my_windowg= Tk()
        my_windowg.config(bg="yellow")
        label= Label(my_windowg,text='enter hours')
        label2= Label(my_windowg,text='enter minutes')
        label3= Label(my_windowg,text='enter AM/PM')
        label4= Label(my_windowg,text='enter reminder')
        entry_1=Entry(my_windowg)
        entry_2=Entry(my_windowg)
        entry_3=Entry(my_windowg)
        entry_4=Entry(my_windowg)
        button_1 = Button(my_windowg,text ='set remainder',command = show)

        label.grid(row=0,column=0)
        entry_1.grid(row=0,column=1)
        label2.grid(row=1,column=0)
        entry_2.grid(row=1,column=1)
        label3.grid(row=2,column=0)
        entry_3.grid(row=2,column=1)
        label4.grid(row=3,column=0)
        entry_4.grid(row=3,column=1)
        button_1.grid(row=4,column=0)





        my_windowg.mainloop()
def mathalarm():
        def invoke1(i1,i2,i3):
            a=int(i1)
            b=int(i2)
            print(a,b)
            if (((i3=="pm")or(i3=="PM")) and a<12 ):
                a=a+12;
        
   
        
            elif(a==12 and ((i3=="am")or(i3=="AM"))):
                    a=0;
            
      
            while 1==1:
                time.localtime()
                x=time.localtime().tm_hour
                y=time.localtime().tm_min
                if a==x and b==y :
                    print("alarm")
                    sound()
                    def off():
                        g=entry_1.get()
                        ch=int(g)
                        if s3 == ch:
                            mixer.music.stop()
                            my_windowx.destroy()
                    
            
                    t1=random.choice(test)+random.choice(test)+random.choice(test)
                    t2=random.choice(test)+random.choice(test)+random.choice(test)
                    z="solve "+ t1 +"+"+ t2 ;
                    s1=int(t1)
                    s2=int(t2)
                    s3=s1+s2;
                    my_windowx= Tk()
                    my_windowx.config(bg="yellow")
                    label= Label(my_windowx,text=z )
                    label2= Label(my_windowx,text='answer')
                    alarmoff = Button(my_windowx,text='alarm off',command= off)
                    entry_1=Entry(my_windowx)
                    label.grid(row=0,column=0)
                    label2.grid(row=1,column=0)
                    entry_1.grid(row=1,column=1)
                    alarmoff.grid(row=1,column=0)
                    my_windowx.mainloop()
                    break
            
            




        def show():
   
            f=entry_1.get()
            s=entry_2.get()
            t=entry_3.get()
            j=" alarm created at " + f+":"+ s + t
            messagebox.showinfo("alarm", j)
   
            invoke1(f,s,t)

     


        my_windowy= Tk()
        my_windowy.config(bg="yellow")
        label= Label(my_windowy,text='enter hours')
        label2= Label(my_windowy,text='enter minutes')
        label3= Label(my_windowy,text='enter AM/PM')
        entry_1=Entry(my_windowy)
        entry_2=Entry(my_windowy)
        entry_3=Entry(my_windowy)
        button_1 = Button(my_windowy,text ='set math alarm',command = show)

        label.grid(row=0,column=0)
        entry_1.grid(row=0,column=1)
        label2.grid(row=1,column=0)
        entry_2.grid(row=1,column=1)
        label3.grid(row=2,column=0)
        entry_3.grid(row=2,column=1)
        button_1.grid(row=3,column=0)





        my_windowy.mainloop()
def timer1():
        def inf():
                def kill():
                        mixer.music.stop()
                        root.destroy()
                root = Tk()
                root.title('Clock')
                lbl = Label(root, text='TIMER',
                            background = 'purple',
                            foreground = 'white')
                bx=Button(root,text='close',command=kill)
            
            
                lbl.grid(row=0,column=0)
                bx.grid(row=0,column=1)
                root.mainloop()
    

        def timer(f,s,t):
            x1=int(f)
            y1=int(s)
            z1=int(t)

            a=time.localtime().tm_hour+x1
            b=time.localtime().tm_min+y1
            c=time.localtime().tm_sec+z1
            while 1==1:
                time.localtime()
                x=time.localtime().tm_hour
                y=time.localtime().tm_min
                z=time.localtime().tm_sec
                if a==x and b==y and c==z:
                    print("timer")
                    sound()
                    inf()
                    break;
            
        def show1():
   
            f=entry_1.get()
            s=entry_2.get()
            t=entry_3.get()
            j=" timer created at " + f+":"+ s + t
            messagebox.showinfo("timer", j)
   
            timer(f,s,t)
    
        my_window3= Tk()
        my_window3.config(bg="yellow")
        label= Label(my_window3,text='enter hours')
        label2= Label(my_window3,text='enter minutes')
        label3= Label(my_window3,text='enter seconds')
        entry_1=Entry(my_window3)
        entry_2=Entry(my_window3)
        entry_3=Entry(my_window3)
        button_1 = Button(my_window3,text ='set timer',command = show1)

        #button_3 = Button(my_window3,text ='close',command = turnoff)

        label.grid(row=0,column=0)
        entry_1.grid(row=0,column=1)
        label2.grid(row=1,column=0)
        entry_2.grid(row=1,column=1)
        label3.grid(row=2,column=0)
        entry_3.grid(row=2,column=1)
        button_1.grid(row=3,column=0)
        #button_2.grid(row=3,column=2)
        #button_3.grid(row=3,column=4)

        my_window3.mainloop()
def changer():
        c=('red','blue','green','yellow','purple','pale green','light cyan')
        my_window.configure(background=random.choice(c))
def snooze(a,b):
        if (time.localtime().tm_min >= 55) and (time.localtime().tm_hour==23):
                l=time.localtime().tm_min +5
                if( l>59):
                        j=60-l
                        a=0
                        b=j
                        print(a)
                        print(b)
                elif(l==60):
                        a=0
                        b=0
                        print(a)
                        print(b)
        if (time.localtime().tm_min >= 55) and (time.localtime().tm_hour==12):
                l=time.localtime().tm_min +5
                if( l>59):
                        j=60-l
                        a=13
                        b=j
                        print(a)
                        print(b)
                elif(l==60):
                        a=13
                        b=0
                        print(a)
                        print(b)
        elif (time.localtime().tm_min >= 55):
                l=time.localtime().tm_min +5
                if( l>59):
                        j=60-l
                        a=time.localtime().tm_hour +1
                        b=j
                        print(a)
                        print(b)
                elif(l==60):
                        a=time.localtime().tm_hour +1
                        b=0
                        print(a)
                        print(b)
                       
                        
        elif(time.localtime().tm_min <= 55):
                a=time.localtime().tm_hour
                b=time.localtime().tm_min +1
                print(a)
                print(b)
                
        while 1==1 :
                time.localtime()
                x=time.localtime().tm_hour
                y=time.localtime().tm_min
                if a==x and b==y :
                        print("alarm")
                        sound()
                        answer = messagebox.askquestion(" ALARM!!!!!! DO YOU WANT SNOOZE ?")
                        if answer== "yes":
                                snooze(a,b)
                        if answer== "no":
                                mixer.music.stop()
                                break;

                    
            
def sound():
        mixer.init()
        mixer.music.load('songname.mp3')
        mixer.music.play()
def turnoff():
        my_window.destroy()
def invoke(i1,i2,i3,i4,i5,i6):
    
    file = open("py.txt", 'r')
    for each in file:
            gr=int(each);
            gr=gr+1
    file.close()
    print(gr)
    file = open("py.txt", 'w')
    for i in range(1):
            gr=str(gr)
            file.write(gr)
    file.close()
    
        
    a=int(i1)
    b=int(i2)
    c=int(i4)
    d=int(i5)
    e=int(i6)
    print(a,b)
    if (((i3=="pm")or(i3=="PM")) and a<12 ):
        a=a+12;
        
   
        
    elif(a==12 and ((i3=="am")or(i3=="AM"))):
            a=0;
            
      
    while 1==1:
        time.localtime()
        x=time.localtime().tm_hour
        y=time.localtime().tm_min
        x1=time.localtime().tm_mday
        y1=time.localtime().tm_mon
        z1=time.localtime().tm_year
        if a==x and b==y and c==x1 and d==y1 and e==z1:
            print("alarm")
            sound()
            answer = messagebox.askquestion(" ALARM!!!!!! DO YOU WANT SNOOZE ?")
            if answer== "yes":
                    mixer.music.stop()
                    snooze(a,b)
                    break;
                    
                    
            if answer== "no":
                    mixer.music.stop()
                    break;
        
            
            




def show():
   
    f=entry_1.get()
    s=entry_2.get()
    t=entry_3.get()
    t1=entry_44.get()
    t2=entry_55.get()
    t3=entry_66.get()
    j=" alarm created at " + f+":"+ s + t
    messagebox.showinfo("alarm", j)
   
    invoke(f,s,t,t1,t2,t3)

def real():
    root = Tk() 
    root.title('Clock') 
  

    def time(): 
        string = strftime('%H:%M:%S %p') 
        lbl.config(text = string) 
        lbl.after(1000, time) 
  

    lbl = Label(root, font = ('calibri', 40, 'bold'), 
            background = 'purple', 
            foreground = 'white') 
  

    lbl.pack(anchor = 'center') 
    time() 
  
    mainloop()      


my_window= Tk()
my_window.config(bg="sky blue")
label= Label(my_window,text='enter hours')
label2= Label(my_window,text='enter minutes')
label3= Label(my_window,text='enter AM/PM')
label44= Label(my_window,text='date')
label55= Label(my_window,text='month')
label66= Label(my_window,text='year')
entry_1=Entry(my_window)
entry_2=Entry(my_window)
entry_3=Entry(my_window)
entry_44=Entry(my_window)
entry_55=Entry(my_window)
entry_66=Entry(my_window)
button_1 = Button(my_window,text ='set alarm',command = show)
button_2 = Button(my_window,text ='show time',command = real)
button_3 = Button(my_window,text ='close',command = turnoff)
button_4 = Button(my_window,text ='colour changer',command=changer)
button_5 = Button(my_window,text ='timer',command=timer1)
button_6 = Button(my_window,text ='math alarm',command=mathalarm)
button_7 = Button(my_window,text ='remainder',command=remainder)
button_8 = Button(my_window,text ='calender',command=cal)
label.grid(row=0,column=0)
entry_1.grid(row=0,column=1)
label2.grid(row=1,column=0)
entry_2.grid(row=1,column=1)
label3.grid(row=2,column=0)
entry_3.grid(row=2,column=1)
label44.grid(row=0,column=3)
entry_44.grid(row=0,column=4)
label55.grid(row=1,column=3)
entry_55.grid(row=1,column=4)
label66.grid(row=2,column=3)
entry_66.grid(row=2,column=4)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=2)
button_3.grid(row=3,column=4)
button_4.grid(row=4,column=4)
button_5.grid(row=4,column=2)
button_6.grid(row=5,column=0)
button_7.grid(row=5,column=2)
button_8.grid(row=5,column=4)





my_window.mainloop()

