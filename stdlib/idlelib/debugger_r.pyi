from collections.abc import Hashable
from idlelib import debugger as debugger, rpc as rpc
from idlelib.pyshell import PyShellEditorWindow
from types import CodeType, FrameType, TracebackType
from typing import Any

debugging: int
idb_adap_oid: str
gui_adap_oid: str

frametable: dict[int, FrameType]
dicttable: dict[int, dict[Any, Any]]
codetable: dict[int, CodeType]
tracebacktable: dict[int, TracebackType]

def wrap_frame(frame: FrameType) -> int: ...
def wrap_info(info: tuple[BaseException, str, TracebackType] | None) -> tuple[BaseException, str, int] | None: ...

class GUIProxy:
    conn: rpc.RPCClient
    oid: str
    def __init__(self, conn: rpc.RPCClient, gui_adap_oid: str) -> None: ...
    def interaction(
        self, message: str, frame: FrameType, info: tuple[BaseException, str, TracebackType] | None = ...
    ) -> None: ...

class IdbAdapter:
    idb: debugger.Idb
    def __init__(self, idb: debugger.Idb) -> None: ...
    def set_step(self) -> None: ...
    def set_quit(self) -> None: ...
    def set_continue(self) -> None: ...
    def set_next(self, fid: int) -> None: ...
    def set_return(self, fid: int) -> None: ...
    def get_stack(self, fid: int, tbid: TracebackType | None) -> tuple[FrameType, int]: ...
    def run(self, cmd: str | CodeType) -> None: ...
    def set_break(self, filename: str, lineno: str) -> str | None: ...
    def clear_break(self, filename: str, lineno: str) -> str | None: ...
    def clear_all_file_breaks(self, filename: str) -> str | None: ...
    def frame_attr(self, fid: int, name: str) -> Any: ...
    def frame_globals(self, fid: int) -> int: ...
    def frame_locals(self, fid: int) -> int: ...
    def frame_code(self, fid: int) -> int: ...
    def code_name(self, cid: int) -> str: ...
    def code_filename(self, cid: int) -> str: ...
    def dict_keys(self, did: int) -> None: ...
    def dict_keys_list(self, did: int) -> list[Hashable]: ...
    def dict_item(self, did: int, key: Hashable) -> str: ...

def start_debugger(rpchandler: rpc.RPCHandler, gui_adap_oid: str) -> str: ...

class FrameProxy:
    def __init__(self, conn: rpc.RPCClient, fid: int) -> None: ...
    def __getattr__(self, name: str) -> Any: ...

class CodeProxy:
    def __init__(self, conn: rpc.RPCClient, oid: int, cid: int) -> None: ...
    def __getattr__(self, name: str) -> str | None: ...

class DictProxy:
    def __init__(self, conn: rpc.RPCClient, oid: int, did: int) -> None: ...
    def keys(self) -> list[Hashable]: ...
    def __getitem__(self, key: Hashable) -> str: ...
    def __getattr__(self, name: str) -> None: ...

class GUIAdapter:
    conn: rpc.RPCClient
    gui: debugger.Debugger
    def __init__(self, conn: rpc.RPCClient, gui: debugger.Debugger) -> None: ...
    def interaction(self, message: str, fid: int, modified_info: tuple[BaseException, str, TracebackType] | None) -> None: ...

class IdbProxy:
    oid: str
    conn: rpc.RPCClient
    shell: PyShellEditorWindow
    def __init__(self, conn: rpc.RPCClient, shell: PyShellEditorWindow, oid: str) -> None: ...
    def call(self, __methodname: str, *args: Any, **kwargs: Any) -> Any: ...
    def run(self, cmd: str | CodeType, locals: dict[str, Any]) -> None: ...
    def get_stack(self, frame: FrameType, tbid: int) -> tuple[list[tuple[FrameProxy, int]], int]: ...
    def set_continue(self) -> None: ...
    def set_step(self) -> None: ...
    def set_next(self, frame: FrameProxy) -> None: ...
    def set_return(self, frame: FrameProxy) -> None: ...
    def set_quit(self) -> None: ...
    def set_break(self, filename: str, lineno: int) -> str | None: ...
    def clear_break(self, filename: str, lineno: int) -> str | None: ...
    def clear_all_file_breaks(self, filename: str) -> str | None: ...

def start_remote_debugger(rpcclt: rpc.RPCClient, pyshell: PyShellEditorWindow) -> debugger.Debugger: ...
def close_remote_debugger(rpcclt: rpc.RPCClient) -> None: ...
def close_subprocess_debugger(rpcclt: rpc.RPCClient) -> None: ...
def restart_subprocess_debugger(rpcclt: rpc.RPCClient) -> None: ...
