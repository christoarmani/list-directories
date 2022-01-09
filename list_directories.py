"""
Created on Sun Apr 18 22:44:39 2021

@author: christoarmani
"""
import os

directory = r'add filepath here'
folders = os.listdir(directory)

with open("folders.txt", "w") as txt_file:
    for name in folders:
            txt_file.writelines(f'{name}\n')