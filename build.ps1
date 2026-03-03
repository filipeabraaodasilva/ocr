# Script PowerShell para criar executável Windows
# Uso: .\build.ps1

Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "  OCR Pipeline - Build Windows EXE  " -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""

# Verificar se está no ambiente virtual
if ($env:VIRTUAL_ENV) {
    Write-Host "[OK] Ambiente virtual ativado" -ForegroundColor Green
} else {
    Write-Host "[ERRO] Ative o ambiente virtual primeiro!" -ForegroundColor Red
    Write-Host "Execute: .venv\Scripts\activate" -ForegroundColor Yellow
    exit 1
}

# Instalar PyInstaller
Write-Host ""
Write-Host "[1/4] Instalando PyInstaller..." -ForegroundColor Yellow
pip install pyinstaller --quiet

# Limpar builds anteriores
Write-Host "[2/4] Limpando builds anteriores..." -ForegroundColor Yellow
if (Test-Path "build") { Remove-Item -Recurse -Force "build" }
if (Test-Path "dist") { Remove-Item -Recurse -Force "dist" }
if (Test-Path "__pycache__") { Remove-Item -Recurse -Force "__pycache__" }

# Criar executável
Write-Host "[3/4] Criando executável..." -ForegroundColor Yellow
Write-Host "Isso pode levar alguns minutos..." -ForegroundColor Gray
pyinstaller build.spec --clean --noconfirm

# Verificar se foi criado
Write-Host "[4/4] Verificando..." -ForegroundColor Yellow
if (Test-Path "dist\OCR_Pipeline.exe") {
    Write-Host ""
    Write-Host "=====================================" -ForegroundColor Green
    Write-Host "        BUILD CONCLUÍDO!            " -ForegroundColor Green
    Write-Host "=====================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Executável criado em:" -ForegroundColor White
    Write-Host "  dist\OCR_Pipeline.exe" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Tamanho:" -ForegroundColor White
    $size = (Get-Item "dist\OCR_Pipeline.exe").Length / 1MB
    Write-Host "  $([math]::Round($size, 2)) MB" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Para executar:" -ForegroundColor White
    Write-Host "  .\dist\OCR_Pipeline.exe" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "IMPORTANTE: Tesseract OCR deve estar instalado!" -ForegroundColor Red
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "[ERRO] Falha ao criar executável!" -ForegroundColor Red
    Write-Host "Verifique os logs acima para detalhes." -ForegroundColor Yellow
    exit 1
}
