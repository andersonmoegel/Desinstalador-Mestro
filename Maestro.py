import os
import shutil
import time

# Diretórios onde os produtos Maestro podem estar instalados
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

# Caminho para o arquivo de log
log_path = r"C:\Windows\Temp\Maestro_Uninstall_Log.txt"

def log_remocao():
    """Registra apenas a mensagem 'Maestro removido com sucesso' no arquivo de log"""
    try:
        with open(log_path, "a") as log_file:
            log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Maestro removido com sucesso\n")
        print("Maestro removido com sucesso")  # Exibe no terminal
    except Exception:
        pass  # Ignora erros ao gravar no log

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

if __name__ == "__main__":
    desinstalar_maestro()
