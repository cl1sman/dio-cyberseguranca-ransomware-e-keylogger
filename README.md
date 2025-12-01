# Simulated Malware Lab — README

**Aviso Legal e Ético**

Este repositório contém **simulações educativas** de comportamentos associados a malwares ("ransomware" e "keylogger") **apenas para fins de aprendizagem** em um ambiente controlado. **NÃO** execute os scripts em máquinas de produção, nem os use para atividades não autorizadas. Use máquinas virtuais isoladas (air-gapped quando possível), snapshots e arquivos de teste (dummy files). Ao usar estes materiais, você concorda em seguir boas práticas éticas e legais.

---

## Objetivo do Projeto

Demonstrar, de forma segura e controlada, os princípios de funcionamento de:

* **Ransomware (simulado)** — processo de 'sequestro' de arquivos de teste dentro de uma pasta dedicada; criação de cópias de backup antes da simulação; geração de mensagem de resgate; e restauração a partir do backup.
* **Keylogger (simulado)** — simulação de captura de teclas a partir de um arquivo de entradas pré-gravadas (não captura eventos do sistema). A ideia é demonstrar fluxos de dados, armazenamento e exfiltração (simulada localmente).

Também documentamos estratégias de defesa, detecção e mitigação.

---

## Estrutura do Repositório

```
/ (repo root)
├─ README.md                     # este arquivo
├─ /scripts
│  ├─ safe_ransom_sim.py         # simulação segura do ransomware
│  ├─ safe_keylogger_sim.py      # simulação segura do keylogger
│  └─ util_lab.py                # utilitários (checagens de ambiente, confirmação)
├─ /lab_files                    # pasta onde você cria os arquivos de teste (não comitar arquivos sensíveis)
│  ├─ sample1.txt
│  └─ sample2.txt
├─ /images                       # capturas de tela (opcional)
└─ LICENSE
```

---

## Requisitos e Ambiente Seguro

1. **Máquina Virtual (recomendado):** use VirtualBox/VMware (snapshot antes de executar).
2. **Isolamento de Rede:** execute sem acesso à internet se for testar partes que simulam exfiltração.
3. **Usuário e Pasta de Teste:** execute os scripts apenas dentro de `./lab_files` e crie somente arquivos dummy (ex.: `*.txt` com conteúdo não-sensível).
4. **Dependências:** Python 3.10+ (nenhuma biblioteca de terceiros obrigatória para as simulações seguras). Use um venv.

---

## Como executar (resumo)

1. Crie/clone o repositório em uma VM isolada.
2. Prepare a pasta `lab_files` com alguns arquivos de texto dummy.
3. Execute `python3 scripts/safe_ransom_sim.py` — o script pedirá confirmação explicita (digite `YES` para prosseguir) e criará backups antes de simular a 'encriptação' (substituição por marcador) e mostrará a mensagem de resgate.
4. Para restaurar, execute o mesmo script com a opção de restauração ou siga as instruções do script.
5. Execute `python3 scripts/safe_keylogger_sim.py` — ele lerá um arquivo `simulated_input.txt` (pré-gravado) e imprimirá/escreverá um log local sem enviar nada pela rede.

---

## Conteúdo pedagógico (o que documentar no repositório)

* Explicação passo-a-passo do que cada script faz e *por que* cada etapa existe.
* Logs de execução (screencaptures) na pasta `/images` com timestamps.
* Reflexão sobre técnicas reais usadas por malwares e como as versões simuladas simplificam/omitiram partes perigosas (ex.: persistência, evasão, comunicação C2, uso de criptografia real).
* Seções: "Detecção e Monitoramento", "Mitigação e Resposta", "Boas Práticas".

---

## Medidas de Defesa (resumo rápido)

* Backup regular e offline
* Aplicar patches e reduzir superfície de ataque
* EDR / AV moderno com heurística e análise comportamental
* Segmentação de rede e políticas de privilégio mínimo
* Treinamento e conscientização de usuários
* Sandboxing e análise em ambientes controlados

---

## Licença

Adote uma licença permissiva (ex.: MIT) e inclua um `LICENSE` que reforce o uso ético.