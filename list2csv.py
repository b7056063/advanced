from Bio import SeqIO
from Bio.Alphabet import generic_dna,generic_protein
#convert fasta files to genbank files
def fasta2genbank(test_fasta,test_gb):
    input_handle=open(test_fasta,"rU")
    output_handle=open(test_gb,"w")
    
    sequences=list(SeqIO.parse(input_handle,"fasta"))
    for seq in sequences:
        seq.seq.alphabet=generic_dna
    
    count=SeqIO.write(sequences,output_handle,"genbank")
    output_handle.close()
    input_handle.close()
    print("Converted %i records" % count)
#fasta2genbank("uniprot_sprot.fasta","test_gb")

def fasta2csv(fastafile,csvfile):
    for record in SeqIO.parse(fastafile,"fasta"):
        seq_dict={record.id:repr(record.seq)}
        my_list=[seq_dict]

    import csv
    import os

    def _build_csv():

#csv title
        columns=['seq_id','sequence']
#    columnss=bytes(columns,encoding="utf8")
        contents=my_list
        a=contents
        #print(contents)
#get current path
        root_path=os.getcwd()

#the whole path of this csv file
        tmp_path=root_path+"/temp.csv"
        f=open(tmp_path,"wb+")
        writer=csv.writer(f)

#write csv title
        writer.writerow(columns)
        for line in a:
            writer.writerow(line)
    if __name__=="__main__":
        _build_csv()
    return f
fastafile='/home/b7056063/uniprot_sprot.fasta'
fasta2csv(fastafile,"test_csv")

#fasta2csv(uniprot_sprot.fasta,test_gb)



#unit test
#import unittest

#class TruthTest(unittest.TestCase):
#    def testTrue(self):
#        assert True==1
#    def testFalse=0
#if __name__=='__main__':
#    unittest.main()
