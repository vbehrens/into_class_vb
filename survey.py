print "Welcome to the survey!"
name = raw_input("What is your name? ")
name2 = raw_input("What is your name? ")
color = raw_input("What is yoru favorite color? ")
color2 = raw_input("What is yoru favorite color? ")
hobby = raw_input("What is your favorite hobby? ")
hobby2 = raw_input("What is your favorite hobby? ")
movie = raw_input("What is your favorite movie? ")
movie2 = raw_input("What is your favorite movie? ")
pet = int(raw_input("Do you have any pets? If yes, how many? "))
pet2 = int(raw_input("Do you have any pets? If yes, how many? "))
sport = raw_input("What is your favorite sport? ")
sport2 = raw_input("What is your favorite sport? ")

print "%s's favorite color is %s" % (name, color)
print "%s's favorite color is %s" % (name2, color2)
print "%s's favorite hobby is %s" % (name, hobby)
print "%s's favorite hobby is %s" % (name2, hobby2)
print "%s's favorite movie is %s" % (name, movie)
print "%s's favorite movie is %s" % (name2, movie2)
print "%s has %i pets." % (name, pet)
print "%s has %i pets." % (name2, pet2)
print "%s's favorte sport is %s" % (name, sport)
print "%s's favorte sport is %s" % (name2, sport2)