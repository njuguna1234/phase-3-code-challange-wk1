def sorted_age(people):

    return sorted(people ,key=lambda person: person[1])

people=[("Alice",30),("Roy",10),("Wahome",28),("Charity",37)]

sorted_people=sorted_age(people)

print(sorted_people)