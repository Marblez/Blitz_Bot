from pynput.mouse import Button, Controller;
import time;

mouse = Controller();
xMap = {"0":400,"1":480,"2":560,"3":640};
yMap = {"0":390,"1":480,"2":540,"3":630};

for i in range(0,4):
    for j in range(0,4):
        mouse.position = (xMap[str(i)],yMap[str(j)]);
        mouse.press(Button.left);
        time.sleep(0.5);
mouse.release(Button.left);
