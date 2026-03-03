========================================
  OCR Pipeline - Guia de Instalação
========================================

Obrigado por baixar o OCR Pipeline!

Este programa extrai texto de imagens e PDFs usando OCR (Reconhecimento Óptico de Caracteres).

========================================
  REQUISITOS
========================================

Para usar este programa, você precisa instalar:

1. Tesseract OCR (Motor de reconhecimento)
2. Pacote de idioma Português

========================================
  INSTALAÇÃO (Windows)
========================================

PASSO 1: Instalar Tesseract OCR
--------------------------------

Opção A - Via Chocolatey (Recomendado):
  1. Abra PowerShell como Administrador
  2. Execute: choco install tesseract
  
Opção B - Instalador Manual:
  1. Baixe de: https://github.com/UB-Mannheim/tesseract/wiki
  2. Execute o instalador: tesseract-ocr-w64-setup-5.x.x.exe
  3. Instale na pasta padrão: C:\Program Files\Tesseract-OCR
  4. IMPORTANTE: Marque "Add to PATH" durante instalação


PASSO 2: Instalar Pacote Português
-----------------------------------

Opção A - Via Chocolatey:
  choco install tesseract-lang-por

Opção B - Manual:
  1. Baixe: https://github.com/tesseract-ocr/tessdata_best/raw/main/por.traineddata
  2. Copie para: C:\Program Files\Tesseract-OCR\tessdata\


PASSO 3: Verificar Instalação
------------------------------

Abra CMD ou PowerShell e execute:
  tesseract --version
  
Se aparecer a versão (ex: tesseract 5.3.0), está instalado!


PASSO 4: Adicionar ao PATH (se necessário)
-------------------------------------------

Se o comando acima não funcionar:
  1. Pressione Windows + R
  2. Digite: sysdm.cpl
  3. Aba "Avançado" → "Variáveis de Ambiente"
  4. Em "Path", clique em "Editar"
  5. Adicione: C:\Program Files\Tesseract-OCR
  6. OK → OK → Reinicie o terminal

========================================
  COMO USAR
========================================

1. Execute: OCR_Pipeline.exe

2. Clique em "Selecionar Diretório"

3. Escolha a pasta com suas imagens ou PDFs

4. Clique em "Processar Arquivos"

5. Aguarde o processamento (veja o progresso)

6. Pronto! Arquivos .md foram criados com o texto extraído

========================================
  FORMATOS SUPORTADOS
========================================

Imagens:  PNG, JPG, JPEG, GIF, BMP, TIFF, WEBP
Documentos: PDF

========================================
  SOLUÇÃO DE PROBLEMAS
========================================

ERRO: "tesseract is not installed"
  → Instale o Tesseract OCR (Passo 1 acima)
  → Verifique se está no PATH (Passo 4 acima)

ERRO: "Failed to load por.traineddata"
  → Instale o pacote português (Passo 2 acima)

Aplicação não abre ou fecha imediatamente:
  → Verifique se Tesseract está instalado
  → Execute via terminal para ver erros:
    cmd → cd "caminho\do\executavel" → OCR_Pipeline.exe

OCR não reconhece texto corretamente:
  → Use imagens com boa qualidade (300+ DPI)
  → Melhore o contraste da imagem
  → Verifique se o documento está em português

========================================
  CARACTERÍSTICAS
========================================

✓ Interface gráfica moderna e intuitiva
✓ Processamento em lote (múltiplos arquivos)
✓ Barra de progresso em tempo real
✓ Log detalhado de processamento
✓ Limpeza automática de texto
✓ Arquivo individual para cada documento
✓ 100% seguro - processamento local

========================================
  SOBRE O ARQUIVO GERADO
========================================

Para cada arquivo processado, é criado um arquivo .md:

Exemplo:
  contrato.pdf  →  contrato.md

O arquivo .md contém:
  - Nome do arquivo original
  - Data e hora da extração
  - Texto limpo e formatado

Você pode abrir .md com qualquer editor de texto!

========================================
  SEGURANÇA E PRIVACIDADE
========================================

✓ Todo processamento é feito localmente no seu computador
✓ Nenhum dado é enviado para internet
✓ Nenhuma conexão externa é feita
✓ Seus documentos permanecem privados

========================================
  SUPORTE
========================================

Problemas? Dúvidas?

- Repositório: <url-do-repositorio>
- Issues: <url-do-repositorio>/issues
- Email: <seu-email>

========================================
  LICENÇA
========================================

Este software é distribuído sob licença MIT
Código aberto e gratuito

Desenvolvido com ❤️

========================================

Versão: 2.0.0
Data: 03/03/2026

Obrigado por usar o OCR Pipeline!
