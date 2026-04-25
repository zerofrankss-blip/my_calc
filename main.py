import flet as ft

def main(page: ft.Page):
    page.title = "Calc"
    # Убираем все сложные настройки темы и размеров
    
    result = ft.Text(value="0", size=30)

    def btn_click(e):
        # Самый надежный способ достать текст
        txt = e.control.text
        if txt == "=":
            try:
                result.value = str(eval(result.value.replace('x', '*')))
            except:
                result.value = "Error"
        elif txt == "C":
            result.value = "0"
        else:
            result.value = txt if result.value == "0" else result.value + txt
        page.update()

    # Простая кнопка без лишних стилей
    def mk_btn(t, color="blue"):
        return ft.ElevatedButton(text=t, on_click=btn_click, expand=True)

    page.add(
        ft.Container(content=result, padding=10, bgcolor="black"),
        ft.Column(
            expand=True,
            controls=[
                ft.Row(controls=[mk_btn("7"), mk_btn("8"), mk_btn("9"), mk_btn("/")]),
                ft.Row(controls=[mk_btn("4"), mk_btn("5"), mk_btn("6"), mk_btn("x")]),
                ft.Row(controls=[mk_btn("1"), mk_btn("2"), mk_btn("3"), mk_btn("-")]),
                ft.Row(controls=[mk_btn("C"), mk_btn("0"), mk_btn("="), mk_btn("+")]),
            ]
        )
    )

if __name__ == "__main__":
    ft.app(target=main)

