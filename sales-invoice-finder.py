with open('sales_data.csv', 'r') as rfile:
    lines = rfile.read()
    lines = lines.split('\n')
    if '' in lines:
        lines.remove('')
selection = input('Search by invoice id (id) or customer last name (lname)? ')

while selection not in ['id', 'lname']:
    print("ERROR: You must enter either 'id' for invoice or 'lname' for customer search ")
    selection = input('Search by invoice id (id) or customer last name (lname)? ')

term = input("Enter your search term: ")
searchCount = 0
if selection == 'id':
    for line in lines:
        if line.split(',')[0] == term:
            searchCount += 1
            print(line)
    print("{} records found".format(searchCount))
else:
    for line in lines:
        if line.split(',')[2] == term:
            searchCount += 1
            print(line)
    print("{} records found".format(searchCount))