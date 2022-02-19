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
    elif b == 'back' :
        c = simpledialog.askstring('last choice', "after marching for a undetermined amount of time you start to feel tired and hungry. you think about sitting down and resting maybe even taking a nap. Will you rest or continue walking?")
    elif c == 'continue' :
                simpledialog.SimpleDialog('final', "you start to see some light. as the light gets closer you increase your speed. until you finaly get out of the cave you look around and notice a helicopter. you try to call for help but your voice fails and you collapse to the ground never to wake up again.")