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

def pShooting():
    bullets.add(Image('pfire.png',player.centerX,player.centerY,height=8.6,width=5))
   

def onStep():
    app.steps+=1
    global fighter
    bild1.centerY += scrolspeed
    bild2.centerY += scrolspeed
    if bild1.top==400:
        bild1.top=-400
    elif bild2.top == 400:
        bild2.top=-400
    
    # saker som rör sig konstant
    bomber.centerY += bomberSpeed 
    fighter.centerY += fighterSpeed
    for bullet in bullets:
        bullet.centerY -=5
    if 400.8>bomber.bottom > 400 :
        bar.width-=bomber_crash
        text_hp.value -= bomber_crash
    elif 401.3>fighter.bottom>400 :
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
            
    for fiende in fiender:
        if fiende.top>400:
            fiender.remove(fiende)
     
    print(fighter.hp)   

        

    
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