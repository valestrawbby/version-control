import datetime

# Get the current date and time
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Path to the version.md file
file_path = "docs/version.md"

# Write the current date and time to the file
with open(file_path, "w") as file:
    file.write(f"Version generated on: {now}\n")

print(f"Date and time written to {file_path}")
# Asked chat gpt to help generate this code 


