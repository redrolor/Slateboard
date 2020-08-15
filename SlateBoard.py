import pygame
pygame.init()

#PEN CONFIGURATIONS
#colors
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)
white=(255,255,255)

# #get pen size from user
# penSizeDefined=False
# while not penSizeDefined:
#     try:
#         penSize=int(input("Pen Size: "))
#         penSizeDefined=True
#     except:
#         print("Integer required. Please try again")
#
# #get eraser Size
# eraserSizeDefined=False
# while not eraserSizeDefined:
#     try:
#         eraserSize=int(input("Eraser Size: "))
#         eraserSizeDefined=True
#     except:
#         print("Integer required. Please try again")

#hardcoding penSize and eraserSize
penSize=15
eraserSize=20

#default color of pen when program starts
defaultColor=red
penColor=defaultColor

#window
window=pygame.display.set_mode((1600,1100))
pygame.display.set_caption("Drawing Tool")


#methods
def checkLeftClick(event):
    if event.type==pygame.MOUSEBUTTONDOWN:
        if event.button==1:
            return True
    return False
def checkLeftClickRaised(event):
    if event.type==pygame.MOUSEBUTTONUP:
        if event.button==1:
            return True
    return False
def checkRightClick(event):
    if event.type==pygame.MOUSEBUTTONDOWN:
        if event.button==3:
            return True
    return False
def checkRightClickRaised(event):
    if event.type==pygame.MOUSEBUTTONUP:
        if event.button==3:
            return True
    return False
def checkWheelTurnedForward(event):
    if event.type==pygame.MOUSEBUTTONDOWN:
        if event.button==4:
            return True
    return False
def checkWheelTurnedBackward(event):
    if event.type==pygame.MOUSEBUTTONDOWN:
        if event.button==5:
            return True
    return False
def checkWheelStopTurnedForward(event):
    if event.type==pygame.MOUSEBUTTONUP:
        if event.button==4:
            return True
    return False
def checkWheelStopTurnedBackward(event):
    if event.type==pygame.MOUSEBUTTONUP:
        if event.button==5:
            return True
    return False

def drawCircle(position,color,penSize):
    pygame.draw.circle(window,color,position,penSize)


run=True
while run:
    #program exit (not working)
    pygame.time.delay(25)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()

        #position of cursor printed
        print(pygame.mouse.get_pos())

        #PEN
        #changes pen color based on key pressed
    #    for  e in pygame.event.get():
        keys=pygame.key.get_pressed()
        if keys[pygame.K_r]:
            penColor=red
        if keys[pygame.K_g]:
            penColor=green
        if keys[pygame.K_b]:
            penColor=blue
        if keys[pygame.K_c]:
            window.fill(black)
            pygame.display.update()

        #left click with hold entering the while loop
        if checkLeftClick(event):
            leftClicked=True
            while leftClicked:
                print("left clicked")
                pos=pygame.mouse.get_pos()
                drawCircle(pos, penColor, penSize)
                pygame.display.update()
                for e in pygame.event.get():
                    if checkLeftClickRaised(e):
                        leftClicked=False

        #ERASER
        #right click with hold entering the while loop
        if checkRightClick(event):
            rightClicked=True
            while rightClicked:
                print("right clicked")
                pos=pygame.mouse.get_pos()
                drawCircle(pos, black, eraserSize)
                pygame.display.update()
                for ev in pygame.event.get():
                    if checkRightClickRaised(ev):
                        rightClicked=False

        #scroll forward increases pen size
        if checkWheelTurnedForward(event):
            turnedForward=True
            count=0
            while turnedForward:
                count+=1
                print("wheel turned forward")
                penSize+=1
                for e in pygame.event.get():
                    if checkWheelStopTurnedForward(e):
                        turnedForward=False
                        break
                #when single click scroll, wheel is thought to keep scrolling
                #This exits check loop after x loops, decrease for higher precision
                if count>1:
                    break

        #scroll backward decreases pen size
        if checkWheelTurnedBackward(event):
            turnedBackward=True
            count=0
            while turnedBackward:
                count+=1
                print("wheel turned backward")
                if penSize>0:
                    penSize-=1
                for e in pygame.event.get():
                    if checkWheelStopTurnedBackward(e):
                        turnedBackward=False
                        break
                #when single click scroll, wheel is thought to keep scrolling
                #This exits check loop after x loops, decrease for higher precision
                if count>5:
                    break
