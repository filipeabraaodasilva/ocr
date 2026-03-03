#!/bin/bash
# Script Bash para criar executável Linux
# Uso: ./build.sh

echo "====================================="
echo "  OCR Pipeline - Build Linux Binary  "
echo "====================================="
echo ""

# Verificar se está no ambiente virtual
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "[OK] Ambiente virtual ativado"
else
    echo "[ERRO] Ative o ambiente virtual primeiro!"
    echo "Execute: source .venv/bin/activate"
    exit 1
fi

# Instalar PyInstaller
echo ""
echo "[1/4] Instalando PyInstaller..."
pip install pyinstaller --quiet

# Limpar builds anteriores
echo "[2/4] Limpando builds anteriores..."
rm -rf build dist __pycache__ *.spec 2>/dev/null

# Criar executável
echo "[3/4] Criando executável..."
echo "Isso pode levar alguns minutos..."
pyinstaller --name OCR_Pipeline \
    --onefile \
    --windowed \
    --clean \
    --noconfirm \
    main.py

# Verificar se foi criado
echo "[4/4] Verificando..."
if [ -f "dist/OCR_Pipeline" ]; then
    echo ""
    echo "====================================="
    echo "        BUILD CONCLUÍDO!            "
    echo "====================================="
    echo ""
    echo "Executável criado em:"
    echo "  dist/OCR_Pipeline"
    echo ""
    echo "Tamanho:"
    du -h dist/OCR_Pipeline | awk '{print "  " $1}'
    echo ""
    echo "Para executar:"
    echo "  ./dist/OCR_Pipeline"
    echo ""
    echo "IMPORTANTE: Tesseract OCR deve estar instalado!"
    echo ""
    
    # Tornar executável
    chmod +x dist/OCR_Pipeline
else
    echo ""
    echo "[ERRO] Falha ao criar executável!"
    echo "Verifique os logs acima para detalhes."
    exit 1
fi
