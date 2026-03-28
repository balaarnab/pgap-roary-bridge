## Script 2: Genome-Specific Standardization of FASTA Sequence Identifiers for Pangenome Analysis

from Bio import SeqIO

genome_name = 'Ag1S'     # Use your own file name, it must match the tag used in gff edit
input_file = "input.fasta"
output_file = f"{genome_name}.fasta"


# Parse input FASTA file and append genome identifier to sequence headers
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for record in SeqIO.parse(infile, "fasta"):
        
        # Use the primary sequence ID and ignore any description fields
        base_id = record.id.split()[0]
        new_id = f"{base_id}_{genome_name}"
        
        # Update all FASTA header fields consistently
        record.id = new_id
        record.name = new_id
        record.description = new_id

        SeqIO.write(record, outfile, "fasta")