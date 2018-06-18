import random

global userinput

global val

print("====----Welcome to the game of greed----====")

p1=raw_input("====----Please enter your name player 1----====")

p2=raw_input("====----Please enter your name player 2----====")

player1_score=0

player2_score=0

swap=2

player1_entered=False

player2_entered=False

val=0

def player1():

    global swap,a

    swap=1

    print p1,"score till now ",player1_score

    a=input("type 0 to play GREED ")

    if a==0:

        play()

    else:

        exit()

def player2():

    global swap,b

    swap=2

    print p2,"score till now ",player2_score

    b=input("type 0 to play GREED ")

    if b==0:

        play()

    else:

        exit()



def swapplayers():



    global swap

    if swap==2:

        player1()

    if swap==1:

        player2()

    









def play():

    global l

    l=[random.randint(1,6) for i in range(1,6)]

    print l

    no_of_times()



def no_of_times():

    global n1,n2,n3,n4,n5,n6,l,n

    n1=l.count(1)

    n2=l.count(2)

    n3=l.count(3)

    n4=l.count(4)

    n5=l.count(5)

    n6=l.count(6)

    n=[n1,n2,n3,n4,n5,n6]

    countscore()



def countscore():

    global n1,n2,n3,n4,n5,n6,l,n,val

    val=0

    if n1>2:

        val+=1000

        n1=n1-3



    else:

        for i in l:

            if l.count(i)>2:

                val+=100*i

                if i==5:

                        n5=n5-3

                break



    if n5>0:

        for i in range (n5):

                val+=50



    if n1>0:    

        for i in range (0,n1):

            val+=100

  

    n[0]=0

    n[4]=0





    print "===-Score is: ",val



    if val==0 and swap==1:

        player1_score=0

        swapplayers()

    if val==0 and swap==2:

        player1_score=0

        swapplayers()

    

    entry()

    

def entry():

    global n1,n5,n,player1_entered,player2_entered,player1_score,player2_score

    global val

    

    

    

    if swap==1 and val>=300 and player1_entered==False:

        player1_entered=True

        print "Player1 you are In!!!"



    if swap==2 and val>=300 and player2_entered==False:

        player2_entered=True

        print "Player2 you are in!!!"



    if swap==1 and player1_entered==True:

        player1_score=player1_score+val

        greed_test()



    if swap==2 and player2_entered==True:

        player2_score=player2_score+val

        greed_test()

    if player1_score>=3000:

         print "===---You survived the game of greed",p1,"Congratulations!---==="

    if player2_score>=3000:

         print "===---You survived the game of greed",p2,"Congratulations!---==="



    else:

        print val

        swapplayers()





def greed_test():

    

     userinput=raw_input('===---GREED OR SAFE? type y or n ---===')

     if userinput=='y':

         greed_again()

     if userinput=='n':

        swapplayers()

     

     else:

         greed_test()



def greed_again():

    for i in l:

        if i>1 & i<5 & i>5 & l.count(i)==3:

            play()

            break

        else:

            playnextplayer()

            break



def playnextplayer():

    global n

    total=0

    global l

    for i in n:

        total=total+i

    print "You could play",total,"times!"

    l=[random.randint(1,6) for i in range(total)]

    print l



    no_of_times()


swapplayers()
