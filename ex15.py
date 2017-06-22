from sys import argv

script, filename = argv

txt = open(filename)

print " "
print "Here's your file %r:" % filename
print " "
print "======"
print txt.read()
print "======"
print " "
print "Type the filename again:"
file_again = raw_input("-->> ")

print " "
txt_again = open(file_again)
print "======"
print txt_again.read()
print "======"

print " "