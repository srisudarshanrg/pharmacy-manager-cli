from datetime import datetime
from functions import add_to_medicine_catalog, delete_from_medicine_catalog, purchase_medicine, add_to_customers, get_id_from_customer_name, get_customer_purchase_history

options = int(input("Are you an admin or a customer:\n" \
"(1) Admin\n" \
"(2) Customer\n"
"Enter Option: "))

if options == 1:
    admin_options = int(input("\nChoose one of the following options:\n" \
    "(1) add a medicine\n" \
    "(2) remove a medicine\n" \
    "(3) view customer records\n"
    "Enter Option: "))

    if admin_options == 1:
        add_medicine = input("\nSpecifiy the following fields:\n" \
        "- medicine name\n" \
        "- expire\n" \
        "- quantity\n" \
        "- price\n" \
        "separated by spaces:\n")

        medicine_description_list = add_medicine.split(" ")

        medicine_description = {
            "medicine": medicine_description_list[0],
            "expiry":  datetime.strptime(medicine_description_list[1], "%d/%m/%Y"),
            "quantity": medicine_description_list[2],
            "price": int(medicine_description_list[3])
        }

        status = add_to_medicine_catalog(medicine_name=medicine_description["medicine"], medicine=medicine_description)

    elif admin_options == 2:
        medicine_name = input("Enter medicine name: ")
        status = delete_from_medicine_catalog(medicine_name)
        print(status)