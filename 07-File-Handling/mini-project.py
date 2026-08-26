import requests

def get_data():
    url = "https://api.rootnet.in/covid19-in/stats/latest"
    response = requests.get(url)
    return response.json()

def show_summary(data):
    summary = data["data"]["summary"]
    print("\n-------INDIA SUMMARY--------")
    print("Total:",summary["total"])
    print("Discharged:",summary["discharged"])
    print("Deaths:",summary["deaths"])

def show_states(data):
    states = data["data"]["regional"]

    name = input("enter the state name:")

    for state in states:
        if name.lower() == state["loc"].lower():
            print("\n--------state data-----------")
            print("Confirmed:",state["totalConfirmed"])
            print("Discharged:",state["discharged"])
            print("Deaths:",state["deaths"])
            return
    print("State not found")

data = get_data()

while True:
    print("\n1.India Summary")
    print("\n2.State Summary")
    print("\n3.exist")

    choice = int(input("enter the choice:"))

    if choice == 1:
        show_summary(data)

    elif choice == 2:
        show_states(data)

    elif choice == 3: 

        break
    else:
        print("Invalid Choice")
         







