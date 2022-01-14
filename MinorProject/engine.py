# ref: https://docs.python.org/3/library/sqlite3.html

import sqlite3

from print_table import print_table


# decl global vars
connection = None
database   = None

# connect to DB store (create if not exists)
def init():
    # set scope
    global connection
    global database

    # connect to db
    connection = sqlite3.connect("database.db")    # connect
    database = connection.cursor()                 # use this handle to SQL exec
    
    # create schema
    database.execute('''CREATE TABLE IF NOT EXISTS records
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, address TEXT, ph_num TEXT)''')

    # make schema persistent
    connection.commit()

    return




def list_all_records():
    # set scope
    global connection
    global database

    database.execute('''SELECT * FROM records''')
    sql_data = database.fetchall()  # fetch records

    # print formatted table
    print_table(sql_data)

    return




def search_by_id(id):
    # set scope
    global connection
    global database

    database.execute('''SELECT * FROM records
                        WHERE id = %i''' % id)  # select id
    sql_data = database.fetchall()              # fetch records

    # print formatted table
    print_table(sql_data)

    return


def search_by_name(name):
    # set scope
    global connection
    global database

    database.execute('''SELECT * FROM records
                        WHERE name LIKE \'%s\'''' % ('%'+name+'%'))  # select name
    sql_data = database.fetchall()                                   # fetch records

    # print formatted table
    print_table(sql_data)

    return

def search_by_address(address):
    # set scope
    global connection
    global database

    database.execute('''SELECT * FROM records
                        WHERE address LIKE \'%s\'''' % ('%'+address+'%'))  # select address
    sql_data = database.fetchall()                                         # fetch records

    # print formatted table
    print_table(sql_data)

    return


def search_by_number(ph_num):
    # set scope
    global connection
    global database

    database.execute('''SELECT * FROM records
                        WHERE ph_num LIKE \'%s\'''' % ('%'+ph_num+'%'))  # select ph_num
    sql_data = database.fetchall()                                       # fetch records

    # print formatted table
    print_table(sql_data)

    return




def add_new_record(name, address, ph_num):
    # set scope
    global connection
    global database

    database.execute('''INSERT INTO records (name, address, ph_num)
                        VALUES (\'%s\', \'%s\', \'%s\')''' % (name, address, ph_num))  # insert data
    connection.commit()                                                                # save

    return




def delete_record_by_id(id):
    # set scope
    global connection
    global database

    database.execute('''DELETE FROM records
                        WHERE id = %i''' % id) # select and delete by id
    connection.commit()                        # save

    return


def delete_record_by_name(name):
    # set scope
    global connection
    global database

    database.execute('''DELETE FROM records
                        WHERE name LIKE \'%s\'''' % ('%'+name+'%'))  # select and delete by name
    connection.commit() # save

    return

def delete_record_by_address(address):
    # set scope
    global connection
    global database

    database.execute('''DELETE FROM records
                        WHERE address LIKE \'%s\'''' % ('%'+address+'%'))  # select and delete by address
    connection.commit()                                                    # save

    return


def delete_record_by_number(ph_num):
    # set scope
    global connection
    global database

    database.execute('''DELETE FROM records
                        WHERE ph_num LIKE \'%s\'''' % ('%'+ph_num+'%'))  # select and delete by ph_num
    connection.commit()                                                  # save

    return




def edit_record_by_id(id, name, address, ph_num):
    if str.strip(name) != "":
        database.execute('''UPDATE records
                            SET name = \'%s\'
                            WHERE id = %i''' % (name, id))        # update name (leave the field blank to skip updating that field)

    if str.strip(address) != "":
        database.execute('''UPDATE records
                            SET address = \'%s\'
                            WHERE id = %i''' % (address, id))     # update address (leave the field blank to skip updating that field)

    if str.strip(ph_num) != "":
        database.execute('''UPDATE records
                            SET ph_num = \'%s\'
                            WHERE id = %i''' % (ph_num, id))      # update ph_num (leave the field blank to skip updating that field)

    connection.commit()                                           # save
    return




def exit_prog():
    connection.commit() # save
    connection.close()  # disconnect from db

    quit()  # exit prog

