from textual.app import App, ComposeResult
from textual import events
from textual.widgets import TextLog


class PrintLogger(TextLog):
    """A TextLog which captures printed text."""

    def on_print(self, event: events.Print) -> None:
        self.write(event.text)


class CaptureApp(App):
    def compose(self) -> ComposeResult:
        yield PrintLogger()

    def on_mount(self) -> None:
        self.query_one(TextLog).write("TextLog")
        self.query_one(TextLog).begin_capture_print()
        print("This will be captured!")
        self.query_one(TextLog).end_capture_print()
        print("This will *not* be captured")


if __name__ == "__main__":
    app = CaptureApp()
    app.run()
