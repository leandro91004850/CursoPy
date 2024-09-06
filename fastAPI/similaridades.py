from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

# Definir duas frases
frase1 = "Devemos proteger o ambiente"
frase2 = "Temos proteger o meio ambiente"

# Carregar o tokenizer e o modelo BERT
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Tokenizar as frases
tokens_frase1 = tokenizer(frase1, return_tensors='pt')
tokens_frase2 = tokenizer(frase2, return_tensors='pt')

# Obter os embeddings das frases
with torch.no_grad():
    embeddings_frase1 = model(**tokens_frase1).last_hidden_state.mean(dim=1)
    embeddings_frase2 = model(**tokens_frase2).last_hidden_state.mean(dim=1)

# Calcular a similaridade de cosseno
similaridade = cosine_similarity(embeddings_frase1, embeddings_frase2)

# calcula a similaridade entre as duas frases variando de 0 (sem similaridade) a 1 (máxima similaridade).
# similaridade ideal acima de 0.93
if similaridade[0][0] > 0.93:
    print(f"A similaridade entre as frases é: {similaridade[0][0]:.2f} - Frases são similares")
else:
    print(f"A similaridade entre as frases é: {similaridade[0][0]:.2f} - Frases não são similares")
