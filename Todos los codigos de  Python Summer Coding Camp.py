#1 )Say "Hello, World!" With Python
print("Hello, World!")

#2) Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    s = a+b 
    r = a-b
    m = a*b
    print(s)
    print(r)
    print(m)
#3 Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
#4 Loops
if __name__ == '__main__':
    n = int(input())
i=0
while i in range (0,n):
    print(i**2)
    i = i + 1
#5 Calendar Module
import calendar

fecha = input().split()
año,mes,dia = int(fecha[2]),int(fecha[0]),int(fecha[1])
dia_de_semana = calendar.weekday(año,mes,dia)
nombre_de_dia = calendar.day_name[dia_de_semana]
print(nombre_de_dia.upper())

#6 Text Wrap

import textwrap
def wrap(string, max_width): 
    return textwrap.fill(string,max_width)
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#7 String Split and Join
def split_and_join(line):
    # write your code here
    
    line = line.split()
    line = "-".join(line)
    return line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
#8 sWAP cASE
def swap_case(s):
    cad = s.swapcase()
    return cad

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#9 String Validators
if __name__ == '__main__':
    s = input()
#Caracteres alfanumericos
print (any(letra.isalnum() for letra in s))

#Caracteres alfabeticos
print (any(letra.isalpha() for letra in s))

#Digitos
print (any(letra.isdigit() for letra in s))

#Minusculas
print (any(letra.islower() for letra in s))

#Mayusculas
print (any(letra.isupper() for letra in s))

#### La funcion any() devuelve True si algun elemento
## de un iterable es True y se compara mediante el for

#10 Lists
if __name__ == '__main__':
    N = int(input())
    lista = []

    for x in range(N):
        renglon = input().split()
        if (renglon[0] == 'insert'):
            lista.insert(int(renglon[1]),int(renglon[2]))
        elif (renglon[0] == "print"):
            print(lista)
        elif (renglon[0] == "remove"):
            lista.remove(int(renglon[1]))
        elif (renglon[0] == "append"):
            lista.append(int(renglon[1]))
        elif(renglon[0] == "sort"):
            lista.sort()
        elif (renglon[0] == "pop"):
            lista.pop()
        elif(renglon[0] == "reverse"):
            lista.reverse()
#11 Print function
if __name__ == '__main__':
    n = int(input())
    cadena = ''
    if n > 0 and n < 151 :
        for i in range (1,n+1):
            cadena += str(i)
    print(cadena)


#12 What's Your Name?
def print_full_name(a, b):
    print("Hello "+ a + " " + b + "! You just delved into python.")
    if __name__ == '__main__':
        first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


#13 Exceptions
if __name__== '__main__':
    for _ in range(int(input())):
        a = input()
        a = a.split(" ")
        b = a[0]
        c = a[1]

        try:
            print(int(b)//int(c))
        
        except ZeroDivisionError as c:
            print(f'Error Code: {c}')
        except ValueError as d:
            print(f'Error Code: {d}')



#14 Words Score

def score_words(words):
    def is_vowel(letter):
        return letter in ['a', 'e', 'i', 'o', 'u', 'y']
    
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
           score +=1
    return score


n = int(input())
words = input().split()
print(score_words(words))

#15 Nested Lists
if __name__ == '__main__':
       lista = []
   scores = []
   for _ in range(int(input())):
       name = input()
       score = float(input())
       lista.append([name,score])
       scores.append(score)

datos = sorted(set(scores))

segundos = []
for i in range(len(datos)):
    if lista[i][1] == datos [1]:
        segundos.append(lista[i][0])

for e in sorted(segundos):
    print(e)

# 16 Powe - Mod Power
a = int (input())
b = int (input())
m = int (input())

print(pow(a,b))
print(pow(a,b,m))

#17 Mod divmod

a = int(input())
b = int(input())

print(a//b)
print(a%b)
print(divmod(a,b))

#18 Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    lista = []
    for i in arr:
        lista.append(i)

    lista_ordenada = sorted(set(lista),reverse=True)
    print(lista_ordenada[1]) 

#19 Python If-Else

if __name__ == '__main__':
    n = int(input().strip())
    if n%2 ==1 or (n in range(6,21)) : print("Weird")
    elif n%2 == 0 and ((n in range(2,6)) or n>20): print("Not Weird")

#20 Classes: Dealing with Complex Numbers
class Complex(object):
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self,no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return Complex(real,imaginary)

    def __sub__(self,no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return Complex(real,imaginary)

    def __mul__(self,no):
        real = (self.real*no.real)-(self.imaginary*no.imaginary)
        imaginary = (self.real*no.imaginary)+(self.imaginary*no.real)
        return Complex(real,imaginary)

    def __truediv__(self,no):
        div = (no.real**2)+(no.imaginary**2)
        real = ((self.real*no.real)+(self.imaginary*no.imaginary))/div
        imaginary = ((self.imaginary*no.real)-(self.real*no.imaginary))/div
        return Complex(real,imaginary)
    
    def mod(self):
        real = math.sqrt((self.real**2)+(self.imaginary**2))
        return Complex(real,0) 
    
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
    if __name__ == '__main__':
        c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')

#21 Integers Come In All Sizes
a = int (input())
b = int (input())
c = int (input())
d = int (input())
print ((a**b)+(c**d))

#22 Any or All

N = int(input())
numbers = input().split()
print(all([int(number)>0 for number in numbers]) and any ([str(number)==str(number)[::-1]for number in numbers]))

#23 Mutations

def mutate_string(string,position,character):
    l =  list(string) #Convertimos a lista
    l[position] = character #Ahora a caracter
    cadena = ''.join(l)
    return cadena

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
#24 Python Evaluation

cadena = input()
A_evaluar = cadena[6:len(cadena)-1] #Obtencion de la cadena
print(eval(A_evaluar))

#25 Map and Lambda Function
cube = lambda x: x**3 # lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    f=[]
    a,b = 0,1
    for i in range (n):
        f.append(a)
        a,b = b,a+b
    return f

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))