# Read the TXT file with names
with open('term_rhosites.txt', 'r') as names_file:
    names = names_file.read().splitlines()

# Open the GTF file for reading
with open('HH103_term35_sorted.gtf', 'r') as gtf_file:
    gtf_lines = gtf_file.readlines()

# Open a new GTF file for writing
with open('modified_file.gtf', 'w') as new_gtf_file:
    for line in gtf_lines:
        # Check if any name from the list is present in the current line
        if any(name in line for name in names):
            # Add the additional column "type=rho_ind"
            fields = line.split('\t')
            new_field = fields[8].rstrip('\n') + ';type=rho_ind'
            fields[8] = new_field
            modified_line = '\t'.join(fields) + '\n'
            new_gtf_file.write(modified_line)
        else:
            new_gtf_file.write(line)
