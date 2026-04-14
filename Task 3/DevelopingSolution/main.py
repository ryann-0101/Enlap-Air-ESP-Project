import pandas as pd
import matplotlib.pyplot as plt

running = True

def load_data_from_csv():
    global flightData
    flightData = pd.read_csv("Task3_data_November 22.csv")
    print("Data loaded from CSV!") 
    return flightData 
  
def validate_data():
    print("--Data Validation--")

    print("Checking for empty dataset....")

    if len(flightData) > 0:
        print("Check complete! Dataset is not empty!")
    
    else:
        print(f"Check complete! Warning: Dataset is empty!")

    print("Checking for missing values....")

    if flightData.isnull().sum().sum() == 0:
        print("Check complete! No missing data found!")
    
    else:
        print(f"Check complete! Found {flightData.isnull().sum().sum()} missing values!")

def graphical_date_production():
    date_columns = flightData.columns[2:]
    dates = date_columns
    passengers = route_data[date_columns].iloc[0]

    plot_df = pd.DataFrame({
        'Date': dates,
        'Passengers': passengers
    })

    plt.figure()
    plt.plot(plot_df['Date'], plot_df['Passengers'])
    plt.xlabel("Date")
    plt.ylabel("Passenger Numbers")
    plt.title(f"Passengers per day: {selected.From} → {selected.To}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def graphical_number_production():
    date_columns = flightData.columns[2:]
    
    routes_data = []
    for idx, row in flightData.iterrows():
        total_passengers = row[date_columns].sum()
        route_label = f"{row['From']} → {row['To']}"
        routes_data.append({'Route': route_label, 'Total_Passengers': total_passengers})
    
    routes_df = pd.DataFrame(routes_data)
    routes_df = routes_df.sort_values('Total_Passengers', ascending=True)
    
    plt.figure(figsize=(10, 6))
    plt.bar(routes_df['Route'], routes_df['Total_Passengers'], color='skyblue')
    
    plt.xlabel("Routes")
    plt.ylabel("Total Passengers (Nov 2022)")
    plt.title("Total Passengers per Route - November 2022")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

load_data_from_csv()
validate_data()

while running:
   
    routes = list(flightData[['From', 'To']].drop_duplicates().itertuples(index=False))
    total_routes = len(routes)
    
    
    
    
    choice = input(f"\nEnter route number to view passenger numbers, 0 to view route list, G to view total passengers per route as a graph & E to exit): ")
    choice = choice.strip().lower()
    match choice:
        case "e":
            print("Terminating Program.")
            running = False
        case "0":
            route_num = 0
            for route in flightData[['From', 'To']].drop_duplicates().itertuples(index=False):
                route_num+=1
                print(f"{route_num} - {route.From} → {route.To}") 
        case "g":
            graphical_number_production()
        case other:
            if choice.isdigit():
                selected_num = int(choice)
                if 1 <= selected_num <= total_routes:
                    
                    selected = routes[selected_num-1]
                    
                   
                    print(f"\nPassenger data for {selected.From} → {selected.To}:")
                    
                    
                    route_data = flightData[
                        (flightData['From'] == selected.From) & 
                        (flightData['To'] == selected.To)
                    ]
                    
                    print(route_data)
                    graph = int(input("Would you like to view this as graphs?\n1 - View total passengers per day as graph\n2 - Exit program\nChoice: "))
                    match graph:
                        case 1:
                            graphical_date_production()
                       
                        case 2:
                            running = False
                            print("Goodbye!")
                    restart = int(input("Would you like to go back? 1 - Menu, 2 - Terminate Program\nChoice:"))
                    match restart:
                        case 1:
                            continue
                        case 2:
                            running = False
                        case other:
                            print("Invalid Choice, going back to menu")
                else:
                    print(f"Please enter 1-{total_routes} or E to exit")
            else:
                print("Please enter a valid option!")