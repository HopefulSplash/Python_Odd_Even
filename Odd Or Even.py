# Check If A Number Is Odd Or Even
# if /2 is = 0 Even
# if /2 is not = 0 Odd

input = int(input("Please Enter a number: "))

if (input % 2) == 0:
   print("{0} is Even".format(input))
else:
   print("{0} is Odd".format(input))