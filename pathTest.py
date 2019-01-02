import sys;
import os;
import time;
from pynput.mouse import Button, Controller;
mouse = Controller();
xMap = {"0":400,"1":480,"2":560,"3":640};
yMap = {"0":390,"1":480,"2":540,"3":630};

letters = raw_input("Enter Letters: ");
letters = letters[:-1];
patharr = letters.split(";")

for coord in patharr:
    x = int(coord[1]);
    y = int(coord[0]);
    mouse.position = (xMap[str(x)],yMap[str(y)]);
    mouse.press(Button.left);
    time.sleep(0.01);
mouse.release(Button.left);
