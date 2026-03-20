# --coding:utf-8--

from robot import *

while is_free_right() or is_free_down():
    
    if is_free_right():
        while is_free_right():
            move_right()
    
    if is_free_down():
        while is_free_down():
            move_down()
