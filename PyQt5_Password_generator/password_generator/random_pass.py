import random


def randCahr(chars):
	ranChar = random.choice(chars)

	return ranChar


def randomPass(chars, passLen):
	password = ""
	for i in range(passLen):
		char = randCahr(chars)
		password += char

	return password