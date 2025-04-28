# Ajuste de Ponto Automático 📅🚀

Bem-vindo ao **AjustePontoBot**! Este projeto foi criado para **automatizar o preenchimento de ajustes de ponto** na plataforma [Oitchau](https://admin.oitchau.com.br/punches/), de forma segura, rápida e prática.

> **Aviso Legal:** Este projeto é fornecido "como está". **Você é integralmente responsável** por seu uso. Não me responsabilizo por quaisquer danos, perdas ou problemas causados direta ou indiretamente pelo uso deste software.

---

## 🔹 Sobre o Projeto

Este bot usa **Selenium** para:
- Abrir seu navegador Chrome.
- Reutilizar sua sessão já logada.
- Preencher datas e horários de ajustes de ponto automaticamente.
- Confirmar os registros de forma segura.

---

## 🔹 Requisitos para Rodar

### 📅 Antes de Começar
- **Você precisa estar já logado** no sistema Oitchau no Chrome.
- **O navegador Chrome deve estar fechado** antes de rodar o script.

### 🔧 Instalando o Ambiente

#### 1. Instale o Chocolatey (caso não tenha):

Abra o **PowerShell como administrador** e rode:

```bash
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iwr https://community.chocolatey.org/install.ps1 -UseBasicParsing | iex
```

#### 2. Instale o Python 3.11 pelo Chocolatey:

```bash
choco install python --version=3.11.7 -y
```

#### 3. Atualize o pip:

```bash
python -m pip install --upgrade pip
```

#### 4. Instale o Selenium:

```bash
pip install selenium
```

#### 5. Certifique-se que o ChromeDriver será gerenciado automaticamente pelo Selenium (versão 4.6+).

Não é preciso instalar o `chromedriver` manualmente.

---

## 🔹 Como Executar o Projeto

1. Feche seu navegador Chrome.
2. No terminal/powershell, navegue até a pasta do projeto:

```bash
cd caminho/da/pasta/do/projeto
```

3. Execute o script:

```bash
python ajuste_ponto.py
```

4. O terminal irá perguntar:

```plaintext
Digite os dias separados por vírgula (ex: 10,12,13):
```

Exemplo de entrada:

```plaintext
14,15,16
```

5. O bot irá abrir o navegador, usar sua sessão logada e registrar todos os ajustes de ponto para os dias informados.

---

## 🔹 Considerações Importantes

- 📦 **Verifique se você está realmente logado** no sistema Oitchau antes de rodar.
- 🔐 **Não abra o Chrome** enquanto o script estiver rodando.
- 🚫 **Não modifique o script se não tiver certeza** do que está fazendo.
- 🔧 **Atualize seu Chrome** para a última versão para evitar incompatibilidades.

---

## 📈 Melhorias Futuras (Planejado)
- Interface com calendário gráfico para selecionar os dias.
- Captura de tela automática de cada ajuste.
- Geração de relatórios de ajustes feitos.

---

> **Feito para facilitar seu dia! Use com responsabilidade!** 🚀

---

## 🌐 Contato

Este é um projeto aberto e sem garantias.
Utilize, modifique e melhore como desejar! 😉
