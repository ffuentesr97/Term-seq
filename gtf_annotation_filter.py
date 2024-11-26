def overlap(start1, end1, start2, end2):
    """Checks if two regions overlap."""
    return end1 >= start2 and end2 >= start1


def filter_gtf(file_path, distance_threshold):
    """Filters the GTF file by removing annotations that are too close and keeping the one with the higher score."""

    # Open the GTF file
    with open(file_path, "r") as file:
        lines = file.readlines()

    new_lines = []  # List to store the selected lines
    prev_end = None  # Variable to store the end position of the previous annotation
    prev_score = None  # Variable to store the score of the previous annotation

    # Iterate through the lines of the file
    for line in lines:
        if line.startswith("#"):
            # Keep comment lines
            new_lines.append(line)
            continue

        # Split the elements of the line
        elements = line.split("\t")

        # Get the start, end, and score values of the current annotation
        start = int(elements[3])
        end = int(elements[4])
        score = float(elements[5])

        if prev_end is None or not overlap(prev_end, prev_end + distance_threshold, start, end):
            # Keep the line if there is no overlap with the previous annotation
            new_lines.append(line)
            prev_end = end
            prev_score = score
        else:
            # If there is an overlap, compare the scores and update if the current score is higher
            if score > prev_score:
                new_lines[-1] = line  # Replace the previous line with the current line
                prev_score = score

    # Save the selected lines in a new file
    new_file_path = file_path.replace(".gtf", "_filtered.gtf")
    with open(new_file_path, "w") as file:
        file.writelines(new_lines)

    print("Filtered GTF file saved as:", new_file_path)


# Call the function to filter the GTF file
gtf_file_path = "HH103_rev_name.gtf"  # Replace with the path to your GTF file
threshold_distance = 2  # Replace with the desired distance threshold

filter_gtf(gtf_file_path, threshold_distance)
