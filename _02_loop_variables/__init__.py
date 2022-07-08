from tkinter import simpledialog, Tk

n = 100

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    for i in range(98, 0, -1):
        print(i+1 , 'bottles on the wall take one down pass it around ',i ,"bottles on the wall")
    print