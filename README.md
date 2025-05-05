# Ajuste de Ponto Automation 🎯

Automação Selenium para realizar ajustes de ponto no sistema [OiTchau](https://admin.oitchau.com.br/punches/).

## ⚙️ Descrição

Este script Python abre o navegador Chrome no perfil do usuário para manter a sessão já autenticada e:
- Navega até o módulo de **Ajuste de Ponto**.
- Insere data, hora, tipo, localização e motivo.
- Confirma o lançamento de pontos de entrada, intervalos e saída.

## 🛑 Aviso

**Uso por sua conta e risco.**  
Não nos responsabilizamos por qualquer uso indevido, bloqueios ou alterações de dados.  

## 🚀 Pré-requisitos

1. Google Chrome instalado (versão compatível com Chromedriver 136.x).  
2. Python 3.13+.  
3. Selenium:
   ```bash
   pip install selenium
   ```
4. Chromedriver em `C:\chromedriver-win64\chromedriver.exe`.  
5. Perfil Chrome preparado em `C:\selenium\profile`.

## 📦 Instalação

1. Clone este repositório:
   ```bash
   git clone <url-do-repo>
   cd <repo>
   ```
2. Verifique se o **chromedriver.exe** está em `C:\chromedriver-win64\`.  
3. Abra o Chrome usando este perfil:
   ```bash
   "C:\Program Files\Google\Chrome\Application\chrome.exe" --user-data-dir="C:\selenium\profile"
   ```
   Faça login em `admin.oitchau.com.br`, feche o navegador.

## 🎯 Como usar

```bash
python ajuste_ponto.py
```
- Insira os dias desejados (ex: `1,2,10`).  
- O bot fará todos os lançamentos automaticamente.  

## 🔧 Configurações

- **`profile_dir`** no construtor do bot: caminho para o diretório de perfil.  
- **`executable_path`** em `Service`: caminho para `chromedriver.exe`.  

## 📄 Licença

MIT License
