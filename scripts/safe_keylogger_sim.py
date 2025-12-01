# safe_keylogger_sim.py -- simulação de keylogger (NÃO intercepta teclado do sistema)
from pathlib import Path
from util_lab import ensure_lab_dir, confirm_running
import time

SIM_INPUT = "simulated_input.txt"   # o usuário cria este arquivo com 'keystrokes' simuladas

def run_simulation():
    lab = ensure_lab_dir()
    confirm_running()
    simfile = lab / SIM_INPUT
    if not simfile.exists():
        print(f"[!] Arquivo de entrada simulado não encontrado: {simfile}")
        print("Crie o arquivo com conteúdo de exemplo para simular teclas.")
        return
    log = lab / "captured_log.txt"
    with simfile.open("r", encoding="utf-8") as src, log.open("a", encoding="utf-8") as dst:
        for line in src:
            # cada linha simula uma sequência de teclas ocorrida num timestamp
            ts = time.strftime("%Y-%m-%d %H:%M:%S")
            dst.write(f"{ts} | {line.rstrip()}\\n")
    print(f"[sim] Log escrito em: {log}")

if __name__ == "__main__":
    run_simulation()
