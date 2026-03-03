# 📄 OCR Pipeline

> Extraia texto de imagens e PDFs com reconhecimento óptico de caracteres (OCR) em português.

![Python](https://img.shields.io/badge/python-3.12+-blue.svg)
![Flet](https://img.shields.io/badge/flet-0.81.0-purple.svg)
![Tesseract](https://img.shields.io/badge/tesseract-OCR-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey.svg)

## 🎯 Sobre o Projeto

**OCR Pipeline** é uma aplicação desktop com interface gráfica moderna que permite extrair texto de documentos digitalizados (imagens e PDFs) usando tecnologia OCR (Optical Character Recognition). Ideal para digitalização de documentos, arquivamento e conversão de imagens em texto editável.

### ✨ Principais Características

- 🖥️ **Interface Gráfica Moderna** - Design intuitivo e profissional
- 📁 **Processamento em Lote** - Processe múltiplos arquivos de uma vez
- 🇧🇷 **OCR em Português** - Reconhecimento otimizado para idioma português
- 🧹 **Limpeza Automática** - Texto formatado e pronto para uso
- 📊 **Progresso em Tempo Real** - Acompanhe cada etapa do processamento
- 💾 **Arquivos Individuais** - Um arquivo .md para cada documento processado
- 🔒 **100% Local** - Seus dados não saem do seu computador

## 📸 Screenshots

![Interface Principal](https://via.placeholder.com/800x500?text=Interface+Principal)

*Interface moderna com tema escuro e organização clara*

## 🚀 Início Rápido

### 📋 Requisitos

- **Windows 10/11** ou **Linux** (Ubuntu, Debian, Fedora, Arch)
- **Python 3.12** ou superior
- **Tesseract OCR** instalado no sistema

### 🪟 Instalação no Windows

1. **Instale o Python**
   - Baixe de [python.org/downloads](https://www.python.org/downloads/)
   - Durante a instalação, marque "Add Python to PATH"

2. **Instale o Tesseract OCR**
   
   **Opção A - Via Chocolatey (recomendado):**
   ```powershell
   choco install tesseract
   ```
   
   **Opção B - Instalador Manual:**
   - Baixe de: [github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
   - Execute o instalador e siga as instruções

3. **Instale o Pacote de Idioma Português**
   ```powershell
   choco install tesseract-lang-por
   ```
   
   Ou baixe manualmente: [por.traineddata](https://github.com/tesseract-ocr/tessdata_best/raw/main/por.traineddata) e copie para `C:\Program Files\Tesseract-OCR\tessdata\`

4. **Clone o Projeto**
   ```powershell
   git clone https://github.com/filipeabraaodasilva/ocr.git
   cd ocr
   ```

5. **Configure o Ambiente**
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

6. **Execute**
   ```powershell
   python main.py
   ```

### 🐧 Instalação no Linux

```bash
# Instalar dependências do sistema
sudo apt-get update
sudo apt-get install -y tesseract-ocr tesseract-ocr-por python3.12 python3.12-venv git

# Clonar projeto
git clone https://github.com/filipeabraaodasilva/ocr.git
cd ocr

# Configurar ambiente
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Executar
python main.py
```

## 📖 Como Usar

### Passo a Passo

1. **Abra a Aplicação**
   ```bash
   python main.py
   ```

2. **Selecione o Diretório**
   - Clique no botão "📁 Selecionar Diretório"
   - Escolha a pasta contendo seus arquivos (imagens ou PDFs)

3. **Visualize os Arquivos**
   - A aplicação detecta automaticamente arquivos suportados
   - Veja a lista com ícones coloridos indicando o tipo

4. **Inicie o Processamento**
   - Clique em "▶ Processar Arquivos"
   - Acompanhe o progresso na barra de status
   - Veja o log detalhado de cada arquivo

5. **Acesse os Resultados**
   - Arquivos `.md` são criados no mesmo diretório
   - Um arquivo para cada documento processado

### Exemplo Visual

**Antes do processamento:**
```
documentos/
├── contrato.pdf
├── relatorio.pdf
└── foto_documento.jpg
```

**Depois do processamento:**
```
documentos/
├── contrato.pdf
├── contrato.md              ← ✓ Texto extraído
├── relatorio.pdf
├── relatorio.md             ← ✓ Texto extraído
├── foto_documento.jpg
└── foto_documento.md        ← ✓ Texto extraído
```

### Formato do Arquivo Gerado

```markdown
# contrato.pdf

**Extraído em:** 03/03/2026 12:30:45

---

[Texto limpo e formatado do documento]
```

## 🔍 Formatos Suportados

| Tipo | Extensões | Status |
|------|-----------|--------|
| **Imagens** | `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.tiff`, `.webp` | ✅ Suportado |
| **PDFs** | `.pdf` | ✅ Suportado |

## 🎯 Processamento de Texto

A aplicação automaticamente:

- ✅ Remove caracteres de controle indesejados
- ✅ Elimina espaços extras e múltiplos
- ✅ Une palavras hifenizadas no final da linha
- ✅ Corrige quebras de linha incorretas
- ✅ Normaliza pontuação e espaçamento
- ✅ Remove linhas vazias excessivas

## 💡 Dicas de Uso

### Para Melhores Resultados

- 📷 Use imagens com **boa resolução** (mínimo 300 DPI)
- 🔆 Certifique-se de que o documento está **bem iluminado**
- 📐 Mantenha o documento **reto** (sem inclinação)
- 🎨 Evite fundos com **muito ruído** ou **sombras**
- 📄 Imagens em **preto e branco** funcionam melhor que coloridas

### Dicas de Performance

- 🚀 Processe em **lotes de até 50 arquivos** por vez
- 💾 Use **SSD** ao invés de HD para processamento mais rápido
- 🖼️ Redimensione imagens muito grandes antes do processamento
- 🔄 Feche outros programas pesados durante o processamento

## 🐛 Solução de Problemas

### Windows

**❌ Erro: "tesseract is not installed"**

Solução:
1. Verifique a instalação: `tesseract --version`
2. Se não funcionar, adicione ao PATH:
   - Pressione `Windows + R`
   - Digite `sysdm.cpl` e pressione Enter
   - Aba "Avançado" → "Variáveis de Ambiente"
   - Edite "Path" e adicione: `C:\Program Files\Tesseract-OCR`
   - Reinicie o terminal

**❌ Erro: "python não é reconhecido"**

Solução:
- Use `py` ao invés de `python`
- Ou reinstale Python marcando "Add to PATH"

**❌ Erro: "Failed to load por.traineddata"**

Solução:
- Instale o pacote português: `choco install tesseract-lang-por`
- Ou baixe manualmente e copie para a pasta tessdata

### Linux

**❌ Erro: "tesseract: command not found"**
```bash
sudo apt-get install tesseract-ocr tesseract-ocr-por
```

**❌ Erro: "ModuleNotFoundError"**
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### Problemas Comuns

**OCR não reconhece texto corretamente:**
- Verifique a qualidade da imagem
- Use imagens com maior resolução
- Certifique-se de que o documento está em português
- Melhore o contraste da imagem

**Aplicação não abre:**
- Execute via terminal para ver mensagens de erro
- Verifique se Python 3.12+ está instalado
- Certifique-se de que o ambiente virtual está ativado

## 📦 Criar Executável

Para distribuir o projeto como executável:

### Windows
```powershell
# Ativar ambiente virtual
.venv\Scripts\activate

# Instalar PyInstaller
pip install -r requirements-build.txt

# Criar executável
.\build.ps1

# Resultado: dist\OCR_Pipeline.exe
```

### Linux
```bash
# Ativar ambiente virtual
source .venv/bin/activate

# Instalar PyInstaller
pip install -r requirements-build.txt

# Criar executável
./build.sh

# Resultado: dist/OCR_Pipeline
```

**⚠️ Nota:** O executável não inclui o Tesseract OCR. Usuários finais precisam instalá-lo separadamente seguindo as instruções acima.

## 🔒 Segurança e Privacidade

- ✅ **Processamento Local** - Todo o processamento é feito no seu computador
- ✅ **Sem Conexão Internet** - Nenhum dado é enviado para servidores externos
- ✅ **Código Aberto** - Todo o código é auditável e transparente
- ✅ **Seus Documentos** - Permanecem privados e sob seu controle

## 🤝 Como Contribuir

Contribuições são muito bem-vindas! Para contribuir:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🙏 Agradecimentos

Este projeto foi possível graças a:

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) - Motor de OCR open source
- [Flet](https://flet.dev/) - Framework para interfaces gráficas em Python
- [Pillow](https://python-pillow.org/) - Biblioteca de processamento de imagens
- [markitdown](https://github.com/microsoft/markitdown) - Extração de texto de PDFs

## 📞 Suporte

Encontrou um problema ou tem uma sugestão?

- 🐛 [Abra uma Issue](https://github.com/filipeabraaodasilva/ocr/issues)
- 💡 [Discussões](https://github.com/filipeabraaodasilva/ocr/discussions)
- 📧 Entre em contato via Issues do GitHub

## 🌟 Mostre seu Apoio

Se este projeto foi útil para você, considere dar uma ⭐ no repositório!

---

<div align="center">

**Desenvolvido com ❤️ para facilitar a digitalização de documentos**

[⬆ Voltar ao topo](#-ocr-pipeline)

</div>
