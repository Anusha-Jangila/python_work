from project import get_selections, calculate_cost, generate_report
from InquirerPy import inquirer
import plotext as plot

# Define the dictionary input for the functions to be tested
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

def test_get_selections(mocker):
    # Mock the inquirer.select().execute() method
    mock_select = mocker.patch('InquirerPy.inquirer.select')

    # Set up the side-effect to simulate user selections for each select prompt
    mock_select.return_value.execute.side_effect=['1','2','3']

    # Call the function to test
    result = get_selections(options)

    # Assert that the function returns the expected results
    assert result == ['1','2','3']

    # Assert that the inquirer.select was called three times
    assert mock_select.call_count == 3

def test_calculate_cost():
    selections = ['1','2','3']

    # Call the function to test
    result = calculate_cost(selections, options)

    # Assert that the function returns the expected result
    assert result == [14408.00, 8000.00, 10000.00]

def test_generate_report(mocker):
    # Mock the plot.show() method
    mock_show = mocker.patch('plotext.show')
    costs = [14408.00, 8000.00, 10000.00]

    # Call the function to test
    generate_report(costs)

    # Assert that the plot.show() was called once
    mock_show.assert_called_once()
