# Import the subprocess module
# It allows Python programs to create and manage external processes
import subprocess

# Display a message before executing the external command
print("Running echo command via subprocess:")

# Execute the system command 'echo'
# subprocess.run() starts the command, waits for it to complete,
# and then returns control to the Python program.
subprocess.run(["echo", "Hello from system shell!"])
# subprocess.run(["mkdir", "Demo"])
