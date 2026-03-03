# 📄 OCR Pipeline - Extração de Texto

Sistema profissional de OCR (Optical Character Recognition) para extração de texto de imagens e PDFs, com interface gráfica moderna.

![Python](https://img.shields.io/badge/python-3.12+-blue.svg)
![Flet](https://img.shields.io/badge/flet-0.81.0-purple.svg)
![Tesseract](https://img.shields.io/badge/tesseract-OCR-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📋 Índice

- [Características](#-características)
- [Instalação Windows](#-instalação-windows)
- [Instalação Linux](#-instalação-linux)
- [Como Usar](#-como-usar)
- [Formatos Suportados](#-formatos-suportados)
- [Troubleshooting](#-troubleshooting)
- [Arquitetura](#-arquitetura)

## ✨ Características

- 🎨 **Interface moderna** com Flet (Material Design)
- 🌙 **Tema escuro** profissional
- 📊 **Barra de progresso** em tempo real
- 📝 **Log colorido** por tipo de mensagem
- 🗂️ **Processamento em lote** de múltiplos arquivos
- 📁 **Arquivos individuais** - Cada arquivo gera seu próprio `.md`
- 🧹 **Limpeza automática** de texto
- ⚡ **Multi-threading** - Não trava a interface

## 🪟 Instalação Windows

### Passo 1: Instalar Python 3.12+

1. **Baixar Python**
   - Acesse: https://www.python.org/downloads/
   - Baixe Python 3.12 ou superior

2. **Instalar**
   - Execute o instalador
   - ✅ **IMPORTANTE:** Marque "Add Python to PATH"
   - Clique em "Install Now"

3. **Verificar**
   ```powershell
   python --version
   # Saída: Python 3.12.x
   ```

### Passo 2: Instalar Tesseract OCR

**Opção A: Via Chocolatey (Recomendado)**
```powershell
# Instalar Chocolatey (se não tiver)
# Executar PowerShell como Administrador
Set-ExecutionPolicy Bypass -Scope Process -Force
iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# Instalar Tesseract
choco install tesseract
```

**Opção B: Instalador Manual**
1. Baixe: https://github.com/UB-Mannheim/tesseract/wiki
2. Execute `tesseract-ocr-w64-setup-5.x.x.exe`
3. Instale em: `C:\Program Files\Tesseract-OCR`
4. Adicione ao PATH:
   - Windows + R → `sysdm.cpl` → Enter
   - Aba "Avançado" → "Variáveis de Ambiente"
   - Edite "Path" → Novo → `C:\Program Files\Tesseract-OCR`
   - OK → OK → Reinicie o terminal

**Verificar:**
```powershell
tesseract --version
# Saída: tesseract 5.x.x
```

### Passo 3: Instalar Pacote Português

**Automático (Chocolatey):**
```powershell
choco install tesseract-lang-por
```

**Manual:**
1. Baixe: https://github.com/tesseract-ocr/tessdata_best/raw/main/por.traineddata
2. Copie para: `C:\Program Files\Tesseract-OCR\tessdata\`
3. Verifique: `tesseract --list-langs` (deve mostrar "por")

### Passo 4: Configurar Projeto

```powershell
# Baixar projeto
git clone <url-do-repositorio>
cd OCR

# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual
.venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Executar
python main.py
```

## 🐧 Instalação Linux

### Ubuntu/Debian

```bash
# Instalar dependências do sistema
sudo apt-get update
sudo apt-get install -y tesseract-ocr tesseract-ocr-por python3.12 python3.12-venv git

# Baixar projeto
git clone <url-do-repositorio>
cd OCR

# Criar ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependências Python
pip install -r requirements.txt

# Executar
python main.py
```

### Outras Distribuições

**Fedora/RHEL:**
```bash
sudo dnf install tesseract tesseract-langpack-por python3 python3-pip
```

**Arch Linux:**
```bash
sudo pacman -S tesseract tesseract-data-por python python-pip
```

## 🚀 Como Usar

### Passo a Passo

1. **Abrir Aplicação**
   ```bash
   python main.py
   ```

2. **Selecionar Diretório**
   - Clique em "📁 Selecionar Diretório"
   - Escolha a pasta com seus arquivos

3. **Verificar Arquivos**
   - Lista mostra todos os arquivos detectados
   - Ícones coloridos indicam o tipo (PDF ou Imagem)

4. **Processar**
   - Clique em "▶ Processar Arquivos"
   - Acompanhe o progresso em tempo real
   - Veja o log detalhado

5. **Resultado**
   - Arquivos `.md` criados no mesmo diretório
   - Um arquivo para cada documento processado

### Exemplo de Uso

**Antes do processamento:**
```
meus_documentos/
├── contrato.pdf
├── relatorio.pdf
└── foto.jpg
```

**Depois do processamento:**
```
meus_documentos/
├── contrato.pdf
├── contrato.md       ← ✓ Texto extraído
├── relatorio.pdf
├── relatorio.md      ← ✓ Texto extraído
├── foto.jpg
└── foto.md           ← ✓ Texto extraído
```

### Formato do Arquivo .md

```markdown
# contrato.pdf

**Extraído em:** 03/03/2026 11:15:30

---

[Texto limpo e formatado extraído do documento]
```

## 🔍 Formatos Suportados

| Formato | Extensão | Tipo |
|---------|----------|------|
| PNG | `.png` | Imagem |
| JPEG | `.jpg`, `.jpeg` | Imagem |
| GIF | `.gif` | Imagem |
| BMP | `.bmp` | Imagem |
| TIFF | `.tiff`, `.tif` | Imagem |
| WebP | `.webp` | Imagem |
| PDF | `.pdf` | Documento |

## 🎯 Limpeza de Texto

O sistema automaticamente:
- ✅ Remove caracteres de controle
- ✅ Elimina espaços extras
- ✅ Une palavras hifenizadas
- ✅ Corrige quebras de linha
- ✅ Normaliza pontuação
- ✅ Remove linhas vazias múltiplas

## 🐛 Troubleshooting

### 🪟 Windows

#### Erro: "tesseract is not installed"
```powershell
# Verificar instalação
tesseract --version

# Adicionar ao PATH manualmente
# Windows + R → sysdm.cpl → Variáveis de Ambiente
# Editar "Path" → Adicionar: C:\Program Files\Tesseract-OCR
# Reiniciar terminal
```

#### Erro: "python não é reconhecido"
```powershell
# Use 'py' ao invés de 'python'
py main.py

# Ou reinstale Python marcando "Add to PATH"
```

#### Erro: "Failed to load tessdata/por.traineddata"
```powershell
# Baixar pacote português
# https://github.com/tesseract-ocr/tessdata_best/raw/main/por.traineddata

# Copiar para:
# C:\Program Files\Tesseract-OCR\tessdata\
```

#### Erro: "No module named 'flet'"
```powershell
# Ativar ambiente virtual
.venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

#### Erro: "Scripts is disabled"
```powershell
# Executar como Administrador
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 🐧 Linux

#### Erro: "tesseract is not installed"
```bash
sudo apt-get install tesseract-ocr tesseract-ocr-por
tesseract --version
```

#### Erro: "ModuleNotFoundError"
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

#### Erro: "markitdown not found"
```bash
pip install markitdown
which markitdown
```

### 🔧 Problemas Comuns (Todas as Plataformas)

#### OCR não reconhece texto
- Use imagens com boa resolução (300+ DPI)
- Melhore o contraste da imagem
- Evite imagens borradas ou com ruído
- Verifique se o idioma está correto (português)

#### Processamento lento
- Processe em lotes menores (máximo 50 arquivos)
- Reduza resolução de imagens muito grandes
- Use SSD ao invés de HD

## 🎯 Criar Executável (.exe para Windows)

### Pré-requisitos

- Python 3.12+ instalado
- Projeto configurado (ambiente virtual + dependências)
- PyInstaller

### Passos para Criar o Executável

#### 🪟 Windows

1. **Ativar Ambiente Virtual**
   ```powershell
   .venv\Scripts\activate
   ```

2. **Instalar Dependências de Build**
   ```powershell
   pip install -r requirements-build.txt
   ```

3. **Executar Script de Build**
   ```powershell
   .\build.ps1
   ```

4. **Resultado**
   - Executável criado em: `dist\OCR_Pipeline.exe`
   - Tamanho aproximado: 80-120 MB
   - Pronto para distribuir!

#### 🐧 Linux

```bash
# Ativar ambiente virtual
source .venv/bin/activate

# Instalar dependências de build
pip install -r requirements-build.txt

# Executar script de build
./build.sh

# Resultado em: dist/OCR_Pipeline
```

### ⚠️ Importante para Distribuição

O executável **NÃO inclui** o Tesseract OCR. Usuários precisam:

1. **Instalar Tesseract OCR separadamente**
   ```powershell
   # Windows
   choco install tesseract
   
   # Ou download manual de:
   # https://github.com/UB-Mannheim/tesseract/wiki
   ```

2. **Instalar pacote de idioma português**
   ```powershell
   choco install tesseract-lang-por
   ```

3. **Adicionar Tesseract ao PATH** (se necessário)

### 📦 Distribuição

**Arquivos para distribuir:**
```
OCR_Pipeline/
├── OCR_Pipeline.exe         # Executável principal
└── README_DISTRIBUIÇÃO.txt  # Instruções para usuários
```

**README_DISTRIBUIÇÃO.txt deve conter:**
- Link para download do Tesseract
- Instruções de instalação do português
- Como adicionar ao PATH
- Como usar a aplicação

### 🔧 Build Personalizado

Para customizar o build, edite `build.spec`:

```python
# Adicionar ícone
icon='icone.ico'

# Incluir arquivos extras
datas=[('recursos/', 'recursos/')],

# Mudar nome
name='MeuOCR'
```

Depois execute:
```powershell
pyinstaller build.spec --clean
```

### 📊 Tamanhos Aproximados

| Plataforma | Tamanho do Executável |
|------------|----------------------|
| Windows 10/11 | 80-120 MB |
| Linux (Ubuntu) | 60-90 MB |

### ⚡ Build Otimizado (Menor Tamanho)

Para reduzir o tamanho do executável:

1. **Editar build.spec**
   ```python
   # Mudar para UPX máximo
   upx=True,
   upx_exclude=[],
   
   # Remover debug
   debug=False,
   ```

2. **Instalar UPX** (compressor)
   ```powershell
   # Windows
   choco install upx
   
   # Linux
   sudo apt-get install upx
   ```

3. **Rebuild**
   ```powershell
   .\build.ps1
   ```

### 🐛 Troubleshooting Build

#### Erro: "PyInstaller not found"
```powershell
pip install pyinstaller
```

#### Erro: "Module not found" no executável
```powershell
# Adicionar ao hiddenimports no build.spec
hiddenimports=[
    'flet',
    'pytesseract',
    'PIL',
    'seu_modulo_aqui',
],
```

#### Executável muito grande
```powershell
# Use UPX para comprimir
# Ou crie versão --onedir ao invés de --onefile
```

#### Erro: "Failed to execute script"
```powershell
# Build com console para ver erros
# Em build.spec: console=True
pyinstaller build.spec --clean
```

### Estrutura do Projeto

```
OCR/
├── main.py              # Core da aplicação
├── README.md            # Esta documentação
├── requirements.txt     # Dependências Python
├── LICENSE              # Licença MIT
└── .venv/              # Ambiente virtual (não versionado)
```

### Fluxo de Processamento

```
1. Seleção de Diretório
   ↓
2. Scan e Detecção de Arquivos
   ↓
3. Processamento Individual
   ├── Imagem → OCR (Tesseract) → PDF temporário → Texto
   └── PDF → Extração (markitdown) → Texto
   ↓
4. Limpeza de Texto (Regex)
   ↓
5. Salvar arquivo.md
```

### Tecnologias

| Componente | Tecnologia | Propósito |
|------------|-----------|-----------|
| Interface | Flet 0.81.0 | UI moderna e responsiva |
| OCR | Tesseract 5.x | Reconhecimento de texto |
| Python | 3.12+ | Linguagem principal |
| Processamento Imagem | Pillow | Conversão e manipulação |
| Extração PDF | markitdown | Extração de texto |
| Multi-threading | threading | Não travar interface |

## 📝 Dependências

```txt
flet==0.81.0          # Interface gráfica
pytesseract==0.3.13   # Wrapper Tesseract
Pillow==12.1.1        # Processamento de imagens
markitdown            # Extração de PDF
```

## 🔒 Segurança e Privacidade

- ✅ Processamento 100% local
- ✅ Nenhum dado enviado para internet
- ✅ Arquivos temporários automaticamente excluídos
- ✅ Open source e auditável

## 📈 Changelog

### v2.0.0 (2026-03-03)
- ✨ Refatoração completa do código
- ✨ Arquivo individual por documento
- ✨ main.py como core único
- ✨ Código profissional e limpo
- ✨ Documentação completa Windows/Linux

### v1.0.0 (2026-03-01)
- ✨ Interface gráfica com Flet
- ✨ Suporte a múltiplos formatos
- ✨ Processamento em lote
- ✨ Limpeza automática de texto

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🙏 Agradecimentos

- **Tesseract OCR** - Engine de OCR open source
- **Flet** - Framework Python para interfaces modernas
- **Markitdown** - Extração de texto de PDFs
- **Pillow** - Processamento de imagens

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📞 Suporte

Para problemas ou dúvidas:
- Consulte a seção [Troubleshooting](#-troubleshooting)
- Abra uma issue no repositório
- Verifique a documentação

---

**Desenvolvido com ❤️ para facilitar a extração de texto de documentos digitalizados.**

**Última atualização:** 03/03/2026
