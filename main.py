import os
import string
import random
import time

# D -> difficulty
# M -> vital message
# N -> user version of vital message

os.system('cls || clear')

print('VITAL MESSAGE')

while True:

	D = int(input('HOW DIFFICULT? (4 - 10)\n'))

	if D >= 4 and D <= 10:
		break

M = ''

for i in range(D):
	M += random.choice(string.ascii_uppercase) # random letters

os.system('cls || clear')

print('SEND THIS MESSAGE: \n')
print(M)

time.sleep(0.5 * D) # metade da dificuldade escolhida em segundos para digitar

os.system('cls || clear')

N = input('')

if N != M:
	print(f'YOU GOT IT WRONG! YOU SHOULD HAVE SENT: {M}')
else:
	print('MESSAGE CORRECT! THE WAR IS OVER!')







