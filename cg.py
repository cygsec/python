#!/usr/bin/env python3
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
    return random.randint(1, 20)

def main():
# there is a max of 15 characters per line, including spaces
    compliment_num = generate_random_number()
    LCD1602.init()	# auto check and select i2c address; background light default is 1

    if compliment_num == 1:
        LCD1602.write(0, 0, 'Your smile lights')
        LCD1602.write(1, 1, 'up any room.')
    elif compliment_num == 2:
        LCD1602.write(0, 0, 'Your kindness is')
        LCD1602.write(1, 1, 'a beacon.')
    elif compliment_num == 3:
        LCD1602.write(0, 0, 'Your energy')
        LCD1602.write(1, 1, 'is uplifting.')
    elif compliment_num == 4:
        LCD1602.write(0, 0, 'Your creativity')
        LCD1602.write(1, 1, 'shines through.')
    elif compliment_num == 5:
        LCD1602.write(0, 0, 'Your compassion')
        LCD1602.write(1, 1, 'knows no limits.')
    elif compliment_num == 6:
        LCD1602.write(0, 0, 'The world is')
        LCD1602.write(1, 1, 'better with you.')
    elif compliment_num == 7:
        LCD1602.write(0, 0, 'Your generosity')
        LCD1602.write(1, 1, 'is a gift.')
    elif compliment_num == 8:
        LCD1602.write(0, 0, 'Your presence')
        LCD1602.write(1, 1, 'brings joy.')
    elif compliment_num == 9:
        LCD1602.write(0, 0, 'Your sincerity')
        LCD1602.write(1, 1, 'is beautiful.')
    elif compliment_num == 10:
        LCD1602.write(0, 0, 'You make others')
        LCD1602.write(1, 1, 'feel valued.')
    elif compliment_num == 11:
        LCD1602.write(0, 0, 'You make people')
        LCD1602.write(1, 1, 'feel heard.')
    elif compliment_num == 12:
        LCD1602.write(0, 0, 'Your outlook')
        LCD1602.write(1, 1, 'is inspiring.')
    elif compliment_num == 13:
        LCD1602.write(0, 0, 'Your kindness')
        LCD1602.write(1, 1, 'soothes hearts.')
    elif compliment_num == 14:
        LCD1602.write(0, 0, 'You radiate warmth')
        LCD1602.write(1, 1, 'and kindness.')
    elif compliment_num == 15:
        LCD1602.write(0, 0, 'You are')
        LCD1602.write(1, 1, 'genuine.')
    elif compliment_num == 16:
        LCD1602.write(0, 0, 'Your love makes')
        LCD1602.write(1, 1, 'life better.')
    elif compliment_num == 17:
        LCD1602.write(0, 0, 'Your effort')
        LCD1602.write(1, 1, 'is commendable.')
    elif compliment_num == 18:
        LCD1602.write(0, 0, 'You are a')
        LCD1602.write(1, 1, 'creative person')
    elif compliment_num == 19:
        LCD1602.write(0, 0, 'You have unbound')
        LCD1602.write(1, 1, 'potential.')
    elif compliment_num == 20:
        LCD1602.write(0, 0, 'You can do')
        LCD1602.write(1, 1, 'anything.')
    else:
        print("ERROR")

def destroy():
	LCD1602.clear()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        destroy()
