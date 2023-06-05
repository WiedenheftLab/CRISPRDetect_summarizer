#!/usr/bin/python

import argparse
import sys
import os
from tqdm import tqdm
import subprocess
import textwrap
import statistics


parser = argparse.ArgumentParser(prog='python CRISPRDetect_summarizer.py',
      formatter_class=argparse.RawDescriptionHelpFormatter,
      epilog=textwrap.dedent('''\

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

	
      	'''))
parser.add_argument('-i', '--input', required=True, type=str, dest='filename',
                        help='SSpecify a CRISPRDetect output file.\n')

parser.add_argument('-o', '--output', required=True, dest='out',
                        help='Specify a filename for summary output.\n')

results = parser.parse_args()
filename = results.filename
out = results.out

os.system("> " + out)

f = open(out, 'a')
sys.stdout = f

print "Array_no\tArray_type\tAccession\tName\tStart\tStop\tStrand\tSubtpye\tRepeat_occurence\tRepeat_length\tMedian_Spacer_lengt\tStd_Spacer_length\tRepeat_seq\tScore"

proc = subprocess.Popen("grep -c '>' " + filename, shell=True, stdout=subprocess.PIPE, )
length = int(proc.communicate()[0].split('\n')[0])

with tqdm(range(length)) as pbar_sum:
    pbar_sum.set_description('Creating summary file...' + filename)
    with open(filename, 'rU') as file:
        for line in file:
            line_arr = line.split()
            if (len(line_arr) != 0):
                if line_arr[0] == "Array":
                    array_no = line_arr[1]
                if "# Array family :" in line:
                    subtype = line.split("# Array family : ")[1].split('\n')[0]
                if "# Summary:" in line:
		    pbar_sum.update()
                    arr = line.split("ID_START_STOP_DIR: ")[1].split(';')
                    name = arr[0]
                    fullname = name.split("-")[0]
                    acc = name.split()[0]
                    low_bound = name.split("-")[-3]
                    high_bound = name.split("-")[-2]
                    ori = name.split("-")[-1]
                    dr_seq = arr[1].split(":")[1]
                    dr_len = arr[2].split(":")[1]
                    rep_occ = arr[3].split(":")[1]
                    score = arr[-2].split(":")[1]
                    spacers = arr[-1].split(":")[1].replace(" ","").split(",")
                    temp = [len(ele) for ele in spacers]
                    res_median = 0 if len(temp) == 0 else statistics.median(temp)
                    res_stdev = 0 if len(temp) == 0 else statistics.stdev(temp)

                    print acc + '_Array_' + array_no + '\tCRISPR\t' + acc + '\t' + fullname + '\t' + low_bound + '\t' + high_bound + '\t' + ori + '\t' + subtype + '\t' + rep_occ + '\t' + dr_len + '\t' + str(res_median) + '\t' + str(res_stdev) + '\t' + dr_seq + '\t' + score

