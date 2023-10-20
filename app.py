#                                  Nesecary Imports                              #
# ----------------------------------------------------------------------------#
import flet as ft
from flet import (
    icons,
    Column,
    Container,
    colors,
    AppBar,
    Text,
    Row,
    alignment,
    padding,
    border,
    IconButton,
)
import os
import _random


#                                  User Control                               #
# -----------------------------------------------------------------------------#


TextBox = TextBox = ft.TextField(
    multiline=True,
    expand=False,
    hint_text="Type Here",
    label="Editor",
    min_lines=18,
    max_lines=18,
    text_size=26,
)
c5 = Container(TextBox, margin=10)


def file_result(e: ft.FilePickerResultEvent):
    global file_path
    file_path = e.files[0].path
    print(file_path)
    f = open(file_path, "r")
    for line in f:
        TextBox.value += line
    TextBox.update()


file_picker = ft.FilePicker(on_result=file_result)


def write(e):
    val = TextBox.value
    with open(file_path, "w") as f:
        f.write(val)


def file_savas(e: ft.FilePickerResultEvent):
    valf = TextBox.value
    result = file_plicker.result.path
    with open(str(result), "w") as w:
        w.write(valf)


file_plicker = ft.FilePicker(on_result=file_savas)

#                                  Main Page                                  #
# -----------------------------------------------------------------------------#


def main(page: ft.Page):
    page.window_width = 600
    page.window_height = 600
    page.title = "Notepad"

    def changedark(event):
        page.theme_mode = ft.ThemeMode.DARK
        page.update()

    def changelight(event):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    # def change_font(event):
    #     page.fonts = {"Times New Roman": "times new roman bold italic.ttf"}
    #     TextBox.text_style = (ft.TextStyle(font_family="Times New Roman"),)

    page.padding = 0
    page.overlay.extend([file_picker, file_plicker])

    c1 = Container(
        bgcolor=colors.BLACK54,
        height=70,
        content=ft.Stack(
            controls=[
                Container(
                    content=ft.IconButton(
                        icon=ft.icons.DARK_MODE,
                        icon_size=20,
                        on_click=changedark,
                        bgcolor=colors.BLACK87,
                    ),
                    alignment=alignment.top_right,
                    margin=ft.margin.only(10, 15, 10, 0),
                ),
                Container(
                    content=ft.IconButton(
                        icon=ft.icons.LIGHT_MODE,
                        icon_size=20,
                        on_click=changelight,
                        bgcolor=colors.BLACK87,
                    ),
                    alignment=alignment.top_right,
                    margin=ft.margin.only(10, 15, 60, 0),
                ),
                Container(
                    content=ft.PopupMenuButton(
                        items=[
                            ft.PopupMenuItem(
                                text="Open",
                                icon=icons.FILE_OPEN,
                                on_click=lambda _: file_picker.pick_files(
                                    allowed_extensions=["txt"],
                                    file_type=ft.FilePickerFileType.ANY,
                                ),
                            ),
                            ft.PopupMenuItem(
                                text="Save", icon=icons.SAVE, on_click=write
                            ),
                            ft.PopupMenuItem(
                                text="Save As",
                                icon=icons.SAVE_AS,
                                on_click=lambda c_: file_plicker.save_file(
                                    allowed_extensions=["txt"],
                                    file_type=ft.FilePickerFileType.ANY,
                                ),
                            ),
                        ],
                        icon=icons.MENU,
                        tooltip="Options",
                    ),
                    margin=ft.margin.only(10, 15, 60, 0),
                ),
            ]
        ),
    )

    page.update()

    page.add(c1, c5)


ft.app(target=main)
