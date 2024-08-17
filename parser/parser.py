from bs4 import BeautifulSoup 
import json 

from mistralai.client import MistralClient

client = MistralClient(api_key="INSERT_YOUR_API_KEY_HERE")

embeddings_batch_response = client.embeddings(
    model="mistral-embed",
    input=["Embed this sentence."],
)

print(embeddings_batch_response.data)

from bs4 import BeautifulSoup 

with open("kannada.html", 'r') as file:
    soup = BeautifulSoup(file.read(), "html.parser")


data = soup.findAll('script',  {"id" : "__NEXT_DATA__"})[0].text


json_parsed = json.loads(data)
json_dict = dict(json_parsed)

for movie in json_dict['props']['pageProps']['searchResults']['titleResults']['titleListItems']:
    print(movie.keys())



