class ITEM:
    def __init__(self, itm_id, nm, desc, prc):
        self.itm_id = itm_id
        self.nm = nm
        self.desc = desc
        self.prc = prc


class MANAGER:
    def __init__(self):
        self.item_list = []

    def add_itm(self):
        try:
            print('\n[[[[ ITEM ADDITION MODE ]]]]')
            itm_id = input("Enter Item ID: ")
            nm = input("Enter Name of Items: ")  
            desc = input("Enter Item Description: ")
            prc = int(input("Enter Item Price[Php]: "))

            if prc < 0:
                raise ValueError("INVALID PRICE!")
            else:
                prc=float(prc)
            new_itm = ITEM(itm_id, nm, desc, prc)
            self.item_list.append(new_itm)
            print("Item has been added successfully!")
        except Exception as e:
            print("Unexpected error:", e)

    def view(self):
        if not self.item_list:
            print("No items in the system")
        else:
            for itm in self.item_list:
                print("--------------------------")
                print("ID         : ", itm.itm_id)
                print("Name       : ", itm.nm)
                print("Description: ", itm.desc)
                print("Price      : ", itm.prc)
                print("--------------------------")

    def update(self):
        print('\n[[[[ ITEM UPDATE MODE ]]]]')
        itm_id = input("Enter Item ID: ")
        for itm in self.item_list:
            if itm.itm_id == itm_id:
                try:
                    print("--------------------------")
                    itm.nm = input("Enter new Name         : ")
                    itm.desc = input("Enter new Description  : ")
                    itm.prc = float(input("Enter new price        : "))
                    print("--------------------------")
                    if itm.prc < 0:
                        raise ValueError("INVALID PRICE!")

                    print("Item updated successfully!")
                except ValueError as ve:
                    print(f"Error: {ve}")
                return
        print("Item NOT FOUND in system")

    def delete(self):
        print('\n[[[[ ITEM DELETION MODE ]]]]')
        itm_id = input("Enter item ID: ")
        for itm in self.item_list:
            if itm.itm_id == itm_id:
                self.item_list.remove(itm)
                print("Item deleted successfully!")
                return
        print("Item NOT FOUND in system")
      
m1 = MANAGER()
choice1 = 'Y'
print("[[[[ITEM MANAGEMENT SYSTEM]]]]")
while choice1.upper() == 'Y':
    print("\n  [1]-------------Add items")
    print("  [2]-------------View items")
    print("  [3]-------------Update items")
    print("  [4]-------------Delete items")
    print("  [5]-------------Exit")
    choice = input("Input choice: ")

    match choice:
        case '1':
            m1.add_itm()
            choice1 = input("Proceed? [y/n]: ")
        case '2':
            m1.view()
            choice1 = input("Proceed? [y/n]: ")
        case '3':
            m1.update()
            choice1 = input("Proceed? [y/n]: ")
        case '4':
            m1.delete()
            choice1 = input("Proceed? [y/n]: ")
        case '5':
            break
        case _:
            print("Invalid choice, try again.")
print("Exiting...")
