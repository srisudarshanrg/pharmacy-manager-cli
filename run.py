from db import db, cur
from db_create import medicine_catalog, customer_info, purchase_record

cur.execute(medicine_catalog)
db.commit()

cur.execute(purchase_record)
db.commit()

cur.execute(customer_info)
db.commit()

# test
query = "SELECT * FROM medicines"
cur.execute(query)
rows = cur.fetchall()

if not rows:
    print("no rows available")
else:
    for row in rows:
        print(row)

cur.close()
db.close()