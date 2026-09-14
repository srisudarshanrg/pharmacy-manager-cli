def add_to_medicine_catalog(db, cur, medicine_name: str, medicine: dict) -> str:
    queryMedicineExists = "SELECT * FROM medicines where medicine=%s"

    try:
        cur.execute(queryMedicineExists, medicine_name)
        rowsMedicineExists = cur.fetchone()

        if rowsMedicineExists == None:
            query = "INSERT INTO medicines(medicine, expiry, quantity, price) VALUES(%s, %s, %s, %s)"

            values = (
                medicine.get("medicine"),
                medicine.get("expiry"),
                medicine.get("quantity", 1),
                medicine.get("price", float(0))
            )

            try:
                cur.execute(query, values)
                db.commit()

                return "medicine added"
            except Exception as e:
                return e
        else:
            _, _, _, _, quantity, _ = rowsMedicineExists
            
            queryUpdateCount = "UPDATE medicines SET quantity=%s WHERE medicine=%s"

            try:
                cur.execute(queryUpdateCount, int(quantity)+1)
                db.commit()

                return "medicine added to catalogue"
            except Exception as e:
                print(e)

    except Exception as e:
        print(e)

def delete_from_medicine_catalog(db ,cur, medicine_name) -> str:
    queryDeleteMedicine = "DELETE FROM medicines WHERE medicine=%s"
    cur.execute(queryDeleteMedicine, medicine_name)
    db.commit()

    return "medicine deleted from catalog"

def purchase_medicine(db, cur, customer_name: int, customer_phone: int, medicine_name: str) -> str:
    queryCheckMedicineExists = "SELECT * FROM medicines WHERE medicine=%s"
    cur.execute()

    check_medicine = cur.fetchone(queryCheckMedicineExists, medicine_name)
    if check_medicine == None:
        return "this medicine is not in our catalogue"
    else:
        medicine_id, _, _, quantity, _ = check_medicine

        queryCheckCustomerExists = "SELECT * FROM customers WHERE name=%s AND phone=%s"
        cur.execute(queryCheckCustomerExists, customer_name, customer_phone)
        check_customer = cur.fetchone()

        if check_customer == None:
            queryAddCustomer = "INSERT INTO customers(name, phone) VALUES(%s, %s)"
            cur.execute(queryAddCustomer, customer_name, customer_phone)

            customer_id = cur.lastrowid
            db.commit()

            queryAddToPurchaseRecords = "INSERT INTO purchase_records(medicine_id, customer_id) VALUES(%s, %s)"
            cur.execute(queryAddToPurchaseRecords, medicine_id, customer_id)

            querySubtractStockMedicine = "UPDATE medicines SET quantity=%s where id=%s"
            cur.execute(querySubtractStockMedicine, int(quantity)-1, customer_id)

            db.commit()

        else:
            customer_id, _, _ = check_customer

            queryAddToPurchaseRecords = "INSERT INTO purchase_records(medicine_id, customer_id) VALUES(%s, %s)"
            cur.execute(queryAddToPurchaseRecords, medicine_id, customer_id)

            querySubtractStockMedicine = "UPDATE medicines SET quantity=%s where id=%s"
            cur.execute(querySubtractStockMedicine, int(quantity)-1, customer_id)

            db.commit()


def add_to_customers(db, cur, customer: str) -> str:
    query = "INSERT INTO customers(name) VALUES(%s)"

    values = (
        customer
    )

    try:
        cur.execute(query, values)

        db.commit()
        return "customer added"
    except Exception as e:
        return e

def purchase(db, cur, medicine_id: int, customer_id: int):
    query = "INSERT INTO purchase_records(medicine_id, customer_id) VALUES(%s, %s)"

    values = (
        medicine_id,
        customer_id
    )

    try:
        cur.execute(query, values)

        db.commit()
        return "purchase record added"
    except Exception as e:
        return e

def get_id_from_customer_name(db, cur, name:str, phone: int) -> int:
    query = "SELECT * FROM medicines WHERE name=%s AND phone=%s"

    try:
        cur.execute(query, name, phone)
        row = cur.fetchone()

        if row:
            id, _, _ = row
            return id
        else:
            print("no such customer found")
            return
    except Exception as e:
        print(e)
        return


def get_customer_purchase_history(db, cur, customer_name: str, phone: int) -> list[dict]:
    customer_id = get_id_from_customer_name(customer_name, phone)

    queryGetCustomerRecords = "SELECT * FROM purchase_records WHERE customer_id=%s"

    try:
        cur.execute(queryGetCustomerRecords, customer_id)
        rowsPurchases = cur.fetchall()
        for rowPurchases in rowsPurchases:
            _, medicine_id, _ = rowPurchases

            queryGetCustomerPurchases = "SELECT * FROM medicines WHERE id=%s"
            cur.execute(queryGetCustomerPurchases, medicine_id)
            rowsMedicines = cur.fetchall()

            list_purchases = []

            try:
                for rowMedicine in rowsMedicines:
                    id, medicine, expiry, quantity, price = rowMedicine
                    purchase = {
                        "id": id,
                        "name": customer_name,
                        "medicine": medicine,
                        "expiry": expiry,
                        "quantity": quantity,
                        "price": price
                    }

                    list_purchases.append(purchase)

                return list_purchases

            except Exception as e:
                print(e)
                return

    except Exception as e:
        print(e)
        return e