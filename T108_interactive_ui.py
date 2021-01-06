"""ECOR 1051 MILESTONE 3 P8 Group:108
Submission Date: April 1st 2020
Designed By: Kousha Motazedian
             Mark Morgan
             Howard Wong
             Stephen Ogundayo"""

from Cimpl import load_image, choose_file, save_as, show, Image
from T108_user_interface import apply_filter

run = True
image = None
while run == True:
    task = input("L)oad image\t S)ave-as\t 2)-tone\t 3)-tone\t\n"
                 "X)treme contrast\t T)int sepia\t P)osterize\t\n"
                 "E)dge detect\t I)mprove edge detect\t V)ertical flip\t\n"
                 "H)horizontal flip\t Q)uit : ")
    task = task.upper()
    if task == "L":
        image = load_image(choose_file())
    elif task == "S":
        save_as(image)
    elif task == "Q":
        run = False
    else:
        if image == None:
            print("No Image Loaded")
        else:
            image = apply_filter(image, task)
