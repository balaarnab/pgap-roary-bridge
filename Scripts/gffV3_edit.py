## Script 1: Genome-Specific Standardization of GFF3 Annotation Files for Pangenome Analysis

import pandas as pd

genome_name = 'Ag1S'
gff_file = 'input.gff'


# Load GFF file
df = pd.read_csv(gff_file, sep='\t', header=None, comment='#')

# Normalize annotation source field to 'PGAP'
df[1] = df[1].str.replace('Local', 'PGAP', regex=False)
df[1] = df[1].str.replace('.', 'PGAP', regex=False)
df[1] = df[1].str.replace('Protein Homology', 'PGAP', regex=False)
df[1] = df[1].str.replace('tRNAscan-SE', 'PGAP', regex=False)
df[1] = df[1].str.replace('GeneMarkS-2+', 'PGAP', regex=False)
df[1] = df[1].str.replace('cmsearch', 'PGAP', regex=False)
df[1] = df[1].fillna('PGAP')

# Append genome identifier to contig/seq IDs
df[0] = df[0].astype(str) + '_' + genome_name

# Ensure coordinates are integers
df[3] = df[3].fillna(0).astype(int)
df[4] = df[4].fillna(0).astype(int)

# Parse attributes column into a list
df[8] = df[8].fillna('').apply(lambda x: x.split(';') if isinstance(x, str) else x)

# Append genome identifier to feature attributes
df[8] = df[8].apply(lambda attrs: [attr if not attr.startswith('locus_tag=') else attr + '_' + genome_name for attr in attrs])
df[8] = df[8].apply(lambda attrs: [attr if not attr.startswith('ID=') else attr + '_' + genome_name for attr in attrs])
df[8] = df[8].apply(lambda attrs: [attr if not attr.startswith('Parent=') else attr + '_' + genome_name for attr in attrs])
df[8] = df[8].apply(lambda attrs: [attr if not attr.startswith('protein_id=') else attr + '_' + genome_name for attr in attrs])

df[8] = df[8].apply(
    lambda attrs: [
        attr + '_' + genome_name if attr.startswith('Name=extdb:') else attr
        for attr in attrs
    ]
)

# Rebuild attributes string and export
df[8] = df[8].apply(lambda items: ';'.join(items))

df.to_csv(f'{genome_name}.gff', sep='\t', header=False, index=False)