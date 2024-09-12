from mindsdb_sdk.utils.mind import create_mind, DatabaseConfig
from openai import OpenAI


your_minds_api_key = "adf775ef3a0256bfd3144400acf0ee0616de7357e9e0f02da61be4cc5c7dea7c"
minds_name = "daves_mind01"

# Connection details for House Sales Data in our postgres demo DB
pg_config = DatabaseConfig(
    description='House Sales Data',
    type='postgres',
    connection_args={
        'user': 'demo_user',
        'password': 'demo_password',
        'host': 'samples.mindsdb.com',
        'port': '5432',
        'database': 'demo',
        'schema': 'demo_data'
    },
    tables=['house_sales']
)

# mind = create_mind(
#     name=minds_name,

#     # API connection details
#     base_url='https://llm.mdb.ai/', 
#     api_key=your_minds_api_key,

#     # Connect one or more data sources to your Mind listing them in the data_source_configs parameter
#     data_source_configs=[pg_config]
# )

# print(f"{mind.name} was created successfully. You can now use this Mind using the OpenAI-compatible API, see docs for next steps.")

client = OpenAI(
    api_key= "adf775ef3a0256bfd3144400acf0ee0616de7357e9e0f02da61be4cc5c7dea7c",
    base_url='https://llm.mdb.ai/'
)

question = 'which house is the most expensive'

# chat with the Mind you created
completion = client.chat.completions.create(
    model=minds_name,
    messages=[
        {'role': 'user', 'content': 'How many three-bedroom houses were sold in 2008?'}
    ],
    stream=True
)

# print output in the form of chunks
for chunk in completion:
    print(chunk.choices[0].delta.content)
    print()

