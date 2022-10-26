from unicodedata import name


class Person:
    
    
    def __init__(self,name,age,country):
        
        
        #Using exceptions
        if(country not in['Uganda','Kenya','Tanzania']):
            raise('Country not in EastAfrica')
        self.name=name
        self.age=age
        self.country=country
      
      #@ property is a decorater known as a getter 
    @property
    
    #Name is now a method
    def country(self):
        
        #self._name  is a private variable.(instance variable)
        return self._country
    
    #@country.setter is a setter.This setter will be added an if that will be able to override the Person1 at the end unlike before
    @country.setter
    def country(self,value):
        self._country=value
        if(value not in['Uganda','Kenya','Tanzania']):
            raise('Country not in EastAfrica')
         

        #Returning string
    def __str__(self):
        return f'Name is {self.name} and age is {self.age} and country is {self.country}'
    
person1= Person('joe don' ,16,'Tanzania')

#Update variables
person1.name = 'jimmy'
person1.age ='15'

#This part changes automatically does not follow the if statement.
person1.country='Uganda'

print(person1)
               