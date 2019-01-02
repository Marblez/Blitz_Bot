import sys;
import os;
import time;
from pynput.mouse import Button, Controller;

print("Preprocessing");
map = {};
arr = [];
wordmap = {};
xMap = {"0":400,"1":480,"2":560,"3":640};
yMap = {"0":390,"1":480,"2":540,"3":630};

def populateMap(map,filename):
    file = open(filename, "r");
    arr = file.read().split('\n');
    for str in arr:
        map[str] = True;
    return;

def populateMatrix(letters,arr):
    if (len(letters) == 16):
        index = 0;
        for i in range(0,4):
            temparr = []
            for j in range(0,4):
                temparr.append(letters[index]);
                index = index + 1;
            arr.append(temparr);
    else:
        print("Length Error");

def beginSearch():
    for i in range(0,4):
        for j in range(0,4):
            wordSearch(arr,map, "","",i,j);
    return;
def wordSearch(arr,map,currword,currpath,currx,curry):
    if currx < 0 or curry < 0 or currx > 3 or curry > 3 or str(str(currx)+str(curry)) in currpath:
        return;
    currpath = currpath +str(currx) + str(curry) + ";";
    currword = currword + arr[currx][curry];
    if len(currword) <= 8:
        if len(currword) >=2 and currword in map and not currword in wordmap:
            clickword(currpath,currword);
        wordSearch(arr,map,currword,currpath,currx+1,curry+1);
        wordSearch(arr,map,currword,currpath,currx+1,curry-1);
        wordSearch(arr,map,currword,currpath,currx+1,curry);
        wordSearch(arr,map,currword,currpath,currx,curry+1);
        wordSearch(arr,map,currword,currpath,currx,curry-1);
        wordSearch(arr,map,currword,currpath,currx-1,curry+1);
        wordSearch(arr,map,currword,currpath,currx-1,curry);
        wordSearch(arr,map,currword,currpath,currx-1,curry-1);
    else:
        return;

def clickword(path,word):
    mouse = Controller();
    print(word + " "+ path);
    # print(path);
    wordmap[word] = True;
    path = path[:-1];
    patharr = path.split(";");

    for coord in patharr:
        x = int(coord[1]);
        y = int(coord[0]);
        mouse.position = (xMap[str(x)],yMap[str(y)]);
        mouse.press(Button.left);
        time.sleep(0.01);
    mouse.release(Button.left);
    return;

populateMap(map,"str1.txt");
populateMap(map,"str2.txt");
populateMap(map,"str3.txt");

print("Completed Preprocessing");

letters = raw_input("Enter Letters: ")
populateMatrix(letters,arr);
beginSearch();
