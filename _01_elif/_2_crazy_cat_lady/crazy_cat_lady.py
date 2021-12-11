from tkinter import simpledialog, messagebox, Tk
import webbrowser


# Use this function to play a video from the internet
def play_video(url):
    webbrowser.open(url)

# =================== DO NOT MODIFY THE CODE ABOVE ===========================


def showsimpledialog(param):
    pass


if __name__ == '__main__':
    # TODO 1) Make a new window variable, window = Tk()
    window = Tk()
    #      2) Hide the window using the window's .withdraw() method
    window.withdraw()
    #      3) Ask the user how many cats they have
    r = simpledialog.askstring('CatN', "how many cats do you have?")
    #      4) If they have 3 or more cats, tell them they are a crazy cat lady
    if r == '3':
        showsimpledialog(''"You are a crazy cat lady.")
    #      5) If they have less than 3 cats AND more than 0 cats, call the
    elif r == '2' :
        play_video("https://www.youtube.com/watch?v=cbP2N1BQdYc")
    #         play_video function below to show them a cat video
    elif r == '1' :
        play_video("https://www.youtube.com/watch?v=cbP2N1BQdYc")
    #      6) If they have 0 cats, show them a video of A Frog Sitting on a
    #         Bench Like a Human

    pass
