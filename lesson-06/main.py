fruit = {"apple": {"kg":12, "price": 22}}

def check_fruit(elemnt):
  if elemnt in fruit:
    return True
  else:
    return False



def end_question():
  ques = input("Add More? yes/no: ")
  ques = ques.lower()
  if ques == "yes":
    return True
  else:
    return False

def main_question():
  helper = {}
  name = input("Enter fruit name: ")
  kg = input("Enter fruit weight: ")
  price = input("Enter fruit price: ")
  helper["kg"] = kg
  helper["price"] = price
  fruit[name] = helper

  return fruit

while True:
  if len(fruit) == 0:
    main_question()
  else:
    print("this is your cart", fruit)
    
    if end_question() == True:
      main_question()
    else:
      break

while True:
  print(fruit)

  inp = input("Would you delete fruit / no: ")
  
  if inp.lower() == "no":
    break
  elif check_fruit(inp) == False:
    print("can't find input element pleas try again")
    pass
  elif len(fruit) == 0:
    break
  else:
    fruit.pop(inp)

result = 0
for key,value in fruit.items():
  kg = int(value['kg'])
  price = int(value['price'])
  result += kg*price
  print(key, "your amount" , kg*price, "GEL")

print("you have to pay", result, "GEL")