'''
Author: Quyen Tran
Date due: 4/26/24
Program Description: A small game with character customization and choose your own story

Plan:
Character Customization:
1.Name
2.Age
3.Randomly generated skills and abilities (strength, agility, intelligence)
4. Personalized companion that can help them during the journey (a pug dog, a black chunky cat, a rat)

Plot:
They're in the hunger games and they have to survive.

1.Game starts with a count down from 10, the user has the choice to run to the middle or to the forest
2.if you go to the center, you have the potential to get a sword and an ally named Rory.
2.if you go to the forest, you have the potential to get an ally named Serena and find water.

There will be 3 endings:
1.Lone Victor where you kill everyone by yourself and lose your mind
2.Sacrifice where you die for your partner
3.Going home where you and your partner go home together

'''
import time
import random
import sys
def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)

def display_and_wait(message):
    print(message)
    input("Press enter to continue...")

def checkHealth(userHealth):
    if(userHealth <= 0):
        print("\n\nYou died! Game over!")
        sys.exit()

def print_stats(health, sanity, intel, strength, agility):
    #adds all the stats to a list so i can iterate through it in a loop
    aList= []
    aList.append(health)
    aList.append(sanity)
    aList.append(intel)
    aList.append(strength)
    aList.append(agility)

    #stats cap at 100 so if a stat is greater than 100, just print 100
    #stats also minimum has to be 0 so don't print negative stats
    for i in range(len(aList)):
        if (aList[i] > 100):
            aList[i] = 100
        elif (aList[i] < 0):
            aList[i] = 0

    print(f"Health: {aList[0]}")
    print(f"Sanity: {aList[1]}")
    print(f"Intellience: {aList[2]}")
    print(f"Strength: {aList[3]}")
    print(f"Agility: {aList[4]}")


def run():
    #Exposition, getting user information for character customization
    userName = input("You're in a raffle! Enter your name: ")
    userAge = int(input("Enter your age: "))

    userIntel = random.randint(0, 100)
    userStrength = random.randint(0, 100)
    userAgility = random.randint(0,100)
    userHealth = 100
    userSanity = 100

    decision = 0

    #ally related variables
    haveAlly = 0 #set 0 at default but when user gets an ally, it will be set to 1 for true
    allyName = "placeholder" #once they find an ally, their name will fill this spot
    allyScore = 20 #a range from 0-100

    #weapon related variables
    haveWeapon = 0 #set 0 at default but when user gets an ally, it will be set to 1 for true
    weaponType = 0 #0 = no weapon, 1 = bow and arrow with Rory, 2 = sword with Serena





    if(userAge > 12 ):
        display_and_wait("\nCongratulations! You have been chosen to be a representative of District 12 for the 74th annual Hunger Game!")
    else:
        print("You are too young and cannot participate in this year's Hunger Game. ")
        sys.exit()

    #prints the user's skills so the user knows what their character is capabale of
    display_and_wait("\nBelow are your stats on a range from 0-100: ")
    print_stats(userHealth,userSanity,userIntel,userStrength,userAgility)
    print("\nWhen your health reaches zero, you will die!")
    display_and_wait("\nThese stats will affect the flow of the story.")


    display_and_wait("\nYour story will begin here. Good luck on winning the Hunger Games!")
    display_and_wait("\nYou open your eyes and realize you're standing on a rising platform.")
    display_and_wait("\nYou don't have time to make sense of your situation as you hear a timer ring in your ears.")

    #a coutdown that counts down from the argument that's passed
    countdown(3)

    display_and_wait("\nA loud horn blares. Some people bolt towards the center of the arena while others book it in the opposite direction")

    #decision: choose to go to the center or not
    print("\nMake your decision!\n1.Go to the center of the arena \n2.Turn and run to the woods")

    decision = int(input("Enter 1 or 2: "))
    while (decision != 1 and decision != 2):
        if (decision != 1 and decision != 2):
            print("\nThat is not a valid option!")
            print("\nPlease try again!")
            decision = int(input("\nEnter 1 or 2: "))

#-----------------------------------------------------------------------------------------------------------------------------

    #if user decides to run to the center of arena
    if (decision == 1):
        display_and_wait("\nYou run as fast as you can to the center! You spot a bow and arrow that has not yet been taken.")
        display_and_wait("\nYou make eye contact with a tall man as you both launch towards the bow and arrows.")
        #if user has an agility score higher than 60, they survive and have the possibility of getting an ally
        if (userAgility>30):
            haveWeapon = 1
            weaponType = 1 #type 1 weapon is a bow and arrows
            display_and_wait("\nYour impressive agility allows you to grab the bow and arrows before the man could.")
            display_and_wait("\nYou see the man put his hands up in defeat.")
            print("\nMake your decision!\n1.Spare him\n2.Kill him")
            decision = int(input("Enter 1 or 2: "))
            #if user spares the man then they will get an ally, if not, they will lose sanity but gain strength
            #ALLY option 1: you get Rory as an ally--------------------------------------------------------------
            if(decision == 1):
                display_and_wait("\nThe man, who calls himself Rory, swears he will repay you for showing him mercy.")
                display_and_wait("\nCongrats! You have made a new ally!")
                haveAlly = 1
                allyName = "Rory"
            #if user decides to kill Rory, they will die
            #DEATH option 2: you die
            else:
                display_and_wait("\nYou shoot the man in the chest without hesitation!")
                display_and_wait("\nHowever, when you turn around, you feel a blade pierce through your chest too.")
                display_and_wait("\nAnother tribute has stabbed you!")
                userHealth -=100
                checkHealth(userHealth)
        #DEATH option 3: you die because your stats in agility is too low-----------------------------------------------------
        #if user's agility score is less than 30, they will die
        else:
            display_and_wait("\nOh no! You're too slow! The man grabs the bow and arrows before you!")
            display_and_wait("\nThe man is approaching you with a menacing glare!")
            display_and_wait("\nYou turn and run away but it is to no avail.")
            display_and_wait("\nYou feel an arrow puncture through your chest and your vision quickly fades to black.")
            userHealth -= 100
            checkHealth(userHealth)


