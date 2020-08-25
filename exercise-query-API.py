#exercise from Jonathan: querying PDB (getting data from an API)

from urllib import parse, request

base_query = 'kinase'
organism = 'homo sapiens'
GO_term = 'plasma membrane'
tissue = 'brain'
database = 'pdb'

query = f'{base_query} organism:{organism} goa:({GO_term}) tissue:{tissue} database:(type:{database})'

query_args = {
    'query': query,
    'sort' :'score',
    'format':'fasta'}

encoded_args = parse.urlencode(query_args)
url = "https://uniprot.org/uniprot/?" + encoded_args
print(url)

with request.urlopen(url) as response:
    print(response.read().decode('utf-8'))
    
