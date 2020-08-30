#exercise from Jonathan: querying uniprot (getting data from an API)
#one day, it would be interesting to get user input at the command line to generate the query dynamically

from urllib import parse, request

#search terms of interest
base_query = 'kinase'
organism = 'homo sapiens'
GO_term = 'plasma membrane'
tissue = 'brain'
database = 'pdb'

#fancy pants f string to put everything in the right format for uniprot
query = f'{base_query} organism:{organism} goa:({GO_term}) tissue:{tissue} database:(type:{database})'

query_args = {
    'query': query,
    'sort' :'score',
    'format':'fasta'}


def query_uniprot(query_args):
    ''' This function takes the dictionary query_args,
    appends its contents to the Uniprot base URL,
    and retrieves and prints the query results'''
    
    encoded_args = parse.urlencode(query_args)
    url = "https://uniprot.org/uniprot/?" + encoded_args

    with request.urlopen(url) as response:
        print(response.read().decode('utf-8'))

def main(query_args):
    query_uniprot(query_args)

if __name__ == '__main__':
    main(query_args)
    
