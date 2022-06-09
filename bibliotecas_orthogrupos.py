
def make_library(in_path_list, out_path):

    out_fhand = open(out_path, 'wt')

    ortho_dict = {}
    for in_path in in_path_list: 
        in_fhand = open(in_path, 'rt')
        
        for line in in_fhand:
            gene_id, orthogroup, ref_gene = line.strip().split('\t')[0:3]
            if orthogroup not in ortho_dict:
                ortho_dict[orthogroup] = {'ref_genes':[], 'gene_ids':[]}
            ortho_dict[orthogroup]['ref_genes'].append(ref_gene)
            ortho_dict[orthogroup]['gene_ids'].append(gene_id)
            
    return ortho_dict
    
            


def main():


    sung = './sung/proteinsNH1LMappedToGroups.txt'
    tokyo = './tokyo/proteinsTokyo1MappedToGroups.txt'
    valencia = './valencia/proteinsHYR1MappedToGroups.txt'
    
    library = './new_ortho_library'


    ortho_dict = make_library([sung, tokyo, valencia], library)
    
    for item in ortho_dict:
        genes = ortho_dict[item]['gene_ids']
        ref_genes = ortho_dict[item]['ref_genes']
        if len(genes) > 1:
            print(item, ref_genes)
            print(item, genes)


if __name__ == '__main__':
    main()
