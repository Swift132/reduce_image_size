from PIL import Image
import os

def reduce_image_size(input_path, output_path, target_size_kb):
    # Abre a imagem
    image = Image.open(input_path)
    
    # Converte o tamanho desejado de KB para bytes
    target_size_bytes = target_size_kb * 1024
    
    # Começa com a qualidade máxima
    quality = 95
    
    # Reduz a qualidade até que o tamanho do arquivo seja menor ou igual ao tamanho desejado
    while True:
        # Salva a imagem com a qualidade atual
        image.save(output_path, format='JPEG', quality=quality)
        
        # Verifica o tamanho do arquivo
        if os.path.getsize(output_path) <= target_size_bytes or quality <= 10:
            break
        
        # Reduz a qualidade
        quality -= 5

    print(f"Imagem salva em {output_path} com qualidade {quality}")

def process_images_in_folder(input_folder, output_folder, target_size_kb):
    # Certifica-se de que a pasta de saída existe
    os.makedirs(output_folder, exist_ok=True)
    
    # Percorre todos os ficheiros na pasta de entrada
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        
        # Verifica se o ficheiro é uma imagem JPEG
        if input_path.lower().endswith(('.jpg', '.jpeg')):
            output_path = os.path.join(output_folder, filename)
            reduce_image_size(input_path, output_path, target_size_kb)

# Caminho para o diretório de input
input_folder = 'caminho/para/sua/pasta_de_entrada'
# Caminho para o diretório de input
output_folder = 'caminho/para/sua/pasta_de_saida'
# Tamanho output em KB
target_size_kb = 500

# Processa todas as imagens na pasta
process_images_in_folder(input_folder, output_folder, target_size_kb)
