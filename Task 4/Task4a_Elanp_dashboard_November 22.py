import pandas as pd
import matplotlib.pyplot as plt

def main_menu():
    
    print("#################################################")
    print("#### Welcome to Elanp Air Flight Data system ####")
    print("#################################################\n")
    return get_depart()
    



def get_depart():
    

    while True:

        print("########### Please select departure airport #############")
        print("### 1. Dublin (DUB)")
        print("### 2. Edinburgh (EDI)")
        print("### 3. Glasgow (GLA)")
        print("### 4. London Heathrow (LHR)")
        print("### 5. London Luton (LTN)")
        print("### 6. Manchester (MAN)")

        

        try:
            choice = int(input('Enter your number selection here: '))
            if choice in range(1,7):
                print("Departure choice accepted!")
                return choice
            else:
                print("Sorry, you did not enter a valid option")
        except ValueError:
            print("Sorry, you did not enter a valid option")

            
        

    


def get_destination(depart):
    

    while True:

        print("########### Please select destination airport #############")
        print("### 1. Dublin (DUB)")
        print("### 2. Edinburgh (EDI)")
        print("### 3. Glasgow (GLA)")
        print("### 4. London Heathrow (LHR)")
        print("### 5. London Luton (LTN)")
        print("### 6. Manchester (MAN)")

        
       
        try:
            choice = int(input('Enter your number selection here: '))
            if choice == depart:
                print("")
                print("")
                print("############### Data entry error ###################")
                print('Destination and departure airports must be different')
                print("")
                print("")  

            elif choice in range(1,7):
                print("Departure choice accepted!")
                return choice
            else:
                print("Sorry, you did not enter a valid option")
        except ValueError:
            print("Sorry, you did not enter a valid option")



def get_number_days():
    while True:
        print("########### Please enter the number of previous days of data you wish to see #############")
        
        choice = input('Enter your number selection here: ')
        
        try:
            days = int(choice)
            if days > 90 or days <= 0:
                print("Invalid Entry - must be between 1 and 90.")
            else:
                print(f"########### You have chosen to see data for the last {days} days #############")
                return days
        except ValueError:
            print("Sorry, you did not enter a valid number")



        
        

def convert_men_choice(choice):
    if choice is None:
        print("Error: No airport choice was selected")
        return None  
    if int(choice) == 1:
        conv_choice = "DUB"
        return conv_choice
    elif int(choice) == 2:
        conv_choice =  "EDI"
        return conv_choice
    elif int(choice) == 3:
        conv_choice =  "GLA"
        return conv_choice
    elif int(choice) == 4:
        conv_choice =  "LHR"
        return conv_choice
    elif int(choice) == 5:
        conv_choice =  "LTN"
        return conv_choice
    else:
        conv_choice =  "MAN"
        return conv_choice

def quick_analyze(data_frame):
    global daily_totals
    
    def passTotal():
        print("\n1. TOTAL PASSENGERS PER DAY:")
        daily_totals = data_frame.sum(axis=0)  # sum across rows
        for date, total in daily_totals.items():
            print(f"   {date}: {total} passengers")
        analysisMenu()

    def bestWorstDays():
        global daily_totals
        print("\n2. BEST & WORST DAYS:")
        daily_totals = data_frame.sum()
        
        best_day = daily_totals.idxmax()
        best_value = daily_totals.max()
        
        worst_day = daily_totals.idxmin()
        worst_value = daily_totals.min()
        
        print(f"   Best day: {best_day} ({best_value} passengers)")
        print(f"   Worst day: {worst_day} ({worst_value} passengers)")
        analysisMenu()
    
    def overallAnalysis():
        print("\n3. OVERALL:")
        daily_totals = data_frame.sum()
        all_total = daily_totals.sum()
        print(f"   All passengers: {all_total}")
        print(f"   Average per day: {all_total/len(daily_totals):.0f}")
        analysisMenu()

    def analysisMenu():
        analysisChoice = int(input("""### QUICK ANALYSIS MENU ###
1 - Total Passengers Per Day
2 - Best & Worst Days
3 - Overall Passenger Number Analysis
4 - Back To Data Menu
Enter Choice: """))
        match analysisChoice:
            case 1:
                passTotal()
            case 2:
                bestWorstDays()
            case 3:
                overallAnalysis()
            case 4:
                return

    analysisMenu()


def bar(data_to_plot):
    global extracted_data

    dates = data_to_plot.columns.tolist()  
    passenger_numbers = data_to_plot.iloc[0].tolist()  
    plt.figure(figsize=(12, 6))  
    plt.bar(dates, passenger_numbers)
    plt.xlabel('Flight Date', fontsize=12)
    plt.ylabel('Passenger Numbers', fontsize=12)
    plt.title(f'Passenger Numbers from {dep_choice} to {dest_choice}', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    

def get_data(depart, dest, days):
    df = pd.read_csv("Task4a_data.csv")
    extract = df.loc[(df['From'] == depart) & (df['To'] == dest)]
    
    if extract.empty:
        print("No flights match this criteria.")
        return None
    
    extract_days = extract.iloc[:, -days:]
    
    def dataMenu():
        dataOption = int(input("""### - Menu - ###
1 - View passenger data (Raw Data)
2 - View passenger data (Bar Chart)
3 - View passenger data (Analysed Breakdown)
4 - View table metadata
5 - Back to main menu
Enter: """))
        
        match dataOption:
            case 1:
                print(extract_days)
                dataMenu()
            case 2:
                print("Generating barchart")
                bar(extract_days)
                dataMenu()
            case 3:
                quick_analyze(extract_days) 
                dataMenu()
            case 4:
                print(extract_days.info())
                dataMenu()
            case 5:
                return

    dataMenu()


   
while True:
    depart_airport = main_menu()


    destination_airport = get_destination(depart_airport)

    dep_choice = convert_men_choice(depart_airport)
    dest_choice = convert_men_choice(destination_airport)

    days = get_number_days()
    print("You have selected departure from: {}".format(dep_choice))
    print("You have selected destination as: {}".format(dest_choice))




    extracted_data = get_data(dep_choice, dest_choice, days) 


    if extracted_data is not None:
        extract_no_index = extracted_data.to_string(index=False)
        print(extract_no_index)

