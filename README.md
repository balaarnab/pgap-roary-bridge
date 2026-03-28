# pgap-roary-bridge
pgap-roary-bridge is a lightweight utility designed to address compatibility limitations between the NCBI Prokaryotic Genome Annotation Pipeline (PGAP) and Roary pan-genome analysis.

## About
Roary is one of the most popular and rapid prokaryotic pan-genome gene clustering pipelines. The pipeline takes General Feature Format version 3 (GFF3) files from an annotation pipeline in a specific orientation as input. Usually, the rapid prokaryotic genome annotation pipeline, Prokka creates an output GFF3 file that matches perfectly for the input of Roary pan-genome analysis. These two pipelines were designed by the same team and acknowledged for their compatibility. Although Prokka is greatly accessible and less resource consuming, it’s not highly comprehensive like the NCBI Prokaryotic Genome Annotation Pipeline (PGAP). However, the PGAP produces GFF3 files without sequences, unlike Prokka, making them not directly compatible with a Roary pan-genome analysis. Additionally, manual appending of genome tags to the attribute column elements is required to distinguish between different genomes in the output GFF3 files.
This mini-project includes three python scripts that assist to edit and append genome tags to the GFF3 files from a PGAP analysis in the least invasive way and compile it with the matching FASTA file to create a Roary analysis ready GFF3 file. 
The scripts are grouped into 3 steps:
1.	Genome-Specific Standardization of GFF3 Annotation Files (GFF3 file edit)
2.	Genome-Specific Standardization of FASTA Sequence Identifiers (FASTA file edit)
3.	Compilation of all edited files into one single input file for Roary (Compilation) 
## Repository structure
- `Scripts/` – Python scripts for GFF3 and FASTA processing
- `Test_files/` – Example input and output files
- `Validation/` – Roary results and comparison figures
## Required packages: 
a.	`pandas`
b.	`biopython`
## Test files:
For example, a PGAP annotated GFF3 file along with sequence FASTA file of the NCBI BioSample: SAMN44958832 (Only the 1st contig is used to reduce size) is included as test files.
Test files comprise,
            `Input.gff`
            `Input.fasta`
            `Ag1S.gff`
            `Ag1S.fasta`
            `Ag1S_Roary.gff`
## Procedure Steps:
1.	GFF3 file edit\
	a. Run the `gffV3_edit.py` script. The input file is named as `input.gff` but it may be required to be renamed according to the PGAP output (usually `annot.gff`).\
    b. Edit the `genome_name` according to requirement.\
	c. After a successful run, it will create a separate GFF file named the given `genome_name`. This file doesn’t contain the sequence.
3.	FASTA file edit\
	a. Run the `fasta_edit.py` script. Make sure the `genome_name` here is a copy of the one used in previous script.\
	b. The input file is named here as `input.fasta`, rename it according to the FASTA sequence file.\
	c. After a successful run it will create a new FASTA file of similar given `genome_name`.
4.	Compilation\
	a. Run the `compiling_files.py` script. Here three input files are required, `gff_file` = the edited GFF file in 1st step; `fasta_file` = the edited FASTA file in 2nd step; `header_source` = the main GFF3 file from PGAP annotation (Here, it’s `input.gff`). Rename the input on the script accordingly.\
	b. After a successful run a final GFF file will be created that can be used directly on Roary..
## Schematic diagram:
           Input.gff    ►    Script 1    ►    Ag1S.gff
           Input.fasta    ►    Script 2    ►    Ag1S.fasta
           Ag1S.gff + Ag1S.fasta + input.gff    ►    Script 3    ►    Ag1S_Roary.gff
## Validation
To check if the script is working properly a small benchmarking test run was performed using 4 Escherichia coli isolates of clonal lineage with less than 30 single nucleotide polymorphisms among them (NCBI BioSample: SAMN44958832; SAMN44958833; SAMN44958843; SAMN44958839). After curation of the GFF3 files, Roary pan-genome analysis was done and the result revealed around 88% of core genes and no cloud gene, indicating possible clonal lineage. A parallel pan-genome analysis of those 4 isolates was also performed from Prokka annotation GFF3 file for comparison. `Roary_result.tif` and `Comparison_graph.tif` figures are included to visualize the result and comparison. 
