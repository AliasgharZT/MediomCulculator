from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivy.properties import ObjectProperty
import math
from kivymd.toast import toast
# from kivy.app import App
import numpy
from scipy.integrate import quad
# from kivy.core.window import Window
# Window.size = (600, 450)

Builder.load_file('style.kv')

class Style(MDAnchorLayout):
    txt=ObjectProperty()
    mn=ObjectProperty()
    _fpl=ObjectProperty()
    _xy=ObjectProperty()
    _xyz=ObjectProperty()
    _integ=ObjectProperty()
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

    def fpl(self):
        self.mn.current='fpl'
    def integ(self):
        self.mn.current='integ'
    def xy(self):
        self.mn.current='xy'
    def xyz(self):
        self.mn.current='xyz'

    def fact(self):
        try:
            q=int(self._fpl.text)
            self._fpl.text=''
            w= math.factorial(q)
            self._fpl.text=str(w)
        except:
            toast('fact= int\n>>123')
    def power(self):
        try:
            q=self._fpl.text.split(',')
            w=math.pow(float(q[0]),float(q[1]))
            self._fpl.text=str(w)
        except:
            toast('pow= vlaue,power\n>>3,3')
    def loga(self):
        try:
            q=self._fpl.text.split(',')
            w=math.log(float(q[0]),float(q[1]))
            self._fpl.text=str(w)
        except:
            toast('log= vlaue,Base\n>>8,3') 

    def solve_xy(self):
        try:
            q=self._xy.text.split(',')
            ab1=[float(q[0]),float(q[1])]
            ab2=[float(q[2]),float(q[3])]
            c12=[float(q[4]),float(q[5])]
            a=numpy.array([ab1,ab2])
            b=numpy.array(c12)
            r=numpy.linalg.solve(a,b)
            x=str(r[0])
            y=str(r[1])
            self._xy.text='x='+x[0:4]+'II y='+y[0:4]
        except:
            toast('a1,b1,a1,b2,c1,c2\na!=b!=c')

    def solve_xyz(self):
        try:
            q=self._xyz.text.split(',')
            abz1=[float(q[0]),float(q[1]),float(q[2])]
            abz2=[float(q[3]),float(q[4]),float(q[5])]
            abz3=[float(q[6]),float(q[7]),float(q[8])]
            c123=[float(q[9]),float(q[10]),float(q[11])]
            a=numpy.array([abz1,abz2,abz3])
            b=numpy.array(c123)
            r=numpy.linalg.solve(a,b)
            x=str(r[0])
            y=str(r[1])
            z=str(r[2])
            self._xyz.text='x='+x[0:4]+'II y='+y[0:4]+'II z='+z[0:4]
        except:
            toast('a1,b1,z1,a2,b2,z2,a3,b3,z3,c1,c2,c3\na!=b!=z!=c')

    def infix_to_postfix(self,expression): 

        stack = [] # initialization of empty stack
        output = '' 
        Operators = set(['+', '-', '*', '/', '(', ')', '^'])  # collection of Operators
        Priority = {'+':1, '-':1, '*':2, '/':2, '^':3} # dictionary having priorities of Operators

        for character in expression:

            if character not in Operators:  # if an operand append in postfix expression

                output+= character

            elif character=='(':  # else Operators push onto stack

                stack.append('(')

            elif character==')':

                while stack and stack[-1]!= '(':

                    output+=stack.pop()

                stack.pop()

            else: 

                while stack and stack[-1]!='(' and Priority[character]<=Priority[stack[-1]]:

                    output+=stack.pop()

                stack.append(character)

        while stack:

            output+=stack.pop()

        return output
    def _integ_(self,x):
        q=self.infix_to_postfix(self.c0)
        r=[]
        for w in range(len(q)):
            if w+1!=len(q):
                if q[w]=='*':
                    if (q[w-2]>='0' and q[w-2]<='9')and(q[w-1]>='0' and q[w-1]<='9'):
                        z=int(q[w-2])*int(q[w-1])
                    elif  (q[w-2]>='0' and q[w-2]<='9')and(q[w-1]=='x'):
                        z=int(q[w-2])*x
                    elif (q[w-2]=='x')and(q[w-1]>='0' and q[w-1]<='9'):
                        z=x*int(q[w-1])
                    elif (q[w-2]=='x')and(q[w-1]=='x'):
                        z=x*x 
                    else:pass
                    r.append(z)
                elif q[w]=='/':
                    if (q[w-2]>='0' and q[w-2]<='9')and(q[w-1]>='0' and q[w-1]<='9'):
                        z=int(q[w-2])/int(q[w-1])
                    elif  (q[w-2]>='0' and q[w-2]<='9')and(q[w-1]=='x'):
                        z=int(q[w-2])/x
                    elif (q[w-2]=='x')and(q[w-1]>='0' and q[w-1]<='9'):
                        z=x/int(q[w-1])
                    elif (q[w-2]=='x')and(q[w-1]=='x'):
                        z=x/x 
                    else:pass
                    r.append(z)
                elif q[w]=='-':
                    if (q[w-2]>='0' and q[w-2]<='9')and(q[w-1]>='0' and q[w-1]<='9'):
                        z=int(q[w-2])-int(q[w-1])
                    elif  (q[w-2]>='0' and q[w-2]<='9')and(q[w-1]=='x'):
                        z=int(q[w-2])-x
                    elif (q[w-2]=='x')and(q[w-1]>='0' and q[w-1]<='9'):
                        z=x-int(q[w-1])
                    elif (q[w-2]=='x')and(q[w-1]=='x'):
                        z=x-x 
                    else:pass
                    r.append(z)
                elif q[w]=='+':
                    if (q[w-2]>='0' and q[w-2]<='9')and(q[w-1]>='0' and q[w-1]<='9'):
                        z=int(q[w-2])+int(q[w-1])
                    elif  (q[w-2]>='0' and q[w-2]<='9')and(q[w-1]=='x'):
                        z=int(q[w-2])+x
                    elif (q[w-2]=='x')and(q[w-1]>='0' and q[w-1]<='9'):
                        z=x+int(q[w-1])
                    elif (q[w-2]=='x')and(q[w-1]=='x'):
                        z=x+x 
                    else:pass
                    r.append(z)
                elif q[w]=='^':
                    if (q[w-2]>='0' and q[w-2]<='9')and(q[w-1]>='0' and q[w-1]<='9'):
                        z=pow(int(q[w-2]),int(q[w-1]))
                    elif  (q[w-2]>='0' and q[w-2]<='9')and(q[w-1]=='x'):
                        z=pow(int(q[w-2]),x)
                    elif (q[w-2]=='x')and(q[w-1]>='0' and q[w-1]<='9'):
                        z=pow(x,int(q[w-1]))
                    elif (q[w-2]=='x')and(q[w-1]=='x'):
                        z=pow(x,x )
                    else:pass
                    r.append(z)
                else:pass 
            else:
                if q[w]=='*':
                    z=None
                    e=0
                    for a in r:
                        if e==0:
                            z=a 
                            e+=1
                        else:
                            z*=a 
                elif q[w]=='/':
                    z=None
                    e=0
                    for a in r:
                        if e==0:
                            z=a 
                            e+=1
                        else:
                            z/=a 
                elif q[w]=='+':
                    z=None
                    e=0
                    for a in r:
                        if e==0:
                            z=a 
                            e+=1
                        else:
                            z+=a 
                elif q[w]=='-':
                    z=None
                    e=0
                    for a in r:
                        if e==0:
                            z=a 
                            e+=1
                        else:
                            z-=a 
                elif q[w]=='^':
                    z=None
                    e=0
                    for a in r:
                        if e==0:
                            z=a 
                            e+=1
                        else:
                            z=pow(z,a)
                else:pass
        return z 
    def solve_integ(self):
        try:
            self.c0=self._integ.text[0:-2]
            self.c1=self._integ.text[-1]
            s=self._integ_(int(self.c1))
            self._integ.text=str(s)
        except:
            toast('(a*x)/(x^a)/...-c\n>>(2*x)+(x^8)+(2*5)-6')


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style='Dark'

        return Style()

MainApp().run()