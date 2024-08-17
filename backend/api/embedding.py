from mistralai.client import MistralClient


class generate_embeddings:
    def __init__(self, api_key):
        self.client = MistralClient(api_key=api_key)
    
    def get_embeddings(self, text):
        embeddings_batch_response = self.client.embeddings(
            model="mistral-embed",
            input=[text],
        )
        return embeddings_batch_response.data[0].embedding
    