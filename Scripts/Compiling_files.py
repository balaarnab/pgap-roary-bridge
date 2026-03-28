## Script 3: Compilation of all edited files into one single input file for the Roary analysis

gff_file = "Ag1S.gff"  # The edited GFF file
fasta_file = "Ag1S.fasta"  # The edited FASTA file
header_source = "input.gff"  # The main annotation GFF file
output_file = "Ag1S_Roary.gff"  # Final output for Roary analysis


with open(output_file, "w") as out:

    # Write header lines from main GFF file
    with open(header_source) as header:
        for line in header:
            if line.startswith("#"):
                out.write(line)

    # Write the edited GFF file
    with open(gff_file, "r") as gff:
        for line in gff:
            out.write(line.rstrip("\n") + "\n")

    # Insert FASTA separator
    out.write("##FASTA\n")

    # Write FASTA sequence
    with open(fasta_file, "r") as fasta:
        for line in fasta:
            out.write(line.rstrip("\n") + "\n")