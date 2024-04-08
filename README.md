# Rojas2024_Aneuploidy
 Code for the paper: "Comparative modeling reveals the molecular determinants of aneuploidy fitness cost in a wild yeast model"   Julie Rojas, James Hose, H. Auguste Dutcher, Michael Place, John F Wolters, Chris Todd Hittinger, Audrey P Gasch

Ths project contain all code used and describe in the paper:

Comparative modeling reveals the molecular determinants of aneuploidy fitness cost in a wild yeast model 

Julie Rojas1, James Hose1, H. Auguste Dutcher1, Michael Place1,2, John F Wolters3, Chris Todd Hittinger3, Audrey P Gasch1,2,4

Affiliations:
1	Center for Genomic Science Innovation, University of Wisconsin-Madison, Madison, WI 53704, USA.
2	Great Lakes Bioenergy Research Center, University of Wisconsin-Madison, Madison, WI 53704, USA.
3	Laboratory of Genetics, DOE Great Lakes Bioenergy Research Center, Wisconsin Energy Institute, 
	Center for Genomic Science Innovation, J. F. Crow Institute for the Study of Evolution, University of Wisconsin-Madison, Madison, WI, United States
4	Department of Medical Genetics, University of Wisconsin-Madison, Madison, WI 53704, USA.

Keywords: Aneuploidy, dosage-sensitive genes, driver genes, CNV, snoRNA, tRNA

Abstract:
Although implicated as deleterious in many organisms, aneuploidy can underlie rapid phenotypic evolution. 
However, aneuploidy will only be maintained if the benefit outweighs the cost, which remains incompletely understood. 
To quantify this cost and the molecular determinants behind it, we generated a panel of chromosome duplications in S. cerevisiae 
and applied comparative modeling and molecular validation to understand aneuploidy toxicity. We show that a multi-factorial model 
including additive gene costs, measured for single-gene duplications using a genomic library, along with the deleterious contribution
of snoRNAs and beneficial effects of tRNAs explains 75-94% of the variance in aneuploid strains’ growth rates. Characterizing the 
properties of detrimental gene duplication using machine learning show no support for the balance hypothesis of aneuploidy toxicity 
and instead identifies gene length as the best predictor of toxicity. Our results present a generalized framework for the cost of 
aneuploidy with implications for disease biology and evolution. 

Notebook description and order to run:

For the Chromosome duplication modelling (Figure 1-3):\n
	1) Aneuploidy_barplot_dataset_preparation: format growth data, plotting, normalize\n
	2) Aneuploidy model for figure 1 to 3.\n

For duplication-sensitive genes classifier (Figure 5):
	1) MoBy_genes_features_dataset_prep: combine gene properties from differents sources
	2) MoBy_GSEA: functional enrichment for detrimental gene duplication (fisher and gsea method). 
	   Significant enrichment are added to the gene features dataset as categorial features.
	3) MoByGenes_ML: train classifier to predict detrimental gene duplication and neutral/beneficial gene duplication.

For the Commonly deleterious gene overexpression (Robinson et al. dataset) classifier (Figure 6):
MoByGenes_ML:
	1) Robinson_genes_features_dataset_prep: dataset assembly with gene properties from different sources 
	  (same features as Moby 1.0 but some variability in the measured gene set). 
	2) Robinson_CommonDS_Classifier: Hypergeometric test for fuctional enrichment in the commonly deleterious gene set
	   Significant functional enrichment are included as categorical features to the dataset. Train a classifier to predict genes that are commonly detrimental when overexpressed.
