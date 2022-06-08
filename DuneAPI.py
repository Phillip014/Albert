#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install duneapi


# In[16]:


import os
from duneapi.api import DuneAPI
from duneapi.types import Network, QueryParameter, DuneRecord, DuneQuery
from duneapi.util import open_query



def fetch_records(dune: DuneAPI) -> list[DuneRecord]:
    sample_query = DuneQuery.from_environment(
        raw_sql='select name,abi,address from ethereum."contracts" limit 10;',
        name="name",
        network=Network.MAINNET,

    )
    return dune.fetch(sample_query)


if __name__ == "__main__":
    os.environ.setdefault("DUNE_USER", "albert123")
    os.environ.setdefault("DUNE_PASSWORD", "88888888")
    os.environ.setdefault("DUNE_QUERY_ID", "887999")
    
    dune_connection = DuneAPI.new_from_environment()
    records = fetch_records(dune_connection)
    print("First result:", records[0])
    print("Len:", len(records))


# In[74]:


import pandas as pd
df = pd.DataFrame(records)
f = open("output.txt", "a")
for i in range(len(records)):    
    print('abi:',str(df['abi'][i]))
    print('contract_adress:',str(df['address'][i]))
    print('name:',str(df['name'][i]))
    print('----------------------------')


# In[76]:


import time
start = time.time()
for i in range(len(records)):    
    print('abi:',str(df['abi'][i]),file=f)
    print('contract_adress:',str(df['address'][i]),file=f)
    print('name:',str(df['name'][i]),file=f)
    print('----------------------------',file=f)
end = time.time()
print ("time is: ",str(end-start))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




