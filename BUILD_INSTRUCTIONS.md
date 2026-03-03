# 🏗️ Instruções de Build - OCR Pipeline

Guia completo para criar executável distribuível.

## 📋 Pré-requisitos

### Windows
- Python 3.12+ instalado
- PowerShell 5.0+
- 500 MB de espaço livre

### Linux
- Python 3.12+ instalado
- Bash shell
- 500 MB de espaço livre

## 🚀 Build Rápido

### 🪟 Windows

```powershell
# 1. Ativar ambiente virtual
.venv\Scripts\activate

# 2. Instalar PyInstaller
pip install -r requirements-build.txt

# 3. Executar build
.\build.ps1

# 4. Resultado em: dist\OCR_Pipeline.exe
```

### 🐧 Linux

```bash
# 1. Ativar ambiente virtual
source .venv/bin/activate

# 2. Instalar PyInstaller
pip install -r requirements-build.txt

# 3. Executar build
./build.sh

# 4. Resultado em: dist/OCR_Pipeline
```

## 📦 Arquivos de Build

### build.spec
Configuração do PyInstaller. Define:
- Nome do executável
- Ícone (se houver)
- Dependências incluídas
- Modo de compilação (onefile/onedir)

### build.ps1 (Windows)
Script PowerShell que:
- Verifica ambiente virtual
- Instala PyInstaller
- Limpa builds anteriores
- Cria executável
- Mostra resultado

### build.sh (Linux)
Script Bash equivalente para Linux.

## 🎯 Processo de Build Detalhado

### Etapa 1: Preparação
```powershell
# Limpar cache Python
py -m pip cache purge

# Atualizar pip
pip install --upgrade pip

# Instalar/atualizar PyInstaller
pip install --upgrade pyinstaller
```

### Etapa 2: Configuração

**Editar build.spec se necessário:**
```python
# Nome do executável
name='OCR_Pipeline',

# Adicionar ícone (opcional)
icon='icon.ico',

# Modo console (debug)
console=False,  # False = sem janela CMD

# Compressão UPX
upx=True,  # Reduz tamanho
```

### Etapa 3: Build

**Opção A - Via Script (Recomendado):**
```powershell
.\build.ps1
```

**Opção B - Manual:**
```powershell
# Limpar
Remove-Item -Recurse -Force build, dist

# Build
pyinstaller build.spec --clean --noconfirm
```

### Etapa 4: Teste

```powershell
# Executar
.\dist\OCR_Pipeline.exe

# Verificar se abre
# Testar processamento de arquivo
```

## 🔧 Customizações

### Adicionar Ícone

1. **Criar/obter ícone .ico**
   - Tamanho: 256x256 pixels
   - Formato: .ico (Windows) ou .icns (Mac)

2. **Editar build.spec:**
   ```python
   exe = EXE(
       ...
       icon='icon.ico',  # Adicionar esta linha
       ...
   )
   ```

3. **Rebuild:**
   ```powershell
   pyinstaller build.spec --clean
   ```

### Incluir Arquivos Extras

```python
# Em build.spec, adicionar em Analysis:
datas=[
    ('recursos/', 'recursos/'),  # Pasta de recursos
    ('config.json', '.'),         # Arquivo individual
],
```

### Build em Uma Pasta (ao invés de um arquivo)

```python
# Em build.spec, mudar EXE para:
exe = EXE(
    pyz,
    a.scripts,
    [],  # Lista vazia aqui
    exclude_binaries=True,  # Adicionar
    ...
)

# Adicionar COLLECT:
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='OCR_Pipeline'
)
```

## 📊 Tamanhos e Performance

### Tamanhos Esperados

| Tipo | Tamanho |
|------|---------|
| **--onefile** | 80-120 MB |
| **--onedir** | 150-200 MB (distribuído em pasta) |
| **Com UPX** | 60-90 MB |

### Tempo de Build

| Sistema | Tempo |
|---------|-------|
| Windows 10 (i5, SSD) | 2-5 minutos |
| Windows 11 (i7, SSD) | 1-3 minutos |
| Linux (i5, SSD) | 1-3 minutos |

