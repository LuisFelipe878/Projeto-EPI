from PIL import Image

# Caminho da imagem de teste
caminho = "data/images/teste.jpg"

# Abre a imagem
imagem = Image.open(caminho)

# Mostra algumas informações
print("================================")
print("          PROJETO-EPI")
print("================================")
print(f"Imagem: {caminho}")
print(f"Tamanho: {imagem.size}")
print("Imagem carregada com sucesso!")
