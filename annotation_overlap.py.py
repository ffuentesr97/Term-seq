def find_overlapping_annotations(file1, file2):
    """
    Find overlapping annotations between two files.

    Parameters:
        file1 (str): Path to the first annotation file.
        file2 (str): Path to the second annotation file.

    Returns:
        list: A list of tuples containing overlapping annotations.
    """
    annotations1 = load_annotations(file1)
    annotations2 = load_annotations(file2)
    overlapping_annotations = []

    for annotation1 in annotations1:
        for annotation2 in annotations2:
            if is_overlap(annotation1, annotation2):
                overlapping_annotations.append((annotation1, annotation2))

    return overlapping_annotations

def load_annotations(file):
    """
    Load annotations from a GTF-like file.

    Parameters:
        file (str): Path to the annotation file.

    Returns:
        list: A list of tuples containing start, end, and gene name for each annotation.
    """
    annotations = []
    with open(file, 'r') as f:
        for line in f:
            data = line.strip().split('\t')
            start = int(data[3])  # Start position
            end = int(data[4])    # End position
            gene_name = data[8]   # Gene name or description
            annotations.append((start, end, gene_name))
    return annotations

def is_overlap(annotation1, annotation2):
    """
    Check if two annotations overlap.

    Parameters:
        annotation1 (tuple): A tuple containing start and end positions of the first annotation.
        annotation2 (tuple): A tuple containing start and end positions of the second annotation.

    Returns:
        bool: True if the annotations overlap, False otherwise.
    """
    start1, end1, _ = annotation1
    start2, end2, _ = annotation2
    return start1 <= end2 and start2 <= end1

def save_overlapping_annotations(overlapping_annotations, output_file):
    """
    Save the overlapping annotations to a text file.

    Parameters:
        overlapping_annotations (list): List of tuples with overlapping annotations.
        output_file (str): Path to the output file.
    """
    with open(output_file, 'w') as f:
        for annotation1, annotation2 in overlapping_annotations:
            f.write("TERM_SEQ: {}\n".format(annotation1))
            f.write("Rho_independent: {}\n".format(annotation2))
            f.write("----------------------\n")

# Example usage
file1 = 'HH103_term35_sorted.gtf'
file2 = 'ter_rhoi_sorted.gtf'
overlapping_annotations = find_overlapping_annotations(file1, file2)
output_file = 'result_termseq_vs_rhoind.txt'
save_overlapping_annotations(overlapping_annotations, output_file)
