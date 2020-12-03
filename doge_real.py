class Dog:
  counter=100
  dog_breed_dict={"Labrador Retriever":5,"German Shepherd":12,"Beagle":10}
def __init__(self,breed_list,accessories_required):
  self.__dog_id_list=[]
  self.__breed_list=breed_list
  self.__price=0
  self.__accessories_required=accessories_required
def get_dog_id_list(self):
  return self.__dog_id_list
def get_breed_list(self):
  return self.__breed_list
def get_price(self):
  return self.__price
def get_accessories_required(self):
  return self.__accessories_required
def get_dog_price(self,breed):
  if breed=="Labrador Retriever":
    price=800
  elif breed=="German Shepherd":
    price=1230
  elif breed=="Beagle":
    price=650
  return price

def generate_dog_id(self,breed):
  Dog.counter+=1
  id=breed[0]+(str)(Dog.counter)
  return id

def validate_breed(self):
  if self.__breed_list in Dog.dog_breed_dict:
    return True
  else:
    return False
def validate_quantity(self):
  count=0
  for i in self.__breed_list:
    if Dog.dog_breed_dict[i]!=0:
      count+=1
  if count==len(self.__breed_list):
      return True
  else:
    return False
def calculate_total_price(self):
  if validate_breed():
    if validate_quantity():
      for i in self.__breed_list:
        Dog.dog_breed_dict[i]-1
        self.__dog_id_list=self.generate_dog_id()
        price=self.get_dog_price(i)
        if self.get_accessories_required():
          price=price+350
        if price>1500:
          self.__price=price-price*5/100
        else:
          self.__price=price

    else:
      return -2

  else:
    return  -1

d=Dog("Beagle",33)
d.calculate_total_price()
