#!/usr/bin/env python
# coding: utf-8

# In[77]:


import os
from duneapi.api import DuneAPI
from duneapi.types import Network, QueryParameter, DuneRecord, DuneQuery
from duneapi.util import open_query

def fetch_records(dune: DuneAPI) -> list[DuneRecord]:
    sample_query = DuneQuery.from_environment(
        #the sql query and return 10 record
        raw_sql='select name,abi,address from ethereum."contracts" limit 10;',
        #the dune name
        name="name",
        network=Network.MAINNET,

    )
    return dune.fetch(sample_query)


if __name__ == "__main__":
    #input username, password, and query id
    os.environ.setdefault("DUNE_USER", "albert123")
    os.environ.setdefault("DUNE_PASSWORD", "88888888")
    os.environ.setdefault("DUNE_QUERY_ID", "887999")
    
    dune_connection = DuneAPI.new_from_environment()
    records = fetch_records(dune_connection)
    print("First result:", records[0])


# In[78]:


import time
start = time.time()
for i in range(len(records)):  
    #get abi from dune and save in txt file
    print('abi:',str(df['abi'][i]),file=f)
    #get contract address from dune and save in txt file
    print('contract_adress:',str(df['address'][i]),file=f)
    #get name from dune and save in txt file
    print('name:',str(df['name'][i]),file=f)
    print('----------------------------',file=f)

#cost time:0.006s, 10 records
end = time.time()
print ("time is: ",str(end-start))


# In[ ]:




