#!/usr/bin/env python3
# requires <INPUT FILE REQUIREMENTS HERE>
# LCD1602 based rasberry pi compliment generator based on random input
import LCD1602
import time
import random

# def setup():
	# LCD1602.init(0x27, 1)	# init(slave address, background light)
	# LCD1602.init(0x3f, 1)	# the i2c address for some LCD1602 is 0x3f
#	LCD1602.write(0, 0, 'You Look')
#	LCD1602.write(1, 1, 'Nice!')
#	time.sleep(2)

def generate_random_number():
    return random.randint(1, 3)

def main():
    compliment_num = generate_random_number()
    LCD1602.init()	# auto check and select i2c address; background light default is 1

    if compliment_num == 1:
        LCD1602.write(0, 0, 'You Look Nice!')
    elif compliment_num == 2:
        LCD1602.write(0, 0, 'You Handsome Boi')
    elif compliment_num ==3:
        LCD1602.write(0, 0, 'You Stinky Butt')
    else:
        print("ERROR")

def destroy():
	LCD1602.clear()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        destroy()
