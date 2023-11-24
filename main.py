from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivy.properties import ObjectProperty
import math
# from kivy.core.window import Window
# Window.size = (600, 450)

Builder.load_file('style.kv')

class Style(MDAnchorLayout):
    txt=ObjectProperty()
    num1=''
    amal=''

    def mom(self):
        if len(self.txt.text)==0:
            self.txt.text='0.'
        elif len(self.txt.text)!=0:
            t=0
            for q in self.txt.text:
                if q=='0':
                    t+=1
            if t==len(self.txt.text):
                self.txt.text='0.'
            else:
                t2=0
                for q in self.txt.text:
                    if q=='.':
                        t2+=1
                if t2==1:
                    pass
                else:
                    self.txt.text+='.'
        else:pass  

    def clear1(self):
        if self.txt.text=='':
            pass
        else:
            t=[]
            for q in self.txt.text:
                t.append(q)
            t.pop()
            tt=''
            for q in t:
                tt+=q 
            self.txt.text=tt 

    def jam(self):
        self.amal='+'
        self.num1=self.txt.text 
        self.txt.text=''
    def kam(self):
        self.amal='-'
        self.num1=self.txt.text 
        self.txt.text=''
    def zar(self):
        self.amal='*'
        self.num1=self.txt.text 
        self.txt.text=''
    def tagh(self):
        self.amal='/'
        self.num1=self.txt.text 
        self.txt.text=''
    def result(self):
        try:
            if self.amal=='*':
                num2=self.txt.text
                self.txt.text=str(float(self.num1)*float(num2))
            elif self.amal=='/':
                num2=self.txt.text
                self.txt.text=str(float(self.num1)/float(num2))
            elif self.amal=='+':
                num2=self.txt.text
                self.txt.text=str(float(self.num1)+float(num2))
            elif self.amal=='-':
                num2=self.txt.text
                self.txt.text=str(float(self.num1)-float(num2))
            else:pass
        except:pass 
    def radic(self):
        try:
            t=math.sqrt(float(self.txt.text))
            self.txt.text=str(t)
        except:pass 

    def cos(self):
        try:
            t=math.cos(float(self.txt.text))
            self.txt.text=str(t)
        except:pass 
    def sin(self):
        try:
            t=math.sin(float(self.txt.text))
            self.txt.text=str(t)
        except:pass 
    def tan(self):
        try:
            t=math.tan(float(self.txt.text))
            self.txt.text=str(t)
        except:pass 
    def cot(self):
        try:
            t=math.tan(float(self.txt.text))
            tt=1/t
            self.txt.text=str(tt)
        except:pass 
    def cosh(self):
        try:
            t=math.cosh(float(self.txt.text))
            self.txt.text=str(t)
        except:pass 
    def sinh(self):
        try:
            t=math.sinh(float(self.txt.text))
            self.txt.text=str(t)
        except:pass 
    def tanh(self):
        try:
            t=math.tanh(float(self.txt.text))
            self.txt.text=str(t)
        except:pass 
    def coth(self):
        try:
            t=math.tanh(float(self.txt.text))
            tt=1/t
            self.txt.text=str(tt)
        except:pass 

    def mosman(self):
        try:
            q=float(self.txt.text)
            q*=-1
            self.txt.text=str(q)
        except:pass 

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style='Dark'

        return Style()

MainApp().run()