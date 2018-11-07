import tkinter as tk
import math
import random

class Boid:
    def __init__(self, widget_id, x_vector, y_vector, speed):
        self.widget_id = widget_id
        self.x_vector = x_vector
        self.y_vector = y_vector
        self.speed = speed


class App(tk.Canvas):
    boids = []

    def move_boids(self):
        for boid in self.boids:
            # get coordinates for boid [x,y]
            boid_coord = self.coords(boid.widget_id)

            # reset x to zero when off the screen
            if boid_coord[0] > self.winfo_width():
                #boid_coord[0] = 0
                #self.coords(boid.widget_id, boid_coord)

            elif boid_coord[0] < 0:
                #boid_coord[0] = self.winfo_width()
                #self.coords(boid.widget_id, boid_coord)

            # reset y to zero when off screen
            if boid_coord[1] > self.winfo_height():
                boid_coord[1] = 0
                self.coords(boid.widget_id, boid_coord)
            elif boid_coord[1] < 0:
                boid_coord[1] = self.winfo_height()
                self.coords(boid.widget_id, boid_coord)

            self.move(boid.widget_id, boid.x_vector * boid.speed, boid.y_vector * boid.speed)
        self.after(10, self.move_boids)

    def __init__(self, master=None):
        tk.Canvas.__init__(self, master)
        self.grid()
        for i in range(10):
            x = random.randint(0, 200)
            y = random.randint(0, 200)
            degrees = random.uniform(0, 360)
            speed = random.uniform(0, 1)
            print(x, y, degrees, speed)

            self.boids.append(Boid(self.create_text(x, y, text="X", anchor=tk.NW), degrees, speed))




app = App()
app.after(1000, app.move_boids)
app.mainloop()
app.destroy() # optional; see description below