#________________________________________________________________________________________________________________________


    #if user decides to run to the woods instead of going to center
    else:
        display_and_wait("\nYou dash straight into the woods without looking behind you")
        display_and_wait("\nAfter 5 minutes of nonstop running, you are exhausted.")
        display_and_wait("\nStopping to catch your breath, you hear the sound of trickling water!")
        display_and_wait("\nYou are very thirsty,so you decide to follow the sound")
        display_and_wait("\nAfter a few minutes of searching, you find a rushing river!")
        display_and_wait("\nDelighted, you almost rush and jump into the water. But, the sound of a blades clashing stop you in your tracks!")
        display_and_wait("\nYou hide yourself in a bush as you watch the fight before you unfold.")
        display_and_wait("\nThe fight is between a blonde woman and a brown-haired man.")
        display_and_wait("\nThe man is burly and slow, but his confidence does not wane as he is armed with"
                             " a sword. \nMeanwhile, the blonde womnan, although evidently stronger and more agile than the man, "
                             "is at a disadvantage without a weapon.")
        display_and_wait("\nThe two fight for some time. The blonde woman manages to evade countless of the man's attacks. "
                             "However, it's clear her stamina has nearly run out")
        print("\nMake your decision!\n1.Reveal yourself and help the blonde woman\n2.Stay hidden and continue watching the fight")
        decision= int(input("Enter 1 or 2: "))
        #if user decides to help the blonde woman win the fight
        #ALLY option 1: you will get Serena as your teammate regardless it's you or Serena who kills the man--------------------------------------------------
        if(decision==1):
            #haveAlly is set to true if the user decides to help the blonde woman
            haveAlly = 1
            allyName = "Serena"

            #you get the sword of the man's
            haveWeapon = 1
            weaponType = 2 #sword
            display_and_wait("\nYou rush out of the bush to make a surprise attack on the brown-haired man")
            display_and_wait("\nThe blonde woman is at first surprised by your arrival, but she quickly regains her composure")
            if(userStrength>30):
                display_and_wait("\nWith yours and the blonde woman's combined strength, you manage to overpower the man!")
                display_and_wait("\nYou see an opening and you have the opportunity to strangle the man to death")
                print("\nMake your decision!\n1.Strangle the man to death\n2.Hesitate")
                decision = int(input("Enter 1 or 2: "))
                #if user decides to stangle the man to death while helping blonde woman
                if (decision==1):
                    display_and_wait("\nYou grip onto the man's neck with all your strength!")
                    display_and_wait("\nThe man struggles vehemently, but after a few moments, his struggling stops.")
                    display_and_wait("\nYou have killed the man.")
                    display_and_wait("\nThe image of his bloodshot eyes imprints itself into your brain.")
                    userSanity -=10
                    userStrength +=10
                    display_and_wait("\nYour stats have changed!")
                    print_stats(userHealth,userSanity,userIntel,userStrength,userAgility)
                    display_and_wait("\nCongratulations! You have made an ally!")
                    display_and_wait("\nThe blonde woman,who calls herself Serena, has declared you guys as teamates!")
                    #if user decides to hesitate and not strangle the man
                else:
                    display_and_wait("\nYou hesitate, unable to find it in yourself to kill another life.")
                    display_and_wait("\nThe blonde woman sees your hesitation and takes matters into her own hands.")
                    display_and_wait("\nShe tackles him to the ground!")
                    display_and_wait("\nKicking the sword out of his hands, she begins to strangle him!")
                    display_and_wait("\nIn utter shock, you can only watch as the man's eyes slowly lose focus until "
                                         "he looks like nothing but the shell of himself")
                    display_and_wait("\nAfter killing the man, the blonde woman gets up from the ground and paces towards you.")
                    display_and_wait("\nYou are gripped with fear when she stretches her hand towards you.")
                    display_and_wait("\nHowever, your fear quickly dissipates when you realize the woman was simply offering a handshake.")
                    display_and_wait("\nCongratulations! You have made an ally!")
                    display_and_wait("\nThe blonde woman, who calls herself Serena, has declared you guys as teamates!")
                #if the user's strength score is less than 30, both they and the blonde woman will die
                #DEATH option 2: both you and the blond woman dies because your strength stats are too low-------------------------------------
            else:
                display_and_wait("\nYour level of strength is too low! You only get in the way for the blonde woman")
                display_and_wait("\nThe man overpowers the both of you!")
                userHealth -= 100
                checkHealth(userHealth)
        #if user decides to not help the blonde woman, they will die
        #DEATH option 3:
        else:
            display_and_wait("\nYou continue to watch the fight.")
            display_and_wait("\nAfter a while of evading attacks, the blonde woman is backed into a corner.")
            display_and_wait("\nUnable to dodge the attacks any longer, the woman stops and shuts her eyes, calmly accepting her demise.")
            display_and_wait("\nWitnessing the following horrific sight, your mind is clouded by a brooding storm and a gasp escapes your lips.")
            display_and_wait("\nUnfortunately, the brown-haired man's alert senses picks up on the sound.")
            display_and_wait("\nHe storms over to the bush you're hiding, and without giving you the chance to react, he swings the blade down onto you.")
            userHealth -=100
            checkHealth(userHealth)







    #conversations and building allyScore arc
    #__________________________________________________________________________________________________________________

    #if the user has an ally
    if (haveAlly):

        display_and_wait(f"\nThis is your current relationship score with your ally: {allyScore} "
              f"\nTry to maintain a good relationship with them for the best ending!")
        #if the ally is RORY
        if(len(allyName) == 4):
            display_and_wait("\nNow as allies, you and Rory have been treking through the forest in complete silence.")
            display_and_wait("\nYou want to say something but feel a pressure to keep quiet.")
            display_and_wait("\nSomething about nearly killing each other puts a real damper on the relationship")
            display_and_wait("\nDeciding you want to break the silence, you contemplate what topics to talk about with Rory")
            print("\nMake your decision!\n1.Talk about each other's past\n2.Talk about something casual")
            decision  = int(input("Enter a number 1 or 2: "))

            #you choose to talk about each other's past
            if (decision == 1):
                display_and_wait("\nWith a topic in mind, you muster the courage to start the conversation")
                display_and_wait("\n\tYou: So, what district are you from?")
                display_and_wait("\nThere's a pause in Rory's movements, as if he was caught off-guard.")
                display_and_wait("\n\tRory: I'm from District 1. ")
                display_and_wait("\nHearing his answer, you recall hearing that tributes from District 1 were trained from birth to become "
                                 "killing machines. You decide not to address that rumor.")
                display_and_wait("\n\tYou: I'm from District 12. We're a whole bunch of coal miners.")
                display_and_wait("\n\tYou: To be honest, I'm still finding it hard to grasp my current situation.\n\tOne day I'm"
                                 " at home with my family and the next day I'm stranded in a forest talking to someone who tried to kill me earlier.")
                display_and_wait("\nAnother pause from Rory.")
                display_and_wait("\n\tYou: I'm just joking.")
                display_and_wait("\nYou fake an awkward laugh and Rory only stares at you as a response")
                display_and_wait("\n\tYou: In your defense, I was trying to kill you too. It's okay though. No harm was done. For neither of us.")
                display_and_wait("\n\tYou: I mean we're just playing by the rules of the game. Can we really be blamed?")
                display_and_wait("\nIt's a rhetorical question, but Rory gives you an answer.")
                display_and_wait("\n\tRory: No. We are simply the chess pieces. We are not the players.")
                display_and_wait("\nNot expecting that answer, you forget about your filter and find yourself speaking before thinking")
                display_and_wait("\n\tYou: I didn't expect to hear a tribute from District 1 to say that.")
                display_and_wait("\nYou realize your mistake when you see the solemn look in Rory's eyes.")
                display_and_wait("\n\tRory: What is it that you're expecting from a tribute from District 1?")
                display_and_wait("\nYou don't have the time to think of an answer as Rory continues.")
                display_and_wait(f"\n\tRory: Tell me, {userName}. Are you scared of me?")
                print("\nMake your choice!\n1.Yes\n2.No")
                decision = int(input("Enter 1 or 2: "))

                #user tells Rory they're afraid of him
                if (decision == 1):
                    display_and_wait("\n\tYou: Isn't it normal for people to be afraid of you?")
                    display_and_wait("\n\tYou: Your district is known for being the best in these Hunger Games where the main goal is to kill people.")
                    display_and_wait("\nWhen you raise your head up to look at Rory, he's glaring holes into your face.")
                    display_and_wait("\nYou have the slight suspicion that was not the right thing to say.")
                    allyScore -= 20
                    display_and_wait(f"\nYour relationship with your ally has worsened!"
                                     f"\nYour current relationship score with Rory is {allyScore}")

                #user tells Rory they're not afraid of him
                else:
                    display_and_wait("\n\tYou: Why would I be scared of you?")
                    display_and_wait("\n\tYou: It was I who spared you, not the other way around")
                    display_and_wait("\nYou begin to laugh. After, you belatedly realize that Rory is watching you.")
                    display_and_wait("\n\tYou: Ahem, look I don't care where you're from. You're not scary.\n\tIn fact, if I had to describe you "
                                     "in one word, I would say you're slow.")
                    display_and_wait("\nRory gives you a peculiar look, and you feel a sense of pride as you begin to explain")
                    display_and_wait("\n\tYou: Because if you were faster, it wouldn't be me "
                                     "who's swinging around this bow and arrow on my back")
                    display_and_wait("\nYou laugh, feeling prideful of your agility.")
                    display_and_wait("\nAnd, in the corner of your eye, you could've sworn you saw the smallest glimpse of a smile on Rory's lips too.")
                    allyScore += 20
                    display_and_wait(f"\nYour relationship with your ally has improved!"
                                     f"\nYour current relationship score with Rory is {allyScore}")


            #You choose to talk about something casual
            elif (decision==2):
                display_and_wait("\nWith a topic in mind, you muster the courage to start the conversation")
                display_and_wait("\n\tYou: So, the weather...It's really nice out today")
                display_and_wait("\nAs if to taunt you, a thunder booms and gray clouds begin to veil the sky.")
                display_and_wait("\n\tRory: A very nice day")
                display_and_wait("\n\tYou pick up on the sarcasm and can't help but roll your eyes.")
                display_and_wait("\n\tYou: I'm just trying to make conversation. I know we agreed to be teammates and all already,"
                                 "\n\t and it might be strictly business to you, but I want to get to know the person who'll"
                                 "\n\t I'll go to hell and back with.")
                display_and_wait("\n\tYou: So, just tell me something about yourself. Anything.")
                display_and_wait("\nRory pauses, as if deep in thought.")
                display_and_wait("\n\tRory: Before coming here, I wanted to become a baker.")
                display_and_wait("\nYou did not expect Rory out of all people to enjoy baking.")
                display_and_wait("\n\tYou: Did you get to bake often before?")
                display_and_wait("\nRory shakes his head.")
                display_and_wait("\n\tRory: I have never baked before")
                display_and_wait("\n\tYou: Then, what made you want to become a baker?")
                display_and_wait("\n\tRory: I want to eat bread.")
                display_and_wait("\nIt sounds so ridiculous that you are too stunned to speak.")
                display_and_wait("\n\tRory: I have only gotten to eat it once."
                                 "\n\tI figured as a baker I would get to eat it again.")
                display_and_wait("\nHearing his explanation, you nod in understanding.")
                display_and_wait("\nBread was rare. Despite the number of factories that manufactured it in the Districts,"
                                 "\nwhen it comes to actually enjoying it, that was a luxury left for those in the Capitol.")
                display_and_wait("\n\tRory: What did you want to do before coming here?")
                display_and_wait("\nThe question from Rory catches you off-guard for a second.")
                display_and_wait("\n\tYou: To be honest, I'm not sure what I wanted but I'm sure it wasn't this."
                                 "\n\tI never thought I would ever be here, forced to take the lives of others to save my own.")
                display_and_wait("\nYou take a deep breath in, trying to collect yourself.")
                display_and_wait("\n\tYou: Even if I manage to walk away from all of this.")
                display_and_wait("\n\tYou: I'll still be a murderer.")
                display_and_wait("\n\tRory: You're just trying to survive.")
                display_and_wait("\nYou look up at Rory and meet his eyes.")
                display_and_wait("\n\tYou: Yeah, we're just trying to survive.")
                allyScore += 20
                display_and_wait(f"\nYour relationship with your ally has improved!"
                                 f"\nYour current relationship score with Rory is {allyScore}")


        #if your ally is Serena the following is the conversation you can have
        else:
            display_and_wait("\nYou trail behind Serena, who treks ahead.")
            display_and_wait("\nShe's clearing the pathway, ripping out the tree branches that hinder her way.")
            display_and_wait("\nFor some reason, she insisted using her bare hands, "
                             "\ntelling you to hold onto the sword of the brown-haired man." )
            display_and_wait("\nNot much dialogue has been exchanged between you two.")
            display_and_wait("\nYou have considered initiating conversation multiple times, but something about the way"
                             "\nSerena yanks and destroys anything obstructing her path has made you reluctant.")
            display_and_wait("\nBut, as the sun continues to dip lower and lower below the horizon, and the silence between you two continue"
                             "\nto drag out, you decide it's now or never")

            #if user hesitated and wasn't the one to kill the man
            if(userSanity==100):
                display_and_wait("\n\tYou: Sorry about freezing up back there")
                display_and_wait("\nSerena pauses in her steps for a second.")
                display_and_wait("\n\tSerena: It's fine. It's happens to everyone on their first time.")
                display_and_wait("\nYou read between the lines and realize that that was not Serena's first time.")
            # if user was the one to kill the brown-haired man
            else:
                display_and_wait("\n\tYou: What happened back there earlier...")
                display_and_wait("\nYour voice trails off as you were unsure of what to say next.")
                display_and_wait("\n\tSerena: When you strangled that guy?")
                display_and_wait("\n\tYou: Yeah.")
                display_and_wait("\nYour throats shuts, and you feel your chest cage into itself.")
                display_and_wait("\n\tYou: I didn't think I could kill him.")
                display_and_wait("\n\tSerena: Why not?")
                display_and_wait("\nIt's a loaded question, but when you look up at Serena, you find yourself lost for an answer.")
                display_and_wait("\nYou decide you want to change the topic")

            #after the slightly different intro, this will be the conversation between user and Serena
            display_and_wait("\n\tYou: You seem pretty experienced.")
            display_and_wait("\nSerena snickers.")
            display_and_wait("\n\tSerena: It would be weirder if I wasn't. I'm from District 1. I'm one of those Career tributes"
                                     "\nas the sponsors would call it.")
            display_and_wait("\nYou recall that Career tributes were those who were trained from birth to participate in the Hunger Games")
            display_and_wait("\nThat means saying that Serena is 'pretty experienced' is an understament. She must've seen more combat "
                                     "\nbattles than most people ever would in a lifetime." )
            display_and_wait("\n\tYou:Why did you choose me as a teammate?")
            display_and_wait("\nYou blurt the question without thinking.")
            display_and_wait("\nUnexpectedly, Serena turns around to face you. Her blonde hair sways with the wind"
                                     "\nand her blue eyes drill into you, as if in scrutiny")
            display_and_wait("\n\tSerena: You know there can only be one winner in this game, right?")
            display_and_wait("\nYou gulp, suddenly finding your throat dry")
            display_and_wait("\nSerena seems to catch onto your nervousness and chuckles.")
            display_and_wait("\n\tSerena: What do you think should happen if we're the last two standing?")
            print("Make your decision!\n1.Tell Serena you would fight to win\n2.Tell Serena you would sacrifice yourself")
            decision = int(input("Enter 1 or 2: "))
            #if user tells Serena they would fight Serena to win at the end
            if (decision == 1):
                    display_and_wait("\n\tYou: I would fight to stay alive.")
                    display_and_wait("\nSerena smiles at your answer. She takes a step closer, leaning closer as she asks")
                    display_and_wait("\n\tSerena: Could you kill me?")
                    display_and_wait("\n\tYou: I would")
                    display_and_wait("\nSerena holds your gaze. The sound of your heart palpitating rings in your ears.")
                    display_and_wait("\n\tSerena: But, the question is could you?")
                    display_and_wait("\nYou realize Serena isn't questioning your capability but rather your will.")
                    display_and_wait("\n\tYou: I could and I would.")
                    display_and_wait("\nSerena looks at you. Stares at you. A smile tugs at her lips.")
                    display_and_wait("\n\tSerena: Good. That's why I chose you as my teammate.")
                    allyScore += 20
                    display_and_wait(f"\nYour relationship with your ally has improved!"
                                             f"\nYour current relationship score with Serena is {allyScore}")
            #if user tells Serena they would sacrifice themselves for Serena to win:
            else:
                display_and_wait("\n\tYou: I don't think I would be able to kill you.")
                display_and_wait("\nSerena tilts her head to the side, looking at you challengingly.")
                display_and_wait("\n\tSerena: Why not?")
                display_and_wait("\nSerena asks casually, as if unable to understand what could possibly be the problem.")
                display_and_wait("\n\tYou: You're my teammate. I just wouldn't be able to betray you like that.")
                display_and_wait("\nSerena stares at you blankly. Her lips curve into a slight frown.")
                display_and_wait(f"\n\tSerena: {userName}, if you do not kill me, you will regret it.")
                display_and_wait("\nSerena turns around and continues forward.")
                display_and_wait("\nBaffled, you dazedly follow after her.")



