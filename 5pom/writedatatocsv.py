import csv

# dict has rows
myData = [
    {'userName': 'admin', 'password': 'admin', 'status': 1},
    {'userName': 'mahetha', 'password': 'mahetha', 'status': 0},
    {'userName': 'admin', 'password': 'mahetha', 'status': 0},
    {'userName': 'naresh', 'password': 'admin', 'status': 0},

]

# headers
fields = ['userName', 'password', 'status']

# create fileobj
f = open("login.csv", 'w', newline='')

# creating a csv writer object
csvwriter = csv.DictWriter(f, fieldnames=fields)

# writing headers (field names)
csvwriter.writeheader()

# writing data rows
csvwriter.writerows(myData)

f.close()