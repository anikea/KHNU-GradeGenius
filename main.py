import flet as ft


def main(page: ft.Page):
    page.title = "KHNU : Grade Genius"
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False
    page.theme_mode = ft.ThemeMode.DARK
    page.add(ft.Image(src=f"/icons/favicon.png"))
    page.update()
    
    
ft.app(target=main, assets_dir="assets")