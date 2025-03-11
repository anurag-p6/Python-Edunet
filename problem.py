vip_person = {
  "membership": 50000,
  "card":"gold",
  "car":"luxiary"
}

normal_person = {
  "membership": 30000,
  "card":"silver",
  "car":"normal"
}

input_person = {
  "membership":int(input("Enter the membership amount:")),
  "card":input("Enter the card:"),
  "car":input("Enter your car:")
}

if(input_person["membership"] == vip_person["membership"] and input_person["card"] == vip_person["card"] and input_person["car"] == vip_person["car"]):
  print("You are VIP person go through VIP gate")
else:
  print("You are not VIP go through normal gate")