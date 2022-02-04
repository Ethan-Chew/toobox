
import random

SIZE=[40,40]
def init():
    global snake
    global food
    global direction
    global snakesize
    global SIZE
    
    
    snake=[(SIZE[0]//2,SIZE[1]//2)]
    snakesize=4
    food=(int(random.randint(0,SIZE[0])),int(random.randint(0,SIZE[1])))
    direction=[0,1]
def update():
    global snake 
    global food
    global direction
    global snakesize
    global SIZE

    if snake[0][0]==food[0] and snake[0][1]==food[1]:
        snakesize+=1
        while food in snake:
            food=(int(random.randint(0,SIZE[0])),int(random.randint(0,SIZE[1])))
    next=(snake[-1][0]+direction[0],snake[-1][1]+direction[1])
    if next[0]<0 or next[0]>SIZE[0] or next[1]<0 or next[1]>SIZE[1]:
        return False
    
    if next in snake:
        return False
    snake.append(next)
    if len(snake)>snakesize:
        snake.pop(0)
    return True
def get_inp(inp):
    global direction
    i=inp
    if i=="w":
        if direction==[-1,0] or direction==[1,0]:
            direction=[0,-1]
    elif i=="s":
        if direction==[-1,0] or direction==[1,0]:
            direction=[0,1]
    elif i=="a":
        if direction==[0,-1] or direction==[0,1]:
            direction=[-1,0]
    elif i=="d":
        if direction==[0,-1] or direction==[0,1]:
            direction=[1,0]
if __name__=="__main__":
    
    init()
    can =True
    while can:
        i=input()
        get_inp(i)
        can=update()
        print(snake)
        print("-"*SIZE[0])
        for i in range(SIZE[0],0,-1):
            line=""
            for j in range(SIZE[1],0,-1):
                
                coor=(i,j)
                if coor in snake:
                    line+="#"
                elif coor == food:
                    line+="$"
                else:
                    line+=" "
            print(line)            


