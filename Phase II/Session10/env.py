import numpy as np
from random import random, randint
import gym
from gym import error, spaces, utils , logger
from gym.utils import seeding
from test import TestApp 
import time
from PIL import Image as PILImage
from PIL import ImageDraw , ImageOps
import  numpy as np
import os
import math
import time
from kivy import Config
Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

class CarEnv(gym.Env):
    metadata = {'render.modes': ['human', 'rgb_array'], 'video.frames_per_second': 60}

    def __init__(self ):
        super(CarEnv, self).__init__()
        self.observation_space = gym.spaces.Box(low=0, high=255, shape=(40, 40, 1)) # 40 * 40 
        self.action_space = gym.spaces.Box(low = np.array([0,-5,0,0]), high = np.array([1,+5,0.5,0]), dtype=np.float32) # Accelerate , Rotate , Braking , no_op
        self.car = TestApp()
        self.car.run()
        # self.reward_range = gym.spaces.Box (low = np.inf
        
    def step(self,action):
        
        if action is not None:
            self.car.apply_action(action)
        
        car_x , car_y , angle, dest_bool = self.car.get_car_location()

        new_obs = self._get_state()

        Living_Penalty = -1
        
        if dest_bool :
            Destination_reward = 50

        if (car_x < 10) or (car_y < 10 ) or (car_x > 1420) or (car_y > 650 ):
            Wall_reward = - 10 

        reward = Living_Penalty + Destination_reward + Wall_reward 

        # Episodes ends when  
        # done =
        
        return new_obs , reward #, done, info 

    def reset(self):
        return self.get_screen(720,330,0)


    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def render(self,mode='human'):
        pass

    def close(self):
        self.car.on_stop() # still on check

    def _take_action(self):
        pass

    def _get_state(self):
        car_x , car_y , angle = self.car.get_car_location()
        return self.get_screen(car_x , car_y , angle)

    def get_screen(self,center_x,center_y,angle):

        #rotates point `A` about point `B` by `angle` radians clockwise.
        def rotated_about(ax, ay, bx, by, angle):
            radius = math.sqrt((by - ay)**2 + (bx - ax)**2)
            angle += math.atan2(ay-by, ax-bx)
            return (
                round(bx + radius * math.cos(angle)),
                round(by + radius * math.sin(angle))
            ) 

        car_center = (center_x , center_y)
        car_angle = angle
        car_length, car_width = 20 , 10

        rect_vertices = (
        (car_center[0] + car_width / 2, car_center[1] + car_length / 2),
        (car_center[0] + car_width / 2, car_center[1] - car_length / 2),
        (car_center[0] - car_width / 2, car_center[1] - car_length / 2),
        (car_center[0] - car_width / 2, car_center[1] + car_length / 2)
        )

        # square_vertices = [rotated_about(x,y, car_center[0], car_center[1], math.radians(0)) for x,y in square_vertices]
        rect_vertices = [rotated_about(x,y, car_center[0], car_center[1], math.radians(car_angle)) for x,y in rect_vertices]

        path=os.path.normpath("C:\\Users\\ani\\Desktop\\P2S10\\images\\MASK1.png")

        img = PILImage.open(path)
        draw = ImageDraw.Draw(img)

        # draw.polygon(square_vertices, fill=(255,0,0))
        draw.polygon(rect_vertices, fill=(0,255,0))
        (width, height) = (img.width // 3, img.height // 3)
        im_resized_image = img.resize((width , height))
        # Co-ordinate points for cropping (40 x 40)
        left ,top , right ,bottom = (car_center[0]//3)-20 , (car_center[1]//3)-20 , (car_center[0]//3)+20 , (car_center[1]//3)+20

        # i  = int(time.time()*1000)%100000 # To get unique value to save images
        im1 = im_resized_image.crop((left, top, right, bottom))
        im2 = ImageOps.grayscale(im1)  

        # Cropped image of 40 x 40  in array format .
        np_array_cutout = np.asarray(im2)
        return np_array_cutout
        
    

a =  CarEnv()
print(a.step([2,-1,0.5]))

