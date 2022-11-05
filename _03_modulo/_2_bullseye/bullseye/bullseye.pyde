def setup():
    # Set the size of your sketch
    size(500,500)

    pass

def draw():
    # Starting with the largest ellipse, use a for loop to draw a bullseye with ellipses
     for i in range(10):
        if i % 2 == 0:
            fill(224,224,224)
        elif i % 2 == 1 :
            fill(224,23,23)
        ellipse(250, 250, 200 - i*20, 200 - i * 20)
    # Use an if statement and modulo to alternate the color of your rings


    pass
