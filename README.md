# Documentação do Script de Desinstalação do Maestro

Este script é responsável por desinstalar as versões do software Maestro (Maestro BPM, Maestro ERP, Maestro MCA, Maestro Nest) presentes no sistema. Ele busca os diretórios onde os produtos do Maestro podem estar instalados, exclui os arquivos e pastas encontradas, e registra a remoção em um arquivo de log.

## Funcionalidades

1. **Busca por diretórios de instalação do Maestro**: O script verifica os diretórios padrão onde os produtos Maestro podem estar instalados.
2. **Exclusão de arquivos**: O script percorre os diretórios encontrados e exclui todos os arquivos e subpastas dentro deles.
3. **Registro de remoção**: Caso a remoção de arquivos seja realizada com sucesso, a mensagem "Maestro removido com sucesso" é registrada no arquivo de log.
4. **Logs**: O arquivo de log é armazenado em `C:\Windows\Temp\Maestro_Uninstall_Log.txt`.

## Estrutura do Código

### 1. Importação de Bibliotecas

```python
import os
import shutil
import time
```
Essas bibliotecas são usadas para manipulação de arquivos e diretórios:
- **`os`**: Para verificar a existência de diretórios e manipulação de arquivos.
- **`shutil`**: Para remover arquivos e pastas.
- **`time`**: Para registrar a data e hora da remoção no log.

### 2. Variáveis de Configuração

#### Caminhos dos produtos Maestro

```python
maestro_paths = [
    r"C:\Program Files\Maestro BPM",
    r"C:\Program Files (x86)\Maestro BPM",
    r"C:\Users\Public\Maestro BPM",
    r"C:\Program Files\Maestro ERP",
    r"C:\Program Files (x86)\Maestro ERP",
    r"C:\Users\Public\Maestro ERP",
    r"C:\Program Files\Maestro MCA",
    r"C:\Program Files (x86)\Maestro MCA",
    r"C:\Users\Public\Maestro MCA",
    r"C:\Program Files\Maestro Nest",
    r"C:\Program Files (x86)\Maestro Nest",
    r"C:\Users\Public\Maestro Nest"
]
```

Esses são os diretórios onde o script procurará pelos produtos Maestro instalados. A lista abrange várias localizações possíveis, tanto para sistemas de 32 bits quanto para 64 bits, além de pastas públicas.

#### Caminho do arquivo de log

```python
log_path = r"C:\Windows\Temp\Maestro_Uninstall_Log.txt"
```

Este é o caminho do arquivo de log onde a remoção do Maestro será registrada, caso a remoção seja bem-sucedida.

### 3. Funções

#### `log_remocao()`

```python
def log_remocao():
    """Registra apenas a mensagem 'Maestro removido com sucesso' no arquivo de log"""
    try:
        with open(log_path, "a") as log_file:
            log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Maestro removido com sucesso\n")
        print("Maestro removido com sucesso")  # Exibe no terminal
    except Exception:
        pass  # Ignora erros ao gravar no log
```

Função responsável por registrar no arquivo de log que o Maestro foi removido com sucesso, incluindo a data e a hora da remoção. Caso ocorra algum erro durante a gravação no log, ele é ignorado.

#### `excluir_arquivos(diretorio)`

```python
def excluir_arquivos(diretorio):
    """Exclui todos os arquivos e pastas dentro do diretório fornecido"""
    removido = False
    for root, dirs, files in os.walk(diretorio, topdown=False):
        for name in files:
            try:
                os.remove(os.path.join(root, name))
                removido = True
            except Exception:
                pass
        for name in dirs:
            try:
                shutil.rmtree(os.path.join(root, name))
                removido = True
            except Exception:
                pass
    return removido
```

Essa função percorre o diretório fornecido, removendo todos os arquivos e pastas dentro dele. Ela retorna `True` se algum arquivo ou pasta foi removido com sucesso, caso contrário, retorna `False`.

#### `desinstalar_maestro()`

```python
def desinstalar_maestro():
    """Desinstala todas as versões do Maestro encontradas"""
    algo_removido = False
    for path in maestro_paths:
        if os.path.exists(path):
            if excluir_arquivos(path):
                algo_removido = True

    if algo_removido:
        log_remocao()
    else:
        print("Nenhuma versão do Maestro encontrada.")  # Não cria log
```

Esta função verifica se algum dos diretórios padrão contém produtos Maestro instalados e, caso encontre, chama a função `excluir_arquivos()` para excluir os arquivos. Se ao menos um diretório foi removido, a função `log_remocao()` é chamada para registrar a remoção. Caso nenhum produto Maestro seja encontrado, uma mensagem é exibida no terminal.

### 4. Execução do Script

```python
if __name__ == "__main__":
    desinstalar_maestro()
```

Esta linha garante que o script será executado apenas quando for chamado diretamente (não quando importado como módulo). Ela chama a função `desinstalar_maestro()` para iniciar o processo de desinstalação.

## Uso

1. **Executar o script**: Basta executar o script em um ambiente Python. Ele tentará localizar as instalações do Maestro e removê-las, além de registrar a remoção no arquivo de log.
2. **Verificar o log**: Após a execução, o arquivo de log `C:\Windows\Temp\Maestro_Uninstall_Log.txt` pode ser verificado para confirmar as remoções realizadas.

## Possíveis Melhorias

- **Tratamento de erros mais robusto**: Em caso de falhas na exclusão de arquivos ou gravação no log, o script pode registrar mais informações sobre o erro.
- **Verificação adicional**: O script pode ser modificado para verificar outras localizações ou realizar verificações de permissão antes de tentar excluir arquivos.

## Conclusão

Esse script foi projetado para facilitar a remoção das versões do Maestro e garantir que o processo seja registrado de forma simples.