#more action because you and your ally find a place to sleep but since you're on the edge of the border, they push you in with wildfires
#----------------------------------------------------------------------------------------------------------------------

    display_and_wait("\nThe sun has set, leaving the moon to hang brillantly in the night sky in its stead")
    display_and_wait(f"\nYou and {allyName} have found a cave to stay for the night.")
    display_and_wait("\nDespite it being in the dead of night, there's still a warmth that accompanies the passing breeze.")
    display_and_wait(f"\n{allyName} had insisted to be first on patrol, so you figured you better catch up on sleep.")
    display_and_wait(f"\nLaying down on your arm, you find yourself drifting off to sleep as the image of {allyName}'s face fades from your vision")
    display_and_wait("\nYou dream about your life before coming to the Hunger Games, reminiscing of the times you were with your family and loved ones.")
    display_and_wait("\nYou hear them calling out to you, chanting your name with smiles on their faces.")
    display_and_wait(f"\n'{userName}!'")
    display_and_wait(f"\n'{userName}!'")
    display_and_wait(f"\n'{userName}!'")
    display_and_wait(f"\n\t{allyName}: {userName}! Wake up!")
    display_and_wait(f"\nYou don't have time to ask what's hapenning as {allyName} pulls you up onto your feet and drags you out of the cave.")
    display_and_wait("\nYou realize you don't need to ask as the second you exited the cave,"
                     "\norange, yellow, and red encompasses your vision.")
    display_and_wait("\nThere's a wildfire!")
    display_and_wait("\n\tYou: Why is there a fire?!")
    display_and_wait(f"\n\t{allyName}: The forest bursted into flames out of no where!")

    #is userAgility is lower than 20 then they would die
    if(userAgility<20):
        display_and_wait("\nYou both run as fast as your feet could manage, jumping over stray logs that block the path, and sliding under fallen trees.")
        display_and_wait(f"\n{allyName} is much more agile than you and it seems they could keep running forever.")
        display_and_wait("\nMeanwhile, your legs are already beginning to shake from exhaustion and overuse.")
        display_and_wait("\nThe heat is immense. It wraps entirely around you, and you feel your consciousness slipping with the lack of oxygen.")
        display_and_wait(f"\nYour pace declines and the back of {allyName} grows smaller and smaller")
        display_and_wait(f"\n\t{allyName}: {userName}! Get up!")
        display_and_wait(f"\nThe flames devour your entire body and {allyName}'s torn expression is the last thing you see.")
        userHealth -=100
        checkHealth(userHealth)
    #if userAgility is 20 or higher, they will either carry their passed out teammate to safety or leave them to die
    else:
        display_and_wait("\nYou both run as fast as your feet could manage, jumping over stray logs that block the path, and sliding under fallen trees.")
        display_and_wait("\nYour high agility allows you to outrun the rapid wildfire.")
        display_and_wait(f"\nHowever, {allyName} was gradually falling behind!")
        display_and_wait("\nYou grab onto their hand and drag them along with you, unwilling to allow them to be consumed by the wrath of the fire. ")
        display_and_wait(f"\nEven despite this though, {allyName} is unable to run any longer.")
        display_and_wait(f"\nYou realize only now that {allyName}'s leg has a large burn wound across their left thigh.")
        display_and_wait(f"\n\t{allyName}: Just go! It's fine!.")
        print(f"Make your decision!\n1.Leave {allyName} behind and escape\n2.Risk it and save {allyName}")
        decision = int(input("Enter 1 or 2: "))

        #if user decides to leave their ally behind
        if(decision==1):
            display_and_wait(f"\nYou tear yourself away from {allyName}.")
            display_and_wait(f"\nEven though {allyName} insisted you leave, their expression twists in absolute disbelief.")
            display_and_wait("\nYou don't let that stop you though, turning around and dashing away from their fallen body.")
            display_and_wait("\nYou run and run, not even bothering to give a second glance when their screams of agony rips through the night")
            display_and_wait(f"\n\t{allyName}: {userName}! Come back! Save me!")
            display_and_wait("\nYou clasp your hands over your ears and continue running.")
            display_and_wait("\nWhen you've gained quite amount of distance, you stop, panting for air.")
            display_and_wait(f"\nYou left {allyName} to die.")
            display_and_wait(f"\n{allyName} was pleading for help.")
            display_and_wait(f"\n{userName}, you killed them.")
            display_and_wait("\nYour stats have changed!")
            userAgility += 10
            userSanity -= 60
            print_stats(userHealth,userSanity,userIntel,userStrength,userAgility)
            #user no longer has an ally in this route
            haveAlly = 0
        #if user decides to save their ally
        else:
            display_and_wait(f"\nYou refuse to leave without {allyName}.")
            display_and_wait("\nSo, despite their vigorous protests, you lift them onto your back and begin running.")
            display_and_wait(f"\n\t{allyName}: Put me down! You'll die!")
            display_and_wait("\nYou do not listen, concentrating all your energy in escaping the looming fire.")
            userAgility += 20
            userStrength += 20
            display_and_wait("\nYour stats have changed!")
            print_stats(userHealth,userSanity,userIntel,userStrength,userAgility)


