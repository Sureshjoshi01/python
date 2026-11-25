# 
#    Create a Set: Create a set named fruits containing “apple”, “banana”, “mango”, and “orange”.
#    Add Element: Add “grape” to the fruits set.
#    Remove Element: Remove “banana” from the fruits set.
#    Discard Element: Try to discard “mango” from the fruits set.


fruits = { 'apple', 'banana', "mango", "orange" }
print("After creating the set:", fruits)
fruits.add('grape')
print("After adding 'grape':", fruits )
fruits.remove('banana')
print("After removing 'banana':", fruits)
fruits.discard('mango')
print("After discarding 'mango':", fruits)
