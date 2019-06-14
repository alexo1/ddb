import sqlparse
from schema import fragment_schema
query="SELECT name, age FROM events WHERE status='open' AND etype='free'";

def preprocess_querry(querry_string):
    new_query=querry_string.strip("SELECT ")
    querry_representation  = {
        'projections': [], # fields to be projected
        'table': '', # tableto query from
        'filters':[] # filter
    }

    sql_tokens = sqlparse.parse(new_query)[0].tokens
    sql_tokens[0]
    refined_tokens =[]

    for token in sql_tokens:
        if token.value != ' ' and token.value != 'FROM':
            refined_tokens.append(token)

    
    for identifier in refined_tokens[0]:
        if identifier.value != ',' and identifier.value!=' ':
            querry_representation['projections'].append(identifier.value)

    querry_representation['table']=refined_tokens[1].value

    sql_tokens = []
    #import pdb; pdb.set_trace()
    for fiter in refined_tokens[2].tokens:
        if fiter.value !='WHERE' and fiter.value != ' ' and fiter.value!='AND':
            sql_tokens.append(fiter)


    querry_representation['filters']= [tok.value for tok in sql_tokens ]
    
    return querry_representation


def data_localization(query_rep):
    table_name = query_rep['table']
    table_fragments = fragment_schema[table_name]['fragments'] #array of fragments
    return [my_fragment for my_fragment in table_fragments if my_fragment['filter'] in query_rep['filters']]




query_rep=preprocess_querry(query)
fragment=data_localization(query_rep)