#---------------------------------------------------------------------------------------------------------------------
#consequences of how user behaved during wildfire arc: by yourself= win but is insane, with a team = happy and will continue

    #THIS IS ENDING #1
    #if user left their teammate to die, they will go insane but win the game
    if(haveAlly == 0):
        display_and_wait(f"\nThat night, you did not rest as the image of {allyName} haunts your dreams.")
        display_and_wait("\nEvery time you close your eyes you see their melting body crawling towards you, "
                             "\nbegging for your help, pleading for your mercy.")
        display_and_wait("\nAnd, every time, you run away. You run away with your tail tucked between your legs.")
        display_and_wait("\nYou run away with their blood on your hands.")
        display_and_wait("\nThe next morning, you trek forward, moving on with your life.")
        display_and_wait("\nYou begin to reason with yourself.")
        display_and_wait("\nYou begin to play the game as it was intended.")
        display_and_wait("\nWhen you stumble upon a man being attacked by a group of gigantic snakes, you do not intervene.")
        display_and_wait("\nYou only come at the end to reap the benefits of the man's death by stealing his materials.")
        display_and_wait("\nYou realize it's easier this way.")
        display_and_wait("\nWhen you care about no one but yourself, it's easier.")
        display_and_wait(f"\nThat night, you dream of {allyName}.")
        display_and_wait(f"\nThe next night, you dream of {allyName}")
        display_and_wait("\nIt's become part of your routine. You watch those around you suffer by the hands of the game during the day, "
                             f"\nand you watch {allyName} suffer by the hands of your own during the night.")
        display_and_wait("\nWhen the finale comes, you expect to feel something.")
        display_and_wait("\nPerhaps excitement about the possibility of going home.")
        display_and_wait("\nPerhaps dread over the upcoming battle you must participate in.")
        display_and_wait("\nYet, there's nothing.")
        display_and_wait("\nAs you pace towards the center of the arena-")
        display_and_wait("\nAs you fight to the death with someone who too was forced to be here-")
        display_and_wait("\nAnd, even as you stand victorious with their blood splattered across your face-")
        userSanity = 0
        display_and_wait(f"\n\tAnnouncer: Congratulations, {userName}. You are the winner of the 74th Annual Hunger Game!")
        display_and_wait("\nStanding in a puddle of blood, you raise one hand up in the air.")
        display_and_wait("\nYou've won the game.")
        display_and_wait("\nThis is what you wanted.")
        display_and_wait(f"\nSo, why aren't you happy, {userName}?")
        display_and_wait("\nYour stats have changed!")
        print_stats(userHealth,userSanity,userIntel,userStrength,userAgility)
        sys.exit()

    #if user saved their ally, this conversation will happen
    if (haveAlly == 1):
        display_and_wait(f"\nYou carry {allyName} away from the fire until your legs finally give out.")
        display_and_wait(f"\nAs you collapse to the ground, {allyName} falls with you.")
        display_and_wait(f"\nThe both of you lie there in silence for a while.")
        display_and_wait("\n\tYou: Are you okay?")
        display_and_wait("\nYour throat is coarse and it's heard in the way your voice cracks.")
        display_and_wait(f"\n\t{allyName}: You're an idiot.")
        display_and_wait("\nPanting for air like your life depends on it, you don't bother defending yourself.")
        display_and_wait(f"\n\t{allyName}: I told you to leave.")
        display_and_wait("\n\tYou: Yeah, you did.")
        display_and_wait(f"\n\t{allyName}: You didn't listen.")
        display_and_wait("\n\tYou: Yeah, I didn't.")
        display_and_wait("\nA silence falls onto the two of you.")
        display_and_wait(f"\n\t{allyName}: Thank you.")
        display_and_wait("\nBreathless still, you close your eyes.")
        display_and_wait("\n\tYou: Yeah.")
        allyScore += 50
        display_and_wait(f"\nYour relationship with your ally has improved!"
                         f"\nYour current relationship score with {allyName} is {allyScore}")


    #This is the last arc! This is the finale where there will be 2 other endings (3 in total)

        display_and_wait("\nWhen you wake up the next morning, the first thing you notice is the smell of cooked stew.")
        display_and_wait("\nThe second thing you notice is you're in yet another cave.")
        display_and_wait("\nAnd, the third thing you notice is the blanket you were using is actually a shirt"
                         f"\nbelonging to {allyName}.")
        display_and_wait("\nYou fold and place the shirt aside.")
        display_and_wait(f"\nAt that moment, {allyName} walks into the cave, a makeshift bowl made out of wood in their hand.")
        display_and_wait("\n\tYou: Did you make a fire?")
        display_and_wait("\nMaking a fire was the same as announcing your presence to everyone nearby with the trail of smoke that it creates.")
        display_and_wait(f"\n{allyName} catches your concern immediately and explains.")
        display_and_wait(f"\n\t{allyName}: Today is the finale. There's only one other person. Unless they want to start the finale early, they"
                         f"won't approach us.")
        display_and_wait("\n\tYou: It's already the finale?")
        display_and_wait("\nYou can't help but grow worried. There can only one winner in this game after all.")
        display_and_wait(f"\n\t{allyName}: Eat.")
        display_and_wait(f"\n{allyName} offers you the bowl of stew. You notice there isn't another bowl.")
        display_and_wait(f"\n\tYou: What about you?")
        display_and_wait(f"\n\t{allyName}: I'll eat later.")
        display_and_wait(f"\nYou can tell by the lack of smoke in the air that the fire has been put out. {allyName} only made one bowl.")
        display_and_wait("\n\tYou: You should have it.")
        display_and_wait(f"\n\t{allyName}: Just eat it. That very well might be your last time eating a warm cooked meal.")
        display_and_wait("\nYou look down at the bowl of stew. You begin to eat.")
        display_and_wait("\nAfter you take your last bite of the stew, as if on cue, a loud horn sounds.")
        display_and_wait("\nAn energetic voice follows the deafening horn.")
        display_and_wait("\n\tAnnouncer: Tributes, please make your way to the center of the arena! The finale showdown will soon begin!")

        #if ally is Rory, this is what the finale will look like
        #ENDING NUMBER 2
        if (len(allyName) ==4 ):
            display_and_wait(f"\nYou look over to {allyName}. He hands you the bow and arrows.")
            display_and_wait("\n\tYou: What will you fight with?")
            display_and_wait("\n\tRory: My fist. Let's go")
            display_and_wait("\nThe two of you begin your journey back to the center of the arena.")
            display_and_wait("\nAs if history is bound to repeat itself, a deafening silence befalls the two of you.")
            display_and_wait("\nYet, this time, it's Rory who breaks it.")
            display_and_wait("\n\tRory: Don't hesitate.")
            display_and_wait("\nYou're not sure what he means.")
            display_and_wait("\nWhen you two arrive at the center of the arena, what you're greeted with is a blonde woman sitting amongst a sea of corpses")
            display_and_wait("\nSeeing the horrific scene, you feel your stomach churn with anxiety.")
            display_and_wait("\nHowever, when you turn to look at Rory, there's nothing but hatred in his eyes.")
            display_and_wait("\n\tYou: Rory, do you know her?")
            display_and_wait("\nThe woman hears your voice and turns to face the two of you.")
            display_and_wait("\nRecognition slowly fills her dazed eyes.")
            display_and_wait("\n\tRory: Her name is Serena, and she's my sister.")
            display_and_wait("\nSerena smiles. Despite her beautiful face, the streak of blood across her cheek overshadows her beauty.")
            display_and_wait("\n\tSerena: Are you finally here to kill me?")
            display_and_wait("\n\tSerena: You've made me wait for so long.")
            display_and_wait("\n\tRory: Give me that")
            display_and_wait("\nRory points to the bow and arrow. Reluctantly, you oblige.")
            display_and_wait("\n\tYou: Will you be okay? She's still your sister.")
            display_and_wait("\n\tRory: She's not my sister. She's a monster.")
            display_and_wait("\n\tRory: She volunteered to be a tribute.")
            display_and_wait("\n\tYou: What?")
            display_and_wait("\n\tRory: I did too.")
            display_and_wait("\n\tRory: I came here to kill her. So, don't get in my way")
            display_and_wait("\nRory leaves with that said, and you are left behind, utterly speechless.")
            display_and_wait("\nThe two quickly jump into battle, not bothering to exchange any furhter dialogue.")
            display_and_wait("\nWatching the fight from the side, you can't even begin to grasp an understanding of the situation.")
            display_and_wait("\nDespite the numerous swords scattered across the pavement, Serena decides to fight without weapon.")
            display_and_wait("\nShe only evades and dodges Rory's attacks, never going in to attack herself.")
            display_and_wait("\nIt's as if Serena doesn't even want to win.")
            display_and_wait("\n\tRory: Stop running away!")
            display_and_wait("\nSerena laughs.")
            display_and_wait("\nShe runs over to where you are standing and ducks behind you.")
            display_and_wait("\n\tSerena: I'm not running anymore. So, why don't you shoot?")
            display_and_wait("\nSerena's hand holds the back of your neck, as if threatning to snap it if you dare to move an inch.")
            display_and_wait("\n\tYet, you take the risk. As she's focused on getting a reaction from Rory, "
                             "\nyou turn around and kick her as hard as you can in the stomach.")
            display_and_wait("\n\tRory wastes no time. Seeing an opening, he draws his bow and shoots, piercing Serena directly in the heart.")
            display_and_wait("\nSpontaneously, Serena begins to hysterically laugh.")
            display_and_wait("\nShe doesn't stop laughing until blood entirely pools her mouth and chokes her.")
            display_and_wait("\nWatching the sight, you can't help but sympathize for her.")
            display_and_wait("\n\tRory: I've finished what I came here for.")
            display_and_wait("\nHe walks over to you and hands you the bow and the last remaining arrow.")
            display_and_wait("\nHe then walks over to his bleeding sister and lays down next to her, soaking in the pool of her blood.")
            display_and_wait(f"\n\tRory: Don't hesitate, {userName}")
            display_and_wait("\nYou finally realize what Rory had meant earlier.")
            display_and_wait("\n\tYou: Rory-")
            display_and_wait("\nYou want to protest. You want to reason with him.")
            display_and_wait("\nYet, Rory does not budge.")
            display_and_wait("\n\tRory: Do it. I deserve this as much as she does.")
            display_and_wait("\nYou draw your bow.")
            display_and_wait("\nYour arms are shaking.")
            display_and_wait("\nYour vision is blurry.")
            display_and_wait("\nIt must be raining.")
            if (allyScore > 60):
                display_and_wait(f"\n\tRory: Thank you, {userName}")
                display_and_wait("\n\tRory: I would've loved to share a bakery with you.")
                display_and_wait(" ")
                display_and_wait(" ")
                display_and_wait(" ")

            display_and_wait(f"\n\tAnnouncer: Congratulations, {userName}! You have won the 74th Annual Hunger Game!")
            sys.exit()









        #ENDING NUMBER 3
        #if ally is Serena, this is what the finale will look like
        else:
            display_and_wait(f"\nYou look over to {allyName}. She hands you the sword.")
            display_and_wait("\nYou are about to question what she will fight with, but she places a finger over your lips, hushing you.")
            display_and_wait("\n\tSerena: Don't worry, princess, I'll be fine even without a weapon.")
            display_and_wait("\nYou try to not get caught up on the pet name.")
            display_and_wait("\n\tYou: How can you be so sure?")
            display_and_wait("\nSerena laughs. Don't worry about it")
            display_and_wait("\nThe two of you begin your journey back to the center of the arena.")
            display_and_wait("\nAs if history is bound to repeat itself, a deafening silence befalls the two of you.")
            display_and_wait("\nYet, this time, it's Serena who breaks it.")
            display_and_wait(f"\n\tSerena: Do you have someone waiting for you when you get home, {userName}?")
            display_and_wait("\n\tYou: Of course. My entire family is back home. What about you?")
            display_and_wait("\n\tSerena: Nope. That's why people said it would be so easy for me to go."
                             "\nSince I didn't have a reason to come back")
            display_and_wait("\nYou remain silent, unsure of what to say to comfort her.")
            display_and_wait("\n\tSerena: I think I have a reason now.")
            display_and_wait("\n\tYou: A reason for you to return home?")
            display_and_wait("\n\tSerena: No. Just a reason.")
            display_and_wait("\nYou're not sure what she means.")
            display_and_wait("\nYet, when the robotic countdown sounds and the horn blares for the last time")
            display_and_wait("\nThe puzzle begins to piece itself together.")
            display_and_wait("\nWhen you two arrive at the center, the last man standing is already there, waiting.")
            display_and_wait("\nThe last tribute reveals himself, and the shock that overcomes his face is hard to not notice.")
            display_and_wait("\n\tYou: Do you know that man, Serena?")
            display_and_wait("\nSerena shrugs, a sly smile on her lips.")
            display_and_wait("\nThe man regains his composure after a moment and introduces himself as Rory, a Career tribute from District 1.")
            display_and_wait("\nHearing where he's from, you whip your head to Serena.")
            display_and_wait("\n\tYou: Serena, you know him, don't you?")
            display_and_wait("\n\tSerena: I've seen him once or twice in passing before probably.")
            display_and_wait("\nRory unsheathes his sword, his glare not straying from Serena's face")
            display_and_wait("\n\tSerena: Oh wait, I just remembered. He's my brother.")
            display_and_wait("\n\tYou: Are you-")
            display_and_wait("\n\tSerena: Am I capable of killing my own brother?")
            display_and_wait("\n\tSerena: Of course I am, that was one of the 101 basic classes.")
            display_and_wait("\nRory has not stopped glaring at Serena. Whatever bad blood they have between them,"
                             "\nyou have a feeling you should let them resolve it between themsleves.")
            display_and_wait(("\n\tSerena: But, even if I didn't take those classes, I would still have no problem killing him."))
            display_and_wait("\n\tSerena: May I have that?")
            display_and_wait("\nSerena points to the sword you're holding. Reluctantly, you give it to her.")
            display_and_wait("\n\tYou: Are you sure about this? I can fight him. He's still your brother after all.")
            display_and_wait("\nSerena takes the sword and grabs onto your hand. She kisses the back of it while looking up at you.")
            display_and_wait("\n\tSerena: Don't worry. I'll make sure you see your family. After all, I got to see mine already.")
            display_and_wait("\nYou watch as Serena treads towards Rory, her brother.")
            display_and_wait("\nThey exchange a few words that are too low for you to pick up on.")
            display_and_wait("\nA second later, they're clashing blades.")
            display_and_wait("\nYou feel as if you should do something to help in the fight, but it seems you do not need to as Serena easily gets the upper hand.")
            display_and_wait("\nSerena finds an opening and knocks down Rory, disarming him in the process.")
            display_and_wait("\n\tSerena: It's really a shame. You had your whole life ahead of you, yet you decided to follow me here.")
            display_and_wait("\n\tSerena: I took you to be smarter than that, Rory. Was your drive to kill me stonger than your intuition?")
            display_and_wait("\nSerena points the blade directly to Rory's neck, only allowing a centimeter of space for him to breathe.")
            display_and_wait("\n\tRory: Shut up and just kill me!")
            display_and_wait("\nSerena chuckles. She draws the blade even closer to Rory's neck.")
            display_and_wait("\n\tSerena: I will do the honors, but before that, I have to ask. Why do you hate me so much?"
                             "\nI've just grown to accept it over time, but I could never understand it. Are you jealous of me or something?")
            display_and_wait("\n\tRory: Shut up!")
            display_and_wait("\nSerena laughs. Her blue eyes are sharp and cold as she looks down at her brother.")
            display_and_wait("\n\tSerena: Well, it seems I've found my answer. Good night, my brother.")
            display_and_wait("\nWith one swift swing, Serena sends Rory's head rolling across the pavement.")
            display_and_wait("\nIt's a terrifying sight, and despite everything, you can't help but retreat when Serena walks over.")
            display_and_wait("\nShe senses your fear and stops in her tracks. With blood plastered across "
                             "\nher face, her clothes, and her beautiful golden hair, she resembles a bloody omen.")
            display_and_wait("\nSerena huffs out a sigh and looks up at the simulated sky.")
            display_and_wait(f"\n\tSerena: {userName}, why did we have to meet here?")
            display_and_wait("\n\tSerena: If things were different, we could've been-")
            display_and_wait("\nSerena stops herself.")
            display_and_wait("\n\tSerena: Well, it's too late to be thinking of hypotheticals now.")
            display_and_wait("\n\tSerena: Thank you. For everything.")
            if (allyScore > 60):
                display_and_wait("\nYou realize Serena's intentions and you rush towards her, shouting for her to stop.")
                display_and_wait(f"\n\tSerena: Most importantly though, thank you for being my reason, {userName}.")
                display_and_wait(" ")
                display_and_wait(" ")
                display_and_wait(" ")
                display_and_wait(f"\n\tAnnouncer: Congratulations, {userName}! You are the winner of the 74th Annual Hunger Game!")
            sys.exit()
