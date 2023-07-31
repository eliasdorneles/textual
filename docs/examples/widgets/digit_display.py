from textual.app import App, ComposeResult
from textual.widgets import Label
from textual.widgets import DigitDisplay


class MyApp(App):
    BINDINGS = []

    def compose(self) -> ComposeResult:
        yield Label("Digits: 0123456789")
        yield DigitDisplay("0123456789")

        punctuation = " .+,XYZ^*/-="
        yield Label("Punctuation: " + punctuation)
        yield DigitDisplay(punctuation)

        equation = "x = y^2 + 3.14159*y + 10"
        yield Label("Equation: " + equation)
        yield DigitDisplay(equation)


if __name__ == "__main__":
    app = MyApp()
    app.run()