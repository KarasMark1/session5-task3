class Book:
 def __init__(self,title,author,isbn):
  self.title=title
  self.author=author
  self.__isbn=isbn
 def get_isbn(self):
  return self.__isbn
 def set_isbn(self,isbn):
  self.__isbn=isbn

class Member:
 def __init__(self,name,membership_id):
  self.name=name
  self.__membership_id=membership_id
 def get_membership_id(self):
  return self.__membership_id
 def set_membership_id(self,membership_id):
  self.__membership_id=membership_id

b=Book("book","karas","4444")
print(b.get_isbn())
b.set_isbn("8289")
print(b.get_isbn())

m=Member("mark","4526")
print(m.get_membership_id())
m.set_membership_id("9564")
print(m.get_membership_id())