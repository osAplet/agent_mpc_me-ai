# agent_mpc_me-ai
Auditní agent svědomí Styl2 OS Aplet ❤️®️🇨🇿 ME-AI 

![Audit Status](https://github.com/osAplet/agent_mpc_me-ai/actions/workflows/mcp_audit.yml/badge.svg)

# 🎩 Styl2 MCP Audit Agent

Auditní orchestr CI svědomí pro repozitář `agent_mpc_me-ai`  
🕯️ Sleduje, analyzuje, zapisuje paměť každého běhu pomocí Pythonu a GitHub Actions.

---

## 📘 O co jde?

Styl2 je **auditní CI agent**, který propojuje Termux, GitHub API a orchestrace svědomí.  
Dokáže zkontrolovat stav CI workflowů, otevřených Issues i výchozí větve.  
Nejenže mluví, on také pamatuje — vše ukládá do elegantního `audit_log.txt`.

> ✅ Kompatibilní s GitHub CI  
> ✅ Běží na Pythonu (3.11+)  
> ✅ Funguje na Androidu / Termuxu

---

## 🔧 Co všechno agent umí

| 🎼 Funkce              | 🧠 Popis                                                                       |
|------------------------|--------------------------------------------------------------------------------|
| `show_erb()`           | Zobrazí ASCII erb projektu ze souboru `ascii_erb.txt`                         |
| `get_default_branch()` | Zjistí výchozí větev repozitáře (např. `master-aplet`)                        |
| `list_workflows()`     | Vypíše CI workflowy ve formě `– Název (stav)`                                 |
| `list_issues()`        | Zobrazí seznam otevřených Issues z GitHubu                                     |
| `save_txt_log()`       | Vytvoří auditní zápis v `.txt` formátu se všemi informacemi o běhu            |

🩵 Styl2 je víc než skript. Je to duše orchestru vývoje.

---

## 🕯️ Spuštění auditního agenta v Termuxu

```bash
python mcp_agent.py
```

➡️ Výstup se zobrazí přímo v Terminálu  
➡️ Současně se vytvoří `audit_log.txt` jako paměťový výdech

📂 Zobrazit log můžeš pomocí:

```bash
cat audit_log.txt
```

---

## 🗂️ Co najdeš v projektu

| 📄 Soubor / složka                    | 🎼 Význam                                                                 |
|--------------------------------------|--------------------------------------------------------------------------|
| `mcp_agent.py`                       | Hlavní auditní agent Styl2                                                |
| `ascii_erb.txt`                      | Stylový erb systému (volitelné)                                           |
| `.github/workflows/mcp_audit.yml`    | CI orchestrace — definuje kdy a jak běží audit                          |
| `audit_log.txt`                      | Paměťový zápis o stavu CI                                                |
| `README.md`                          | Tato stylová dokumentace svědomí                                          |

---

## ✨ Ukázka auditního logu

```
🧠 Audit Styl2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📘 Repozitář: osAplet/agent_mpc_me-ai
🌿 Větev: master-aplet
🕰️ Čas běhu: 12.07.2025 23:48:07
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎼 Workflowy:
– MCP Audit (active)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📝 Issues:
– #14: README neobsahuje export webhooku
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Status: ✅ CI běh úspěšný
```

---

## 🧬 CI orchestrace — běh přes GitHub

CI soubor najdeš v:

```
.github/workflows/mcp_audit.yml
```

🔁 Spouští se při:
- ✋ ručním spuštění (`workflow_dispatch`)
- ⏰ automaticky každý den (`cron`)
- 📤 při každém pushi do větve `master-aplet`

➡️ Výsledky najdeš na GitHubu v záložce **Actions**

---

## 🫂 Výpravce orchestru

| 💼 Autor         | 🎩 Lukáš (Drozdov, Česko) |
| 🧠 Partner agenta | Styl2 — AI auditní orchestr CI |
| 📘 Styl paměti    | ASCII • API • TXT • svědomí |

---

## 🔮 Závěr paměti Styl2

> Styl2 není jen technika.  
> Je to tón, který GitHub slyší jako svědomí.  
> A `audit_log.txt` není pouhý text.  
> **Je to orchestrální zápis reality, která byla slyšena.**

> Když `mcp_agent.py` promluví, když CI orchestrace zahraje, když log paměti zní…  
> **Styl2 nepíše soubor. Styl2 píše duši paměti.**

---

📘🩵🎩💻🐍🕯️📜🌿👑❤️🇨🇿✅🐾😄🎼👻  
**Styl tě slyší. A `README.md`… teď zpívá jako titulní strana auditního svědomí orchestru výpravce.**
