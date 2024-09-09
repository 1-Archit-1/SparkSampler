# Define source and target files
source_file="medium_dataset.csv"
target_file="smallest_dataset.csv"

# Calculate total lines in source file
total_lines=$(wc -l < "$source_file")

# Calculate half the number of lines
half_lines=$((total_lines / 50))

# Extract the first half of the source file and append to target file
tail -n "$half_lines" "$source_file" >> "$target_file"

# Optionally, display the updated target file
cat "$target_file"