import flet as ft
from flet import View, Container, MainAxisAlignment, CrossAxisAlignment, Margin


def main(page: ft.Page):
    page.title = "KHNU : Grade Genius"
    page.window_width = 400
    page.window_height = 600
    page.window_resizable = False
    page.theme_mode = ft.ThemeMode.DARK
    # page.window_center()
    page.update()
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(automatically_imply_leading=False, title=ft.Text("Головна"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("Студент", on_click=lambda _: page.go("/student")),
                    ft.ElevatedButton("Викладач", on_click=lambda _: page.go("/teacher")),
                ],
                vertical_alignment = MainAxisAlignment.CENTER,
                horizontal_alignment = CrossAxisAlignment.CENTER,

            )

        )
        if page.route == "/student":
            page.views.append(
                ft.View(
                    "/student",
                    [
                        ft.AppBar(automatically_imply_leading=False, title=ft.Text("Студент"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Ввести дані"),
                        ft.OutlinedButton("Старт", width=100),
                        ft.FilledButton("Назад", on_click=lambda _: page.go("/")),
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=150
                )
            )
        if page.route == "/teacher":
            page.views.append(
                ft.View(
                    "/teacher",
                    [   
                        ft.AppBar(automatically_imply_leading=False, title=ft.Text("Викладач"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Ввести дані"),
                        ft.OutlinedButton("Старт", width=100),
                        ft.FilledButton("Назад", on_click=lambda _: page.go("/")),
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=150
                )
            )
        page.update()

        
    page.on_route_change = route_change
    page.go(page.route)
    
ft.app(target=main, assets_dir="assets")