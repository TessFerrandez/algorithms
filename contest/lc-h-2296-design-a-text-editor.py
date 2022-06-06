class TextEditor:
    def __init__(self):
        self.cursor = 0
        self.text = ""

    def addText(self, text: str) -> None:
        # adds text to where the cursor is, cursor is at right of text
        self.text = self.text[: self.cursor] + text + self.text[self.cursor:]
        self.cursor += len(text)

    def deleteText(self, k: int) -> int:
        # delete k chars to the left of cursor - returns # actual deleted chars
        n_chars = min(k, self.cursor)
        self.text = self.text[: self.cursor - n_chars] + self.text[self.cursor:]
        self.cursor -= n_chars
        return n_chars

    def cursorLeft(self, k: int) -> str:
        # moves cursor left k chars - returns last min(10, len) chars to the left of cursor
        # where len is chars left of cursor
        self.cursor -= min(self.cursor, k)
        if self.cursor < 10:
            return self.text[: self.cursor]
        return self.text[self.cursor - 10: self.cursor]

    def cursorRight(self, k: int) -> str:
        # moves cursor right k chars - returns the last min(10, len) chars to the left of cursor
        # where len in chars left of cursor
        n = len(self.text)
        self.cursor = min(n, self.cursor + k)
        if self.cursor <= 10:
            return self.text[: self.cursor]
        return self.text[self.cursor - 10: self.cursor]


te = TextEditor()
te.addText("bxyackuncqzcqo")
assert te.cursorLeft(12) == "bx"
assert te.deleteText(3) == 2
assert te.cursorLeft(5) == ""
te.addText("osdhyvqxf")
assert te.cursorRight(10) == "yackuncqzc"

te = TextEditor()
te.addText("leetcode")
assert te.deleteText(4) == 4
te.addText("practice")
assert te.cursorRight(3) == "etpractice"
assert te.cursorLeft(8) == "leet"
assert te.deleteText(10) == 4
assert te.cursorLeft(2) == ""
assert te.cursorRight(6) == "practi"
