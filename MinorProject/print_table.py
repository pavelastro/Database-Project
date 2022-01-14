def print_table(sql_data):
    for row in sql_data:
        print('\n', end='')

        print("Sl.:     ", row[0])
        print("Name:    ", row[1])
        print("Address: ", row[2])
        print("Contact: ", row[3])

        print('\n', end='')
