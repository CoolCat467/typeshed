from idlelib.config import idleConf as idleConf
from idlelib.pyshell import PyShellEditorWindow
from tkinter import Event, Text
from typing import Any

class FormatParagraph:
    max_width: int
    editwin: PyShellEditorWindow
    def __init__(self, editwin: PyShellEditorWindow) -> None: ...
    @classmethod
    def reload(cls) -> None: ...
    def close(self) -> None: ...
    def format_paragraph_event(self, event: Event[Any], limit: int | None = ...) -> str: ...

def find_paragraph(text: Text, mark: str) -> tuple[str, str, str, str]: ...
def reformat_paragraph(data: str, limit: int) -> str: ...
def reformat_comment(data: str, limit: int, comment_header: str) -> str: ...
def is_all_white(line: str) -> bool: ...
def get_indent(line: str) -> str: ...
def get_comment_header(line: str) -> str: ...
def get_line_indent(line: str, tabwidth: int) -> tuple[int, int]: ...

class FormatRegion:
    editwin: PyShellEditorWindow
    def __init__(self, editwin: PyShellEditorWindow) -> None: ...
    def get_region(self) -> tuple[str, str, str, list[str]]: ...
    def set_region(self, head: str, tail: str, chars: str, lines: list[str]) -> None: ...
    def indent_region_event(self, event: Event[Any] | None = ...) -> str: ...
    def dedent_region_event(self, event: Event[Any] | None = ...) -> str: ...
    def comment_region_event(self, event: Event[Any] | None = ...) -> str: ...
    def uncomment_region_event(self, event: Event[Any] | None = ...) -> str: ...
    def tabify_region_event(self, event: Event[Any] | None = ...) -> str: ...
    def untabify_region_event(self, event: Event[Any] | None = ...) -> str: ...

class Indents:
    editwin: PyShellEditorWindow
    def __init__(self, editwin: PyShellEditorWindow) -> None: ...
    def toggle_tabs_event(self, event: Event[Any]) -> str: ...
    def change_indentwidth_event(self, event: Event[Any]) -> str: ...

class Rstrip:
    editwin: PyShellEditorWindow
    def __init__(self, editwin: PyShellEditorWindow) -> None: ...
    def do_rstrip(self, event: Event[Any] | None = ...) -> None: ...
