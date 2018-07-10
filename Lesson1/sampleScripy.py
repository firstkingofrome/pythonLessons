import math
import demoLibrary


#scope function
def sampleFunction(x,y,z):
    outOfScope = 10
    return (x+y+z)
    pass





def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have" + str(cheese_count) + "Cheeses!")
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"




#name space main
def main():
    cheese = input("how much cheese do you want: ")
    cracker = input("# crackers?: ")
    cheese_and_crackers(cheese, cracker)
    
    
    
main()
#scope global
