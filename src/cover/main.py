import sys

# Check if the --input and --template arguments are provided
if len(sys.argv) != 5 or sys.argv[1] != "--input" or sys.argv[3] != "--template":
    print("Usage: python3 main.py --input <txt_file> --template <template_file>")
    sys.exit(1)

txt_file_path = sys.argv[2]
template_file_path = sys.argv[4]

# Read values from TXT file and prompt for input
placeholders = {}
with open(txt_file_path, 'r') as txt_file:
    for line in txt_file:
        line = line.strip()
        if line and not line.startswith('#'):  # Ignore comments starting with '#'
            key = line
            value = input(f"Enter the value for '{key}': ")
            placeholders[key] = value

# Read template
with open(template_file_path, 'r') as file:
    original_template = file.read()

# Replace placeholders in the template
formatted_template = original_template
for key, value in placeholders.items():
    formatted_template = formatted_template.replace(f"(({key}))", value)

# Overwrite the template file with the formatted output
with open(template_file_path, 'w') as file:
    file.write(formatted_template)

print(f"Template file '{template_file_path}' has been updated with formatted content.")
print("Press Enter when ready to revert the template file to its original content.")
input()

# Revert the template file back to its original content
with open(template_file_path, 'w') as file:
    file.write(original_template)
print(f"Template file '{template_file_path}' has been reverted to its original content.")
