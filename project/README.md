# HOME BUILDING SELECTION SYSTEM
#### Video Demo:  https://youtu.be/RRczmyB2ixY
#### Description:
 - **Purpose:** The **Home Building Selection System** is an interactive Python application that allows users to select various home building options, such as
   elevation, countertops, and flooring from a dynamic menu. The system calculates the total cost of the selected items and provides a detailed breakdown, including a visual budget report. This project is designed to help homeowners or builders manage their selection process efficiently while staying within budget.
 - **Scope:** Although I only considered elevation, countertops and flooring selections for this project, it is extendable.
 - **User Interaction:** To have it working on the codespace, I made it a command-line tool, but this project can be made a GUI application, by replacing
   InquirerPy library with Tkinter.
 - **Data:** Used a dictionary to store the data for this project, which can be enhanced to be driven from a database.
 - **Out of scope:** Not handled in this scope, but the selections can as well be saved to the database for review or modifications later.
 - **Functionality:**
   - **Display Options:** Show available selections to the user.
   - **User Input:** Allow users to select from available options dynamically from a list.
   - **Calculate Costs:** Calculate the cost for each category based on user selections. Also, breakdown the total cost by categories and show the percentages.
   - **Generate Report:** Provide the total cost and breakdown of the toal cost by categories and show the percentages. Also, show the cost breakdown by
     categories using a bar chart visualization. This chart shows the proportion of each category(elevation, countertops, flooring) in terms of their costs.
 - **Usage:**
   Once you start the application, you will be presented with a menu of home building options such as elevation, countertops and flooring. Simply follow the prompts in the terminal to select the items of your choice.
   Once you've made your selections, the system will calculate the total cost based on your selections and display a detailed breakdown by category(a summary of the items you chose and their respective costs). Additionally, a visual bar chart will show the percentage of money spent in each category.
 - **Error handling:** Added error handling to ensure the program handles run-time errors gracefully.
 - **Python dependencies:**
   - **plotext:** Used this Python library to create a plot directly in the terminal, without opening a separate graphical interface.
     plotext.bar(categories, costs) - creates a bar chart with the specified categories and costs.
     plotext.show() - renders the bar chart in the terminal.
   - **InquirerPy:** To display options as a dropdown, the graphical user interface library, tkinter was used initially, but the codespace wasn't allowing to
     create a window, so as an alternative used InquirerPy library for dropdown-like experience in the terminal. It allows to create interactive prompts in the terminal, similar to dropdowns.
 - **Unit tests:** To write unit tests for a Python function that captures input from the user using InquirerPy.select, pytest-mock plugin was used. The mocker
   fixture provided by pytest-mock, allows to mock the functions. Mocking replaces the original function with a mock object. This allows to simulate user input. The return values for each call were specified using side_effect.
