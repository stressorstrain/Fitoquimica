from qbwPythonModule import *

gene_file='mm9_sel_chroms_knownGene.txt'
fopen=open(gene_file,'rU').readlines()

gene_info=loadGeneFile(gene_file)

chroms=[]
gene_counts={}

for k in gene_info.keys():
	chr=gene_info[k]['chr']
	if chr not in chroms:
		chroms=chroms+[chr]

for chr in chroms:
	chrom_count=0 
	for k in gene_info.keys():
		if gene_info[k]['chr']==chr:
			chrom_count+=1

	gene_counts[chr]=chrom_count
	
fa_file='selChroms_mm9.fa.zip'
