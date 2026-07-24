###############################################
#
# Working with List of Lists (Multi-dimensional Data Structures)
#
# When processing large amounts of input files, it is useful to store data in multi-dimensional data structures.
# A List of Lists helps to store data in a concise manner.
#
############################################### 

# Defining a List of Lists (a list containing 4 sub-lists)
a = [[1, 2], [1, 4], [3, 5], [5, 7]]

print("Original List of Lists:", a)

###############################################
#
# Accessing and Updating Values
#
# You can perform operations like searching for specific values and updating the list values.
#
############################################### 

# Accessing the first element of the first sub-list
print("First sub-list:", a[0])
print("Second element of the first sub-list:", a[0][1])

# Updating a value inside the list of lists
a[0][1] = 20
print("List after update:", a)

###############################################
#
# Iterating over a List of Lists
#
# You can use a nested for loop to traverse the sub-lists and their individual elements.
#
############################################### 

print("\nIterating through the list of lists:")
i = 0
for item in a:
    j = 0
    for item1 in item:
        # Printing each individual element from the sub-lists
        print(f"Element at [{i}][{j}] = {item1}")
        j += 1
    i += 1

###############################################
#
# Practical Application: Regression Reports
#
# List of Lists can be used for Test case overall information, where one item is linked to multiple data attributes.
# Pandas can be used to write a list of lists into an excel file.
#
############################################### 

# Each sub-list provides test name, description, test status, and comments
regression_report = [
    ["testname", "test description", "test status", "comments"],
    ["axi_wr_test", "check AXI Write txs", "PASS", "None"],
    ["axi_rd_test", "Check AXI Read txs", "PASS", "none"],
    ["axi_burst_test", "check the burst txs", "FAIL", "Wrap bursts are failing"]
]

print("\nRegression Report Data:")
for report_row in regression_report:
    print(report_row)
