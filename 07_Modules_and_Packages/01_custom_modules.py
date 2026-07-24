# Importing custom local modules
# Assuming 'vlsi_tools/alu1.py' is in your PYTHONPATH or local directory
import sys
sys.path.append("../vlsi_tools") # Adding the tools directory to path

try:
    import alu1
    print("Successfully imported custom module 'alu1'")
except ModuleNotFoundError:
    print("Could not find alu1.py. Make sure the vlsi_tools directory exists.")
try:
    import alu2
    print("Successfully imported custom module 'alu2'")
except ModuleNotFoundError:
    print("Could not find alu2.py. Make sure the vlsi_tools directory exists.")
