students = {
    "s1":{"name":"Abdul","surname":"Raeen","address":"Neemuch"},
    "s2":{"name":"Avesh","surname":"Mansuri","address":"Rajiv Nagar"},
    "s3":{"name":"Amir","surname":"Khan","address":"Pune"},
    "s4":{"name":"Rehan","surname":"Pathan","address":"Indore"},
}


for student in students:
    

    print(f'Hello {students[student]["name"]} {students[student]['surname']} From {students[student]['address']}')