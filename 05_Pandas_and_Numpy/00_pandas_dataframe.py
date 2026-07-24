import pandas as pd
# Creating a DataFrame (2D table) from a dictionary
data = {
    'Test_Name': ['alu_test', 'fifo_test', 'fsm_test'],
    'Status': ['PASS', 'FAIL', 'PASS']
}
df = pd.DataFrame(data)
print("Basic DataFrame:\n", df)
