it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['Instacart', 'Taboola', 'Samsara']) #if you don't add brackets it just does letters and scatters them
it_companies.remove('Oracle')
#if the item wanted to remove is not found it will raise errors but the discard method wont

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.union(B)
A.intersection(B) #7
A.issubset(B) #True
A.isdisjoint(B) #False
print(B.symmetric_difference(A)) #i don't know why this isn't working (i'll fix it later)
del A
del B

age = [22, 19, 24, 25, 26, 24, 25, 24, 26]
age_set = set(age)
age_list = list(age)
print(len(age_list)-len(age_set)) #the list
#strings are unmodifiable and are a string or just a word
#lists are ordered banks of characters, you can modify these
#tuples are ordered banks of characters just like lists but you cant change these
#sets are modifiable and can only keep one of each word or number, they are also not ordered
words = {'I am a teacher and I love to inspire and teach people'}