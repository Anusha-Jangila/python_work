import plotext as plot
from InquirerPy import inquirer

def main():
    # Define options in a dictionary, with example data
    options = {
        'Elevation':{
            '1':{'name': 'Modern Farmhouse', 'price': 14408.00},
            '2':{'name': 'Coastal Classic', 'price': 5000.00},
            '3':{'name': 'Cottage Style', 'price': 10000.00},
            '4':{'name': 'Craftsman Style', 'price': 15000.00}
        },
        'Countertops':{
            '1':{'name': 'Laminate', 'price': 10.00},
            '2':{'name': 'Granite', 'price': 40.00},
            '3':{'name': 'Quartz', 'price': 59.00}
        },
        'Flooring':{
            '1':{'name': 'Carpet', 'price': 3.00},
            '2':{'name': 'Vinyl sheet', 'price': 2.00},
            '3':{'name': 'Vinyl planks', 'price': 4.00},
            '4':{'name': 'Hardwood', 'price': 7.00}
        }
    }
    selections = get_selections(options)
    costs = calculate_cost(selections, options)
    generate_report(costs)

# Show available options to the user and capture the selections
# options - dictionary of the available selections
def get_selections(options):
    print("Home Building Selection Tool")

    # Allow user to select from a list of elevations
    selected_elevation = inquirer.select(
        message = "Elevation",
        choices = [{"name": f"{value['name']} - ${value['price']:,.2f}", "value" : key} for key, value in options['Elevation'].items()]
    ).execute()

    # Allow user to select from a list of countertops
    selected_countertop = inquirer.select(
        message = "Countertop",
        choices = [{"name": f"{value['name']} - ${value['price']:,.2f} per sqft", "value" : key} for key, value in options['Countertops'].items()]
    ).execute()

    # Allow user to select from a list of flooring options
    selected_flooring = inquirer.select(
        message = "Flooring",
        choices = [{"name": f"{value['name']} - ${value['price']:,.2f} per sqft", "value" : key} for key, value in options['Flooring'].items()]
    ).execute()

    return [selected_elevation, selected_countertop, selected_flooring]

# Calculate costs based on user selections
# selections - list of user made selections
# options - dictionary of the available selections
def calculate_cost(selections, options):
    try:
        elevation_cost = options['Elevation'][selections[0]]['price']
        countertop_cost = options['Countertops'][selections[1]]['price'] * 200 # Assumption for simplicity: Fixed area of 200sqft for countertops
        flooring_cost = options['Flooring'][selections[2]]['price'] * 2500 # Assumption for simplicity: Fixed area of 2500sqft for flooring

        return [elevation_cost, countertop_cost, flooring_cost]

    except Exception as e:
        print(f"An error occurred: {e}")

# Display the total cost and cost breakdown along with percentages and a bar chart
# costs - costs associated with the user made selections
def generate_report(costs):
    try:
        total_cost = sum(costs)

        elevation_cost = costs[0]
        countertop_cost = costs[1]
        flooring_cost = costs[2]

        # Calculate percentages
        elevation_percentage = (elevation_cost / total_cost) * 100
        countertop_percentage = (countertop_cost / total_cost) * 100
        flooring_percentage = (flooring_cost / total_cost) * 100

        # Format the total cost with commas and round off to two decimal places
        print(f"\nTotal cost for your selections : ${total_cost:,.2f}")

        # Display a breakdown of costs
        print("Cost Breakdown")
        print(f" Elevation - ${elevation_cost:,.2f} ({elevation_percentage:.2f}%)")
        print(f" Countertop - ${countertop_cost:,.2f} ({countertop_percentage:.2f}%)")
        print(f" Flooring - ${flooring_cost:,.2f} ({flooring_percentage:.2f}%)")

        print()

        # Plot a vertical bar chart with the options on x- axis and cost on y-axis
        option_categories = ['Elevation','Countertops','Flooring']
        costs = [elevation_cost, countertop_cost, flooring_cost]
        plot.bar(option_categories, costs, color="blue")
        plot.title('Cost Breakdown')

        # Display the plot
        plot.show()
    except Exception as e:
        print(f"An error occured: {e}")

if __name__ == "__main__":
    main()
