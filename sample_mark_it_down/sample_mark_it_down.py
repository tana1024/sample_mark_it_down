"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from markitdown import MarkItDown

class Extruct(rx.State):
    """The app extruct."""

    ...
    contents = "abc"

    def execute(self):
        markitdown = MarkItDown()
        result = markitdown.convert("https://www.jpx.co.jp/corporate/investor-relations/ir-library/securities-reports/tvdivq0000008r0t-att/view23-1.pdf")
        print(result.text_content[:20000])
        self.contents = result.text_content[:20000].replace('\n', '<br>').replace('<br><br>', '<br>')

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            rx.link(
                "2023年度第1四半期報告書(サンプル)",
                href="https://www.jpx.co.jp/corporate/investor-relations/ir-library/securities-reports/tvdivq0000008r0t-att/view23-1.pdf",
                target="_blank",
            ),
            rx.button(
                "ファイルの内容抽出",
                on_click=Extruct.execute,
            ),
            rx.html(
                Extruct.contents,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )

app = rx.App()
app.add_page(index)
