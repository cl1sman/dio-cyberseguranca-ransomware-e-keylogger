# safe_ransom_sim.py -- simulação segura de comportamento de 'ransomware'
import argparse
from pathlib import Path
import shutil
import time
from util_lab import ensure_lab_dir, confirm_running

BACKUP_DIR_NAME = "backup_before_sim"

def simulate_encrypt(path: Path):
    # substitui o conteúdo por um marcador, mas antes faz backup
    for p in path.iterdir():
        if p.is_file():
            backup_path = path / BACKUP_DIR_NAME / p.name
            shutil.copy2(p, backup_path)
            # substituir conteúdo (SIMULA encriptação)
            p.write_text("[SIMULATED ENCRYPTED CONTENT]\n")
            print(f"[sim] '{p.name}' marcado como encriptado (simulado).")

def restore_from_backup(path: Path):
    bdir = path / BACKUP_DIR_NAME
    if not bdir.exists():
        print("[!] Backup não encontrado.")
        return
    for bp in bdir.iterdir():
        target = path / bp.name
        shutil.copy2(bp, target)
        print(f"[sim] Restaurado: {bp.name}")

def make_ransom_note(path: Path):
    note = path / "READ_ME_FOR_RESTORE.txt"
    note.write_text("This is a SIMULATED ransom note. No real encryption was performed.\n")
    print("[sim] Ransom note criada.")

def main():
    parser = argparse.ArgumentParser(description="Ransomware simulation (SAFE).")
    parser.add_argument("--restore", action="store_true", help="Restaurar arquivos do backup.")
    args = parser.parse_args()
    lab = ensure_lab_dir()
    # garantir pasta de backup
    (lab / BACKUP_DIR_NAME).mkdir(exist_ok=True)
    confirm_running()
    if args.restore:
        restore_from_backup(lab)
    else:
        simulate_encrypt(lab)
        make_ransom_note(lab)
        print("Simulação completa. Os arquivos foram marcados como ENCRYPTED (simulado).")

if __name__ == "__main__":
    main()
