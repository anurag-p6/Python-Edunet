import math

abhishek_temp = int(input("Enter the temp abhishek:"))
sahil_temp = int(input("Enter the temp sahil:"))

if(abhishek_temp and sahil_temp):
     print(math.floor((abhishek_temp + sahil_temp)/2))
elif(abhishek_temp):
   print(abhishek_temp)
elif(sahil_temp):
   print(sahil_temp)
else:
  print("Lab is Empty")
