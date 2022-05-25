from email.mime import image
from tokenize import group
from turtle import circle
from cmu_graphics import*


bild1=Image('skög.png' , 0, 0, height=400, width=400)
bild2=Image('skög.png' , 0, -400, height=400, width=400)
bomber=Image('bomber.png', 200,18,height=65.7, width=70)
player=Image('plan.png', 200,300,height=50, width=40)
fighter=Image('enemyfighter.png',300,18,height=30,width=30)

#hälsa 
app.hp=100 
bar = Rect(5,4,110,8,fill='red')
text_hp = Label(app.hp,130,7,size=10, fill='red')
fighter.hp= 40
bomber.hp=100

#grupper
bullets = Group()
fiender = Group()
bombers= Group()
bombs1= Group()
bombs2= Group()
bombs3= Group()



bombers.add(bomber)
fiender.add(fighter,bomber)





app.steps=0 
###skada
bomber_crash=25
fighter_crash=5
player_dmg=10  
###hastigheter
scrolspeed=0.5
player.speed=3
bomberSpeed=0.8
fighterSpeed=1.3
bullets_speed=8
bombs1_speed = 3
bombs2_speedy= 3
bombs2_speedx = ((bombs2_speedy**2)/2)**(1/2)
bombs3_speedy= 3
bombs3_speedx = -((bombs2_speedy**2)/2)**(1/2)
def pShooting():
    bullets.add(Image('pfire.png',player.centerX,player.centerY,height=8.6,width=5))
    

def bShooting():
    bombs1.add(Image('pfire.png',bomber.centerX,bomber.centerY,height=8.6,width=5))
    bombs2.add(Image('pfire.png',bomber.centerX,bomber.centerY,height=8.6,width=5))
    bombs3.add(Image('pfire.png',bomber.centerX,bomber.centerY,height=8.6,width=5))
    #bombs1.add(Circle(bomber.centerX, bomber.centerY,5))
    #bombs2.add(Circle(bomber.centerX, bomber.centerY,5))
    #bombs3.add(Circle(bomber.centerX, bomber.centerY,5))


def onStep():
    app.steps+=1
    global fighter
    bild1.centerY += scrolspeed
    bild2.centerY += scrolspeed
    if bild1.top==400:
        bild1.top=-400
    elif bild2.top == 400:
        bild2.top=-400
    if app.steps % 35 ==  0 and bomber.bottom<400 and bomber.visible== True:
        bShooting()
    for bomb in bombs1:
            bomb.centerY += bombs1_speed
    
    for bomb in bombs2:
        bomb.centerX += bombs2_speedx
        bomb.centerY += bombs2_speedy
    for bomb in bombs3:
        bomb.centerX += bombs3_speedx
        bomb.centerY += bombs3_speedy
   
    if bomber.top<= 400:
        bomber.centerY += bomberSpeed 
    fighter.centerY += fighterSpeed
    for bullet in bullets:
        bullet.centerY -=bullets_speed
    if 400.8>bomber.bottom > 400 and bomber.visible==True :
        bar.width-=bomber_crash
        text_hp.value -= bomber_crash
    elif 401.3>fighter.bottom>400 and fighter.visible==True :
        bar.width-=fighter_crash
        text_hp.value -= fighter_crash
    
    for bullet in bullets:
        if bullets.hitsShape(fighter) :
            fighter.hp -= player_dmg
        if bullets.hitsShape(bomber) :
            bomber.hp -= player_dmg
        for fiende in fiender:
            if bullet.hitsShape(fiende) :
                bullets.remove(bullet)
            if bullet.bottom==0:
                bullets.remove(bullet)
    
            
    
     
      

        

    
    if fighter.hp<=0:
        fighter.visible= False
    
    if bomber.hp<=0:
        bomber.visible= False
   

        

def onKeyHold(keys):
    if 'up' in keys and 'left' in keys:
        player.centerX -= ((player.speed**2)/2)**(1/2)
        player.centerY -= ((player.speed**2)/2)**(1/2)
            
    elif 'up' in keys and 'right' in keys:
        player.centerX += ((player.speed**2)/2)**(1/2)
        player.centerY -= ((player.speed**2)/2)**(1/2)
            
    elif 'down' in keys and 'right' in keys:
        player.centerX += ((player.speed**2)/2)**(1/2)
        player.centerY += ((player.speed**2)/2)**(1/2)
            
    elif 'down' in keys and 'left' in keys:
        player.centerX -= ((player.speed**2)/2)**(1/2)
        player.centerY += ((player.speed**2)/2)**(1/2)
            
    elif 'up' in keys:
        player.centerY -= player.speed
            
    elif 'down' in keys:
        player.centerY += player.speed
            
    elif 'left' in keys:
        player.centerX -= player.speed
            
    elif 'right' in keys:
        player.centerX += player.speed
    
    # skjuta
    if 'f' in keys and app.steps%7==0:
        pShooting()
    
   

   

            




cmu_graphics.run()