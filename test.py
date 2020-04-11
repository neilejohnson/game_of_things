# import csv
# from answers import get_number_answers
# from pathlib import Path
from time import sleep
import os
random_block = '░'

for x in range(1,71):
    os.system('cls')
    for y in range(3):
        print(random_block * (71-x))
        print(' ' * (71-x) + random_block * (x-1))
    sleep(.07)



# y=1

# while True:
#     os.system('cls')
#     print(  '\n' * 3 +
#             ' '*23 + random_block*13 + ' '*24 + '\n' +
#             ' '*22 + random_block +  ' '*13 + random_block + '\n' +
#             ' '*18 + random_block*4 +  ' '*3 + random_block + ' '*11 + random_block + '\n' +
#             ' '*17 + random_block +  ' '*14 + random_block + ' '*5 + random_block + '\n' +
#             ' '*17 + random_block +  ' '*20 + random_block)

#     if y%2==0:
#             print( 
#                 ' '*17 + random_block +  ' '*20 + random_block + '\n' +
#                 ' '*17 + random_block +  ' '*20 + random_block + '\n' +
#                 ' '*18 + random_block*4 +  ' '*7 + random_block + ' '*3 + random_block + ' '*4 + random_block + '\n' +
#                 ' '*22 + random_block +  ' '*6 + random_block + ' '*3 + random_block + ' '*4 + random_block + '\n' +
#                 ' '*22 + random_block +  ' '*7 + random_block*3 + ' '*5 + random_block)
#     else:
#         print( 
#             ' '*18 + random_block*4 +  ' '*16 + random_block + '\n' +
#             ' '*22 + random_block +  ' '*15 + random_block + '\n' +
#             ' '*19 + random_block*3 +  ' '*7 + random_block + ' '*3 + random_block + ' '*4 + random_block + '\n' +
#             ' '*18 + random_block +  ' '*10 + random_block + ' '*3 + random_block + ' '*4 + random_block + '\n' +
#             ' '*19 + random_block*3 +  ' '*8 + random_block*3 + ' '*5 + random_block)

#     print(
#             ' '*22 + random_block + ' '*15 + random_block + '\n' +
#             ' '*23 + random_block + ' '*13 + random_block + '\n' +
#             ' '*24 + random_block + ' '*4 + random_block*3 + ' '*4 + random_block + '\n' +
#             ' '*25 + random_block*4 + ' '*3 + random_block*4)
#     sleep(1)
#     y+=1
  