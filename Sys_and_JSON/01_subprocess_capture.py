# Import the subprocess module
# It is used to execute external system commands from Python
import subprocess

# Execute the 'echo' command and capture its output
# capture_output=True stores the command's stdout and stderr
# text=True returns the output as a string instead of bytes
result = subprocess.run(
    ["echo", "Capturing output!"],
    capture_output=True,
    text=True
)

# Display the exit status of the command
# A return code of 0 indicates successful execution
print("Return Code:", result.returncode)

# Display the captured standard output
# strip() removes any trailing newline characters
print("Captured Stdout:", result.stdout.strip())
