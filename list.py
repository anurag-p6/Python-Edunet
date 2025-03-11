list1 = ["Aakash","Deepak","Mitesh","Buffalo","Sahil","Shirke","Sambhar","Bitkya"]

print(list1[3:5]);

print(list1[2::3])

for i in range(len(list1)):
    if list1[i] == "Buffalo":
        print(i)