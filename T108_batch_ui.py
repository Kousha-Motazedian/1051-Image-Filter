"""ECOR 1051 MILESTONE 3 P8 Group:108
Submission Date: April 1st 2020
Designed By: Kousha Motazedian
             Mark Morgan
             Howard Wong
             Stephen Ogundayo"""

from Cimpl import load_image, choose_file, save_as, show, Image
from T108_user_interface import apply_filter

file_name = choose_file()
infile = open(file_name, "r")
command_list = []
for line in infile:
    command_list = line.split()
    image = load_image(command_list[0])
    saved_image = command_list[1]
    for x in range(2, len(command_list)):
        task = command_list[x]
        image = apply_filter(image, task)
    save_as(image, saved_image)
infile.close()
