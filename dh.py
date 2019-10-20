#!/usr/bin/python

import sys

def main():
	g = int(raw_input("Enter public key, g: "))
	p = int(raw_input("Enter public key, p: "))

	a = int(raw_input("Enter Alice's private key, a: "))

        b = int(raw_input("Enter Bob's private key, b: "))

        x = (g ** a) % p

        print "x to send to Bob is: ", x

        y = (g ** b) % p

        print "y to send to Alice is: ", y

        n1 = (y ** a) % p

        n2 = (x ** b) % p

        if n1 == n2:
        	print "shared secret is ", n1
        else:
		print "something went wrong"
		
if __name__ == "__main__":
	main()
