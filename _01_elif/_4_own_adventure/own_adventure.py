from tkinter import simpledialog, messagebox, Tk

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story



if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    a = simpledialog.askstring('first choice', "You wake up in a dark cave with two tunnels. The tunnel on the left seems to gently slope up. While the tunnel on the right has a steep slope upwards and a small bit of light is coming from the other end of it.  ")

    if a == 'left' :
        b = simpledialog.askstring('second choice', "You start to head done the left path. a little later you hear rocks falling back were you first came from. Will you go back and see what happened or countine down the ever so slightly brighter tunnel?")
        if b == 'c' :
            c = simpledialog.askstring('last choice', "after walking for a undetermined amount of time you start to feel tired and hungry. you think about sitting down and resting maybe even taking a nap. Will you rest or continue walking?")
        if b == 'go back' :
           e = simpledialog.askstring('final', "you start walking back and the ceiling suddenly shakes. Ignoring the noise and slightly moving ground you keep walking twoards the place you were orignlly at. you finally see your starting point and notice the right tunnel caved in. glad you didn't try climbiming up that path. You turn and start walking back down the left tunnel. not long after the celing suddenly collapse above your head.")
        if c == 'rest' :
            simpledialog.SimpleDialog('final', "you sit down and take a break. After who knows how long you wake up to see s bright light. Once your eyes adjust you see a group of 5 men standing over you with ropes and the like. You weakly ask What took you so long?")
        if c == 'c' :

            simpledialog.SimpleDialog('final', "you start to see some light. as the light gets closer you increase your speed. until you finaly get out of the cave you look around and notice a helicopter. you try to call for help but your voice fails and you collapse to the ground never to wake up again.")
    elif a == 'right' :
        d = simpledialog.askstring('second choice', "you slowly climb up the steep slope when you hear a faint rumble and look back to see the cave collapesing behind you start climbing as fast as you can. Sadly the rocks catch up with you and you are buried alive. will you try to dig your way out or stay still and wait for someone to save you?")
        if d == 'stay' :
            d == simpledialog.askstring('final', "you wait in place and slowly fall asleep. you wake up to a sudden noise and a bright light. Someone yells I found one and you see more and more light. until your eyes final adjust and your hosited out the rubble. you look around and ask were am I. A woman aproaches you and explains everything that happened to you.")
        if d == 'dig' :
            d == simpledialog('final',"you kept digging till your hands go numb and you finally saw some light. you call out for help a2and hear faint voices in the distance you keep calling help help. finally you see someone aproaching when all of a sudden more rocks start to fall. you scream HURRY! but the ppl seemed to have turned around and started to run. you despratly look at there backs until a rock falls crushing you The End.")