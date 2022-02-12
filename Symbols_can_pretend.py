from turtle import*

x=-300
y=300
up()
setpos(-300,300)
down()
speed(300)
def sq1():
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    fd(10)

a=open('code.txt','r')
a=a.read()
b=''
p=0
for i in a:
    if p==25:
        p=0
        b+='\n'
        y-=10
        up()
        setpos(x,y)
        down()
    p+=1
    if i=='0':
        b+='.'
        up()
        fd(10)
        down()
    else:
        b+='*'
        sq1()
print(b)
    
