
PREFIX = 'BpliTokyo1'


def parse_fasta(in_path, out_path):

    out_fhand = open(out_path, 'wt')        

    for line in open(in_path):
        
        line = line.strip()          
        if line.startswith('>'):
        
            gene_number, transcript_number = line[2:].split('.')
            transcript_number = transcript_number.replace('t', '')
            
            new_header = '>{}g{:05d}.{}\n'.format(PREFIX, int(gene_number), transcript_number)
            out_fhand.write(new_header)
            continue
            
        out_fhand.write(line + '\n')
    
    out_fhand.close()

    return
    
    
def parse_gff(in_path, out_path):

    out_fhand = open(out_path, 'wt')
    
    for line in open(in_path):
        
        line = line.strip().split('\t')
        gene_info = line[-1]
        
        new_line = '\t'.join(line[0:-1]) + '\t'
        
        for field in gene_info.split(';'):
            if not field:
                continue
                   
            ID, value = field.split('=')
            renamed_value = []
            for sub in value.split('.'):
                if sub.startswith ('g'):
                    gene_number = sub[1:]
                    new_sub = '{}g{:05d}'.format(PREFIX, int(gene_number))
                    renamed_value.append(new_sub)
                elif sub.startswith('t'):
                    sub = sub.replace('t', '')
                    renamed_value.append(sub)
                else:
                    renamed_value.append(sub)
            new_value = '.'.join(renamed_value)
            
            new_line += ID + '=' + new_value + ';'
        
        out_fhand.write(new_line + '\n')
                      
                    
def main():

    prot_path = './tokyo/augustus.hints.aa'
    nt_path = './tokyo/augustus.hints.codingseq'
    gff3_path= './sung/augustus.hints.gff3'
    
    renamed_prot_path = './tokyo/augustus.renamed.prot'
    renamed_nt_path = './tokyo/augustus.renamed.nt'
    renamed_gff3_path = './sung/NH1L.augustus.renamed.gff3'

    #parse_fasta(prot_path, renamed_prot_path)
    #parse_fasta(nt_path, renamed_nt_path)
    parse_gff(gff3_path, renamed_gff3_path)
  

if __name__ == '__main__':
    main()
