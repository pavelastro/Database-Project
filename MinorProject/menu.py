import engine


def show_menu():
    print("1.  List All Records")
    print('\n', end='')
    print("2.  Search A Record By Serial Number")
    print("3.  Search Records By Name")
    print("4.  Search Records By Number")
    print("5.  Search Records By Address")
    print('\n', end='')
    print("6.  Add A New Record")
    print('\n', end='')
    print("7.  Delete A Record By Serial Number")
    print("8.  Delete Records By Name")
    print("9.  Delete Records By Number")
    print("10. Delete Records By Address")
    print('\n', end='')
    print("11. Edit Record By Serial Number")
    print('\n', end='')
    print("12. Exit")
    print("> ")

    opt = input()

    #TODO: Input data
    match opt:
        case '1':
            engine.list_all_records()

        case '2':
            print("Enter ID : ")
            id=input()
            engine.search_by_id(int(id))

        case '3':
            print("Enter name")
            name=input()
            engine.search_by_name(name)

        case '4':
            print("enter number")
            number=input()
            engine.search_by_number(number)

        case '5':
            print("Enter address")
            address=input()
            engine.search_by_address(address)

        case '6':
            print("Name, Address and Number")
            name=input()
            address=input()
            number=input()
            engine.add_new_record(name, address, number)

        case '7':
            print("Enter ID")
            id=input()
            engine.delete_record_by_id(int(id))

        case '8':
            print("enter name")
            name=input()
            engine.delete_record_by_name(name)

        case '9':
            print("Enter number")
            number=input()
            engine.delete_record_by_number(number)

        case '10':
            print("Enter address")
            address=input()
            engine.delete_record_by_address(address)

        case '11':
            print("enter ID, Name,Address and Number")
            id=input()
            name=input()
            address=input()
            number=input()
            engine.edit_record_by_id(int(id),name,address,number)

        case '12':
            engine.exit_prog()

        case _:
            return


    return
