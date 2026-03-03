#!/usr/bin/env python3
"""OCR Pipeline - Interface gráfica para extração de texto de imagens e PDFs."""

import os
import re
import subprocess
import threading
from datetime import datetime

import flet as ft
import pytesseract
from PIL import Image


SUPPORTED_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp', '.pdf'}
IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp'}
MAX_LOG_MESSAGES = 100


class OCRApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self._configure_page()
        
        self.selected_directory = None
        self.is_processing = False
        self.files_to_process = []
        
        self._create_widgets()
        self.page.update()
    
    def _configure_page(self):
        self.page.title = "OCR Pipeline - Extração de Texto"
        self.page.window.width = 1000
        self.page.window.height = 800
        self.page.window.min_width = 900
        self.page.window.min_height = 700
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.padding = 20
        self.page.scroll = ft.ScrollMode.AUTO
    
    def _create_widgets(self):
        header = self._build_header()
        directory_card = self._build_directory_card()
        files_card = self._build_files_card()
        progress_card = self._build_progress_card()
        log_card = self._build_log_card()
        actions_row = self._build_actions_row()
        
        self.page.add(
            ft.Column([
                header,
                directory_card,
                ft.Container(height=15),
                files_card,
                ft.Container(height=15),
                progress_card,
                ft.Container(height=15),
                log_card,
                ft.Container(height=20),
                actions_row,
            ], scroll=ft.ScrollMode.AUTO)
        )
    
    def _build_header(self):
        return ft.Container(
            content=ft.Column([
                ft.Text(
                    "📄 Pipeline de OCR e Extração de Texto",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "Converte imagens e PDFs em texto pesquisável",
                    size=16,
                    color=ft.Colors.GREY_400,
                    text_align=ft.TextAlign.CENTER,
                ),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=ft.Padding(0, 0, 0, 30),
        )
    
    def _build_directory_card(self):
        self.dir_text = ft.Text(
            "Nenhum diretório selecionado",
            size=14,
            color=ft.Colors.GREY_500,
            italic=True,
        )
        
        self.select_dir_btn = ft.FilledButton(
            content=ft.Row([
                ft.Icon(ft.Icons.FOLDER_OPEN),
                ft.Text("Selecionar Diretório"),
            ], tight=True),
            on_click=self.select_directory,
            height=50,
        )
        
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Icon(ft.Icons.FOLDER, color=ft.Colors.BLUE_400, size=20),
                        ft.Text("Diretório de Trabalho", size=18, weight=ft.FontWeight.BOLD),
                    ]),
                    ft.Divider(height=1, color=ft.Colors.GREY_800),
                    ft.Container(height=10),
                    self.select_dir_btn,
                    self.dir_text,
                ]),
                padding=20,
            ),
            elevation=2,
        )
    
    def _build_files_card(self):
        self.files_count_text = ft.Text("0 arquivos", size=14, color=ft.Colors.GREY_500)
        self.files_list = ft.ListView(spacing=5, padding=10, height=180)
        
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Icon(ft.Icons.LIST_ALT, color=ft.Colors.GREEN_400, size=20),
                        ft.Text("Arquivos Encontrados", size=18, weight=ft.FontWeight.BOLD),
                        ft.Container(expand=True),
                        self.files_count_text,
                    ]),
                    ft.Divider(height=1, color=ft.Colors.GREY_800),
                    ft.Container(height=10),
                    ft.Container(
                        content=self.files_list,
                        border=ft.border.all(1, ft.Colors.GREY_800),
                        border_radius=8,
                    ),
                ]),
                padding=20,
            ),
            elevation=2,
        )
    
    def _build_progress_card(self):
        self.progress_bar = ft.ProgressBar(
            value=0,
            bar_height=12,
            color=ft.Colors.GREEN_400,
            bgcolor=ft.Colors.GREY_800,
        )
        
        self.progress_text = ft.Text(
            "Pronto para processar",
            size=13,
            color=ft.Colors.GREY_500,
            text_align=ft.TextAlign.CENTER,
        )
        
        self.current_file_text = ft.Text(
            "",
            size=12,
            color=ft.Colors.BLUE_300,
            italic=True,
            text_align=ft.TextAlign.CENTER,
        )
        
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Icon(ft.Icons.TIMELINE, color=ft.Colors.ORANGE_400, size=20),
                        ft.Text("Progresso", size=18, weight=ft.FontWeight.BOLD),
                    ]),
                    ft.Divider(height=1, color=ft.Colors.GREY_800),
                    ft.Container(height=10),
                    self.progress_bar,
                    ft.Container(height=5),
                    self.progress_text,
                    self.current_file_text,
                ]),
                padding=20,
            ),
            elevation=2,
        )
    
    def _build_log_card(self):
        self.log_list = ft.ListView(spacing=2, padding=10, height=200, auto_scroll=True)
        
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Icon(ft.Icons.TERMINAL, color=ft.Colors.PURPLE_400, size=20),
                        ft.Text("Log de Processamento", size=18, weight=ft.FontWeight.BOLD),
                        ft.Container(expand=True),
                        ft.IconButton(
                            icon=ft.Icons.DELETE_OUTLINE,
                            icon_color=ft.Colors.RED_400,
                            tooltip="Limpar log",
                            on_click=lambda _: self.clear_log(),
                        ),
                    ]),
                    ft.Divider(height=1, color=ft.Colors.GREY_800),
                    ft.Container(height=10),
                    ft.Container(
                        content=self.log_list,
                        border=ft.border.all(1, ft.Colors.GREY_800),
                        border_radius=8,
                        bgcolor=ft.Colors.GREY_900,
                    ),
                ]),
                padding=20,
            ),
            elevation=2,
        )
    
    def _build_actions_row(self):
        self.process_btn = ft.FilledButton(
            content=ft.Row([
                ft.Icon(ft.Icons.PLAY_ARROW),
                ft.Text("Processar Arquivos", size=16, weight=ft.FontWeight.BOLD),
            ], tight=True),
            on_click=self.start_processing,
            disabled=True,
            height=60,
            style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_700),
            expand=True,
        )
        
        return ft.Row([
            self.process_btn,
            ft.FilledButton(
                content=ft.Row([
                    ft.Icon(ft.Icons.EXIT_TO_APP),
                    ft.Text("Sair"),
                ], tight=True),
                on_click=lambda _: self.page.window.close(),
                height=60,
                style=ft.ButtonStyle(bgcolor=ft.Colors.RED_700),
            ),
        ], spacing=15)
    
    def select_directory(self, e):
        def handle_result(e: ft.FilePickerResultEvent):
            if e.path:
                self.selected_directory = e.path
                self.dir_text.value = e.path
                self.dir_text.italic = False
                self.dir_text.color = ft.Colors.WHITE
                self.scan_directory()
                self.log_message(f"📁 Diretório selecionado: {e.path}")
                self.page.update()
        
        picker = ft.FilePicker(on_result=handle_result)
        self.page.overlay.append(picker)
        self.page.update()
        picker.get_directory_path(dialog_title="Selecione o diretório")
    
    def scan_directory(self):
        if not self.selected_directory:
            return
        
        self.files_to_process = []
        
        try:
            for file in os.listdir(self.selected_directory):
                file_path = os.path.join(self.selected_directory, file)
                if os.path.isfile(file_path):
                    ext = os.path.splitext(file)[1].lower()
                    if ext in SUPPORTED_EXTENSIONS:
                        self.files_to_process.append(file)
            
            self._update_files_ui()
            self.page.update()
        
        except Exception as e:
            self.log_message(f"✗ Erro ao escanear diretório: {e}", "error")
    
    def _update_files_ui(self):
        self.files_list.controls.clear()
        
        if self.files_to_process:
            for i, file in enumerate(self.files_to_process, 1):
                ext = os.path.splitext(file)[1].upper()[1:]
                icon = ft.Icons.PICTURE_AS_PDF if ext == 'PDF' else ft.Icons.IMAGE
                icon_color = ft.Colors.RED_400 if ext == 'PDF' else ft.Colors.BLUE_400
                
                self.files_list.controls.append(
                    ft.Container(
                        content=ft.Row([
                            ft.Icon(icon, size=16, color=icon_color),
                            ft.Text(f"{i}.", size=12, color=ft.Colors.GREY_500, width=30),
                            ft.Text(f"[{ext}]", size=12, weight=ft.FontWeight.BOLD, color=icon_color, width=50),
                            ft.Text(file, size=12),
                        ]),
                        padding=5,
                        border_radius=5,
                        bgcolor=ft.Colors.GREY_900,
                    )
                )
            
            self.files_count_text.value = f"{len(self.files_to_process)} arquivos"
            self.files_count_text.color = ft.Colors.GREEN_400
            self.process_btn.disabled = False
            self.log_message(f"✓ {len(self.files_to_process)} arquivo(s) encontrado(s)")
        else:
            self._show_empty_files_message()
            self.files_count_text.value = "0 arquivos"
            self.files_count_text.color = ft.Colors.GREY_500
            self.process_btn.disabled = True
            self.log_message("⚠ Nenhum arquivo suportado encontrado")
    
    def _show_empty_files_message(self):
        self.files_list.controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Text("Nenhum arquivo suportado encontrado.", color=ft.Colors.GREY_500),
                    ft.Container(height=10),
                    ft.Text("Formatos suportados:", size=12, weight=ft.FontWeight.BOLD),
                    ft.Text("• Imagens: PNG, JPG, GIF, BMP, TIFF, WEBP", size=11),
                    ft.Text("• Documentos: PDF", size=11),
                ]),
                padding=15,
            )
        )
    
    def start_processing(self, e):
        if self.is_processing or not self.files_to_process:
            if not self.files_to_process:
                self.show_alert("Aviso", "Nenhum arquivo para processar!", ft.Colors.ORANGE_700)
            return
        
        self.process_btn.disabled = True
        self.select_dir_btn.disabled = True
        self.is_processing = True
        self.page.update()
        
        threading.Thread(target=self.process_files, daemon=True).start()
    
    def process_files(self):
        total_files = len(self.files_to_process)
        processed_count = 0
        
        self._log_processing_start(total_files)
        
        for i, filename in enumerate(self.files_to_process, 1):
            file_path = os.path.join(self.selected_directory, filename)
            progress = i / total_files
            
            self.update_progress(progress, f"{i}/{total_files} arquivos processados", filename)
            self.log_message(f"\n[{i}/{total_files}] Processando: {filename}")
            
            try:
                text = self._process_single_file(file_path)
                
                if text:
                    output_file = self._generate_output_filename(filename)
                    self._save_individual_file(output_file, text, filename)
                    processed_count += 1
                    self.log_message(f"  ✓ Sucesso ({len(text)} caracteres) → {os.path.basename(output_file)}")
                else:
                    self.log_message(f"  ⚠ Nenhum texto extraído", "warning")
            
            except Exception as e:
                self.log_message(f"  ✗ Erro: {str(e)}", "error")
        
        self._log_processing_end(processed_count, total_files)
        self._finish_processing()
    
    def _generate_output_filename(self, input_filename):
        base_name = os.path.splitext(input_filename)[0]
        return os.path.join(self.selected_directory, f"{base_name}.md")
    
    def _save_individual_file(self, output_file, text, original_filename):
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# {original_filename}\n\n")
            f.write(f"**Extraído em:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
            f.write("---\n\n")
            f.write(text)
    
    def _log_processing_start(self, total_files):
        separator = "=" * 60
        self.log_message(f"\n{separator}")
        self.log_message("🚀 INICIANDO PROCESSAMENTO")
        self.log_message(separator)
        self.log_message(f"Total de arquivos: {total_files}")
        self.log_message(f"{separator}\n")
    
    def _log_processing_end(self, processed_count, total_files):
        separator = "=" * 60
        self.log_message(f"\n{separator}")
        self.log_message("✓ PROCESSAMENTO CONCLUÍDO!")
        self.log_message(f"✓ {processed_count}/{total_files} arquivos processados com sucesso")
        self.log_message(f"{separator}\n")
        
        self.show_alert(
            "Sucesso!",
            f"Processamento concluído!\n\n{processed_count} de {total_files} arquivos processados\nArquivos .md criados no diretório",
            ft.Colors.GREEN_700
        )
    
    def _finish_processing(self):
        self.process_btn.disabled = False
        self.select_dir_btn.disabled = False
        self.is_processing = False
        self.update_progress(0, "Pronto para processar", "")
        self.page.update()
    
    def _process_single_file(self, file_path):
        ext = os.path.splitext(file_path)[1].lower()
        
        if ext in IMAGE_EXTENSIONS:
            return self._process_image(file_path)
        elif ext == '.pdf':
            text = self._extract_text_with_markitdown(file_path)
            return self._clean_text(text) if text else None
        
        return None
    
    def _process_image(self, file_path):
        temp_pdf = file_path + "_temp.pdf"
        
        try:
            image = Image.open(file_path)
            image = self._convert_to_rgb(image)
            
            ocr_data = pytesseract.image_to_pdf_or_hocr(image, extension='pdf', lang='por')
            
            with open(temp_pdf, 'wb') as f:
                f.write(ocr_data)
            
            text = self._extract_text_with_markitdown(temp_pdf)
            os.remove(temp_pdf)
            
            return self._clean_text(text) if text else None
        
        except Exception as e:
            if os.path.exists(temp_pdf):
                os.remove(temp_pdf)
            raise e
    
    @staticmethod
    def _convert_to_rgb(image):
        if image.mode in ('RGBA', 'LA', 'P'):
            rgb_image = Image.new('RGB', image.size, (255, 255, 255))
            if image.mode == 'P':
                image = image.convert('RGBA')
            rgb_image.paste(image, mask=image.split()[-1] if image.mode in ('RGBA', 'LA') else None)
            return rgb_image
        elif image.mode != 'RGB':
            return image.convert('RGB')
        return image
    
    @staticmethod
    def _extract_text_with_markitdown(pdf_path):
        try:
            result = subprocess.run(
                ['markitdown', pdf_path],
                capture_output=True,
                text=True,
                check=True,
                timeout=60
            )
            return result.stdout
        except Exception:
            return None
    
    @staticmethod
    def _clean_text(text):
        if not text:
            return ""
        
        text = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', text)
        text = re.sub(r' +\n', '\n', text)
        text = re.sub(r'\n +', '\n', text)
        text = re.sub(r'\n{3,}', '\n\n', text)
        text = re.sub(r'-\n([a-zàáâãäåèéêëìíîïòóôõöùúûüç])', r'\1', text, flags=re.IGNORECASE)
        text = re.sub(r'([^\n.!?:;])\n([a-zàáâãäåèéêëìíîïòóôõöùúûüç])', r'\1 \2', text, flags=re.IGNORECASE)
        text = re.sub(r' {2,}', ' ', text)
        text = re.sub(r' +([,.!?;:])', r'\1', text)
        text = re.sub(r'([.!?;:])([A-ZÀ-Ú])', r'\1 \2', text)
        text = re.sub(r'\n\s+\n', '\n\n', text)
        
        return text.strip()
    
    def update_progress(self, value, text, current_file):
        self.progress_bar.value = value
        self.progress_text.value = text
        self.current_file_text.value = f"📄 {current_file}" if current_file else ""
        self.page.update()
    
    def log_message(self, message, level="info"):
        colors = {
            "error": ft.Colors.RED_400,
            "warning": ft.Colors.ORANGE_400,
            "success": ft.Colors.GREEN_400,
            "info": ft.Colors.GREY_400
        }
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        self.log_list.controls.append(
            ft.Text(
                f"[{timestamp}] {message}",
                size=11,
                color=colors.get(level, ft.Colors.GREY_400),
                font_family="Courier New",
            )
        )
        
        if len(self.log_list.controls) > MAX_LOG_MESSAGES:
            self.log_list.controls.pop(0)
        
        self.page.update()
    
    def clear_log(self):
        self.log_list.controls.clear()
        self.log_message("Log limpo")
        self.page.update()
    
    def show_alert(self, title, message, bgcolor):
        def close_dialog(e):
            dialog.open = False
            self.page.update()
        
        dialog = ft.AlertDialog(
            title=ft.Text(title, weight=ft.FontWeight.BOLD),
            content=ft.Text(message),
            bgcolor=bgcolor,
            actions=[ft.TextButton("OK", on_click=close_dialog)],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()


def main(page: ft.Page):
    OCRApp(page)


if __name__ == "__main__":
    ft.app(target=main)
