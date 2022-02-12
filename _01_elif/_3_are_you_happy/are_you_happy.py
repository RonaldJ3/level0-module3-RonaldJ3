from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    window = Tk()
    window.withdraw()

    h = simpledialog.askstring('AH', "Are you happy?")

    if h == 'yes' :
        messagebox.showinfo('AH', "Keep doing whatever your doing.")

    elif h == 'no' :
        H = simpledialog.askstring('AH', "Do you want to be happy?")

        if H == 'yes' :
            messagebox.showinfo('AH', "Change something.")

        elif H == 'no' :
            messagebox.showerror('AH', "Keep doing whatever your doing.")
    pass
