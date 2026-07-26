import re
# Extracting VHDL/Verilog port names
line = "  data_out : out std_logic_vector(31 downto 0);"
match = re.match(r'\s*(.*)\s*:\s*(out|in)\s*std_logic_vector', line)
if match:
    print("Found Port:", match.group(1).strip(), "| Direction:", match.group(2))
