# -*- coding: utf-8 -*-
my_name = 'Caleb Saunders'
my_age = 28
my_height = 69 # inches
my_weight = 138 #lbs
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

sum_of_age_weight_height = my_age + my_height + my_weight



print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % (my_teeth)


#this line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, sum_of_age_weight_height)
