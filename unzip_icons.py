import zipfile
import os

# Caminho para o arquivo ZIP
zip_path = '/home/cooker/project/icons_ipma_weather.zip'

# Diretório de destino para os ícones
extract_path = '/home/cooker/project/meteo/static/meteo/icons'

# Criar o diretório de destino, se não existir
os.makedirs(extract_path, exist_ok=True)

# Descompactar o arquivo ZIP
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print(f"Ícones descompactados em: {extract_path}")
