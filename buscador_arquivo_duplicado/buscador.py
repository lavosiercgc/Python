import os
import hashlib
from collections import defaultdict

def calcular_hash(caminho_arquivo, bloco_tamanho=65536):
    """Gera o hash SHA-256 de um arquivo em partes para evitar uso excessivo de memória."""
    sha256 = hashlib.sha256()
    try:
        with open(caminho_arquivo, 'rb') as f:
            while bloco := f.read(bloco_tamanho):
                sha256.update(bloco)
        return sha256.hexdigest()
    except (PermissionError, FileNotFoundError):
        # Ignora arquivos do sistema trancados ou sem permissão de leitura
        return None

def encontrar_duplicados(diretorio):
    tamanhos = defaultdict(list)
    duplicados = defaultdict(list)

    print("Mapeando tamanhos dos arquivos...")
    # Passo 1: Agrupa os arquivos apenas pelo tamanho em bytes
    for raiz, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            caminho_completo = os.path.join(raiz, arquivo)
            try:
                tamanho = os.path.getsize(caminho_completo)
                tamanhos[tamanho].append(caminho_completo)
            except (PermissionError, FileNotFoundError):
                continue

    print("Verificando hashes de arquivos com tamanhos idênticos...")
    # Passo 2: Calcula o hash apenas para tamanhos que possuem mais de um arquivo
    for tamanho, caminhos in tamanhos.items():
        if len(caminhos) > 1:
            hashes_locais = defaultdict(list)
            for caminho in caminhos:
                hash_arquivo = calcular_hash(caminho)
                if hash_arquivo:
                    hashes_locais[hash_arquivo].append(caminho)
            
            # Se o mesmo hash aparecer mais de uma vez, temos duplicados
            for hash_val, lista_arquivos in hashes_locais.items():
                if len(lista_arquivos) > 1:
                    duplicados[hash_val].extend(lista_arquivos)

    return duplicados

if __name__ == "__main__":
    # COLOQUE AQUI O CAMINHO DA PASTA QUE DESEJA ANALISAR
    # Exemplo no Windows: "C:\\Users\\SeuUsuario\\Pictures"
    # Exemplo no Linux/Mac: "/home/usuario/documentos"
    #pasta_raiz = r"C:\Caminho\Para\Sua\Pasta"
    pasta_raiz = r"C:\Users\admin\Downloads"

    resultado = encontrar_duplicados(pasta_raiz)

    if not resultado:
        print("\nNenhum arquivo duplicado foi encontrado!")
    else:
        print(f"\nForam encontrados {len(resultado)} grupos de arquivos duplicados:\n")
        for i, (hash_id, caminhos) in enumerate(resultado.items(), start=1):
            print(f"Grupo {i} (Hash: {hash_id[:10]}...):")
            for caminho in caminhos:
                print(f"  -> {caminho}")
            print("-" * 50)
