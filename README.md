# CRISPRDetect_summarizer

Author: Murat Buyukyoruk

Associated lab: Wiedenheft lab

        CRISPRDetect_summarizer help:

This script is developed to generate a summary file from a CRISPRDetect output file. The order of headers are:
    
        Array_no\tArray_type\tAccession\tName\tStart\tStop\tStrand\tSubtpye\tRepeat_occurence\tRepeat_length\tMedian_Spacer_lengt\tStd_Spacer_length\tRepeat_seq\tScore

statistics module is required. Additionally, tqdm is required to provide a progress bar since some multifasta files can contain long and many sequences.
        
Syntax:

        python CRISPRDetect_summarizer.py -i demo_CRISPRDetect.txt -o demo_summary.txt

CRISPRDetect_summarizer dependencies:

	statistics                                          https://anaconda.org/conda-forge/statistics
	tqdm                                                refer to https://pypi.org/project/tqdm/
	
Input Paramaters (REQUIRED):
----------------------------
	-i/--input		FASTA			Specify a CRISPRDetect output file.

	-o/--output		List			Specify a filename for summary output.
	
Basic Options:
--------------
	-h/--help		HELP			Shows this help text and exits the run.

