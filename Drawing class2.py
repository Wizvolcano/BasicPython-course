import turtle
tao = turtle.Pen() #ดึงความสามารถปากกา
tao.shape('turtle') #แปลงร่างเป็นเต่า
def Rectangle():
    '''Fx นี้เอาไว้วาดรูปสี่เหลี่ยม'''
    for i in range(4):
        tao.fd(100)
        tao.lt(90)
        
def Go(x,y):
    '''Fx นี้เอาไว้ย้ายเต่าไปตำแหน่งที่ต้องการ'''
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

def Circle():
    '''Fx นี้เอาไว้วาดวางกลมซ้อนกัน'''
    for i in range(10):
        tao.circle(100)
        tao.left(36)

Go(300,300)
Rectangle()

Go(-300,300)
Rectangle()

Go(300,-300)
Rectangle()

Go(-300,-300)
Rectangle()

Go(50,50)
Circle()

