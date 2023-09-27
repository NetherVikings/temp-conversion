

choice = input("Do you want Celcius or Fareinheit? (C/F?) ")

if choice == "F" :
   fareinheit = input("What is the tempurature in Celcius? ")
   answer = int(fareinheit) * 1.8 + 32
elif choice == "C":
   celcius = input("What is the tempurature in Fareinheit? ")
   answer = (int(celcius) - 32.0) * .555555
print ('%.1f' %answer)


