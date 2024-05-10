from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

class Person:
    def __init__(self, name, transactions):
        self.name = name
        self.transactions = transactions

def add_person(name):
    return Person(name, [])

def add_transaction(payer, total, detail, beneficiaries):
    if not isinstance(payer, Person):
        raise ValueError("Payer must be a Person object")
    if not all(isinstance(b, Person) for b in beneficiaries):
        raise ValueError("All beneficiaries must be Person objects")
    transaction = {"total": total, "detail": detail, "beneficiaries": beneficiaries, "num_beneficiaries": len(beneficiaries)}
    payer.transactions.append(transaction)

def calculate_total_cost(people):
    total_cost = 0
    for person in people:
        for transaction in person.transactions:
            total_cost += transaction["total"]
    return total_cost

def calculate_debt(person, people):
    person_paid = sum(t["total"] for t in person.transactions)
    person_share = 0
    for p in people:
        for t in p.transactions:
            if person in t["beneficiaries"]:
                person_share += t["total"] / t["num_beneficiaries"]
    return person_share - person_paid

# Create a dictionary of Person objects
people_dict = {
    "Raul": add_person("Raul"),
    "Narcisa": add_person("Narcisa"),
    "Edi": add_person("Edi"),
    "Andreea": add_person("Andreea"),
    "Patrick": add_person("Patrick"),
    "GBolba": add_person("G. Bolba"),
    "ABolba": add_person("A. Bolba")
}

# Assign the Person objects to the variables
raul = people_dict["Raul"]
narcisa = people_dict["Narcisa"]
edi = people_dict["Edi"]
andreea = people_dict["Andreea"]
patrick = people_dict["Patrick"]
g_bolba = people_dict["GBolba"]

# Transactions
add_transaction(raul, 4770, "Avion", [raul, narcisa, edi, andreea])
add_transaction(raul, 380, "Parking", [raul, narcisa, edi, andreea])
add_transaction(raul, 160, "Vinieta", [raul, narcisa, edi, andreea])
# add_transaction(raul, 0, "Motorina", [raul, narcisa, edi, andreea])  # TO BE ADDED COMPLETED
add_transaction(patrick, 5100, "Cazare", [patrick, raul, narcisa, edi, andreea])


# Debts
total_cost = calculate_total_cost(people_dict.values())
print(total_cost)
raul_debt = calculate_debt(raul, people_dict.values())

# Create a list of all transactions
transactions = [(p.name, t["total"], t["detail"], [b.name for b in t["beneficiaries"]]) 
                for p in people_dict.values() 
                for t in p.transactions]
# Create the transactions DataFrame
df_transactions = spark.createDataFrame(transactions, ["Payer", "Total", "Detail", "Beneficiary"])
df_transactions.show(truncate=False)

print(raul_debt)