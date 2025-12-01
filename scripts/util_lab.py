# util_lab.py -- checagens e utilitários de segurança
import os
from pathlib import Path
import sys

LAB_DIR = Path.cwd() / "lab_files"

def ensure_lab_dir():
    if not LAB_DIR.exists():
        print(f"[i] Criando pasta de teste em: {LAB_DIR}")
        LAB_DIR.mkdir(parents=True, exist_ok=True)
    return LAB_DIR

def confirm_running():
    print("ATENÇÃO: Este é um ambiente de simulação. Só execute em uma VM isolada e com arquivos dummy.")
    ans = input("Digite 'YES' para confirmar que você está em ambiente seguro: ").strip()
    if ans != "YES":
        print("Confirmação não recebida. Abortando.")
        sys.exit(1)
