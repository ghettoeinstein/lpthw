x = "There are %d types of people." % 10

# assign a variable named binary to the string value of' binary'
binary = "binary"
# variable named do_not which contains the string "don't"
do_not = "don't"

# The y variable is storing the evaluation of a string with variable substitution"
y = "Those who know %s and those who %s." % (binary, do_not)


# Print the value of x
print x

# Print the value of y
print y



# Print what you said with string substituion
print "I said: %r." % x

# Print what you also said with string substituion"
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"


# Concatenate the hilarious variable in a print statement with the joke_evaluation variable

print joke_evaluation % hilarious

# Assign a string value to w
w = "This is the left side of..."
# Assign a string value to e
e = "a string with a right side."


# Print both w and e
print w + e
