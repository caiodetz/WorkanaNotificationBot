from PyInstaller.__main__ import run
import os

def build_executable(script_path, output_dir="dist", onefile=True, windowed=False, icon_path=None, additional_files=None):
    if not os.path.exists(script_path):
        print(f"Erro: O arquivo {script_path} não foi encontrado.")
        return

    args = [
        script_path,                     # Caminho do script
        f"--distpath={output_dir}",      # Diretório de saída
    ]

    if onefile:
        args.append("--onefile")
    if windowed:
        args.append("--console")
    if icon_path and os.path.exists(icon_path):
        args.append(f"--icon={icon_path}")
    if additional_files:
        for file_path in additional_files:
            if os.path.exists(file_path):
                args.append(f"--add-data={file_path}{os.pathsep}.")
            else:
                print(f"Aviso: O arquivo adicional {file_path} não foi encontrado e será ignorado.")

    try:
        run(args)
        print(f"Build concluído com sucesso! Executável criado em '{os.path.abspath(output_dir)}'.")
    except Exception as e:
        print(f"Erro ao criar o executável: {e}")

# Exemplo de uso
if __name__ == "__main__":
    script = "main.py"  # Substitua pelo caminho do seu script Python
    additional_files = ["notification.mp3"]  # Lista de arquivos adicionais
    build_executable(script, onefile=True, windowed=True, icon_path="icon.ico", additional_files=additional_files)
