from pyautogui import *
import pydirectinput
import time


from python_imagesearch.imagesearch import imagesearch

#Define interacting with the dog
def interact_with_dog():
    print('Interating with dog.')
    #<3 you ethan 
    for i in range(25) :
        pydirectinput.keyDown("z")
        pydirectinput.keyUp("z")
        time.sleep(.1)   

    
#Delay before the program Starts
time.sleep(3)

while True:

    #Go into the cave
    pydirectinput.keyDown('up')
    pydirectinput.keyUp('up')

    #Wait for fade
    time.sleep(1)

    #Search for dog
    pos = imagesearch("./stray_dog.png",precision = 0.7) 

    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
    else:
        print("image not found")

    #If position one.
    if pos[1] == 288: 
        print("Dog at position one.")
        #Find x axi
        pydirectinput.keyDown('up')
        pydirectinput.keyUp('up')

        pydirectinput.keyDown('up')
        pydirectinput.keyUp('up')

        pydirectinput.keyDown('up')
        pydirectinput.keyUp('up')

        #Find y axi
        pydirectinput.keyDown('right')
        pydirectinput.keyUp('right')

        pydirectinput.keyDown('right')
        pydirectinput.keyUp('right')

        pydirectinput.keyDown('right')
        pydirectinput.keyUp('right')
        print('At dog.')
        #Run function

        interact_with_dog()

        #Get your ass outta there
        pydirectinput.keyDown('left')
        pydirectinput.keyUp('left')

        pydirectinput.keyDown('left')
        pydirectinput.keyUp('left')

        pydirectinput.keyDown('left')
        pydirectinput.keyUp('left')

        pydirectinput.keyDown('down')
        pydirectinput.keyUp('down')
        
        pydirectinput.keyDown('down')
        pydirectinput.keyUp('down')

        pydirectinput.keyDown('down')
        pydirectinput.keyUp('down')
        #Nice job omori
        print('Loop finished')    


    






    #If position two.
    if pos[1] == 96:
        print('Dog at position two.')
        #Go Up
        pydirectinput.keyDown('up')
        pydirectinput.keyUp('up')

        pydirectinput.keyDown('up')
        pydirectinput.keyUp('up')

        pydirectinput.keyDown('up')
        pydirectinput.keyUp('up')

        pydirectinput.keyDown('up')
        pydirectinput.keyUp('up')
        #Go Right
        pydirectinput.keyDown('right')
        pydirectinput.keyUp('right')

        pydirectinput.keyDown('right')
        pydirectinput.keyUp('right')

        pydirectinput.keyDown('right')
        pydirectinput.keyUp('right')
        #Go Up 
        pydirectinput.keyDown('up')
        pydirectinput.keyUp('up')
        #Go Right     
        pydirectinput.keyDown('right')
        pydirectinput.keyUp('right')
        #Go Up 
        pydirectinput.keyDown('up')
        pydirectinput.keyUp('up')
        print('At dog.')

        #Interact with the dog
        interact_with_dog()
        

        #Get your ass outta there
        pydirectinput.keyDown('left')
        pydirectinput.keyUp('left')

        pydirectinput.keyDown('down')
        pydirectinput.keyUp('down')

        pydirectinput.keyDown('left')
        pydirectinput.keyUp('left')

        pydirectinput.keyDown('left')
        pydirectinput.keyUp('left')

        pydirectinput.keyDown('left')
        pydirectinput.keyUp('left')

        pydirectinput.keyDown('down')
        pydirectinput.keyUp('down')
        
        pydirectinput.keyDown('down')
        pydirectinput.keyUp('down')

        pydirectinput.keyDown('down')
        pydirectinput.keyUp('down')

        pydirectinput.keyDown('down')
        pydirectinput.keyUp('down')
        #Nice job omori
        print('Loop finished')

    #If position three
    if pos[1] == 160:
        print('Dog at position three.')

        #Find Dog up(4), right(2), up(1)
        pydirectinput.keyDown('up')
        pydirectinput.keyUp('up')

        pydirectinput.keyDown('up')
        pydirectinput.keyUp('up')

        pydirectinput.keyDown('up')
        pydirectinput.keyUp('up')

        pydirectinput.keyDown('up')
        pydirectinput.keyUp('up')

        pydirectinput.keyDown('right')
        pydirectinput.keyUp('right')
        
        pydirectinput.keyDown('right')
        pydirectinput.keyUp('right')

        pydirectinput.keyDown('up')
        pydirectinput.keyUp('up')
        
        #Interact with the dog
        interact_with_dog()      

        #Get your ass outta there
        pydirectinput.keyDown('down') 
        pydirectinput.keyUp('down')

        pydirectinput.keyDown('down') 
        pydirectinput.keyUp('down')

        pydirectinput.keyDown('left') 
        pydirectinput.keyUp('left')

        pydirectinput.keyDown('left') 
        pydirectinput.keyUp('left')

        pydirectinput.keyDown('down') 
        pydirectinput.keyUp('down')

        pydirectinput.keyDown('down') 
        pydirectinput.keyUp('down')

        #Nice job omori
        print('Loop finished')


    #Go out of the cave
    pydirectinput.keyDown('down')
    pydirectinput.keyUp('down')
    time.sleep(1)
        
     
        
        

