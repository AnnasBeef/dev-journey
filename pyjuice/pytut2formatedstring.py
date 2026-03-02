#using formated strings will be easer to visualize 
first = 'John'
last = 'Smith'
message = first + '[' +last + '] is a coder' 
#string Concatenation, you can easily visualise the output
#this is too complicated and hard to understand
#output: John[Smith] is a coder
print(message)


msg = f' {first} [{last}] is a coder' #formated string
print (msg)