## ⚠️ Importante para Distribuição

### O que ESTÁ incluído:
- ✅ Python runtime
- ✅ Flet e dependências
- ✅ Pillow
- ✅ pytesseract (wrapper Python)

### O que NÃO está incluído:
- ❌ Tesseract OCR (executável)
- ❌ Pacotes de idioma do Tesseract
- ❌ markitdown (precisa ser instalável via pip)

### Soluções:

**Opção 1: Instruir usuário** (Recomendado)
- Incluir `README_DISTRIBUICAO.txt`
- Listar requisitos claramente

**Opção 2: Criar instalador**
- Usar Inno Setup ou NSIS
- Incluir Tesseract no instalador
- Configurar PATH automaticamente

**Opção 3: Bundled**
- Incluir Tesseract na pasta
- Modificar código para apontar para binário local
- Maior tamanho (~200 MB)

## 🐛 Troubleshooting Build

### Erro: "Unable to find vcvarsall.bat"
```powershell
# Instalar Visual C++ Build Tools
# https://visualstudio.microsoft.com/downloads/
```

### Erro: "ImportError" no executável
```powershell
# Adicionar ao hiddenimports no build.spec
hiddenimports=[
    'flet',
    'pytesseract',
    'PIL',
    'PIL._imagingtk',
    'PIL._tkinter_finder',
    'modulo_que_falta',
],

# Rebuild
pyinstaller build.spec --clean
```

### Executável não abre (Windows)
```powershell
# Build com console para debug
# Em build.spec: console=True
pyinstaller build.spec --clean

# Executar e ver erros
.\dist\OCR_Pipeline.exe
```

### Antivírus bloqueia executável
```powershell
# Assinar digitalmente (requer certificado)
# Ou adicionar exceção no antivírus
# Ou buildar em VM limpa
```

### Erro: "Failed to execute script"
```powershell
# Verificar todas as dependências
pip list

# Rebuild do zero
Remove-Item -Recurse -Force build, dist, __pycache__
pip uninstall pyinstaller
pip install pyinstaller
pyinstaller build.spec --clean
```

## 📦 Criar Pacote de Distribuição

### Estrutura Recomendada

```
OCR_Pipeline_v2.0/
├── OCR_Pipeline.exe          # Executável
├── README_DISTRIBUICAO.txt   # Instruções para usuário
├── LICENSE.txt               # Licença
└── recursos/                 # Recursos extras (se houver)
```

### Criar ZIP

```powershell
# Windows
Compress-Archive -Path dist\OCR_Pipeline.exe, README_DISTRIBUICAO.txt, LICENSE -DestinationPath OCR_Pipeline_v2.0_Windows.zip

# Linux
zip -r OCR_Pipeline_v2.0_Linux.zip dist/OCR_Pipeline README_DISTRIBUICAO.txt LICENSE
```

## 🔒 Boas Práticas

### Antes do Build
- [ ] Testar código em ambiente limpo
- [ ] Atualizar versão no código
- [ ] Atualizar CHANGELOG
- [ ] Verificar todas as dependências

### Durante o Build
- [ ] Usar ambiente virtual limpo
- [ ] Build com console=False
- [ ] Testar executável em VM limpa
- [ ] Verificar tamanho do arquivo

### Após o Build
- [ ] Testar em Windows limpo
- [ ] Verificar com antivírus
- [ ] Documentar instruções
- [ ] Criar release notes

## 📈 Versionamento

Sugestão de nomenclatura:
```
OCR_Pipeline_v2.0.0_Windows_x64.exe
OCR_Pipeline_v2.0.0_Linux_x64
```

Formato: `NomeProjeto_vMAJOR.MINOR.PATCH_Plataforma_Arquitetura`

## 🚀 Automação CI/CD

Para automatizar builds:

**GitHub Actions:**
```yaml
name: Build Executables
on: [push, release]
jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [windows-latest, ubuntu-latest]
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: pip install -r requirements.txt
      - run: pip install pyinstaller
      - run: pyinstaller build.spec
```

---

**Build pronto para produção!** 🎉
