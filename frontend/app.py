"""
Codeunit: app.py
Author: Ethan Campbell
Date: 28-Mar-2026
Description: Starts the app.
            Always call first: "python3 -m streamlit run frontend/app.py"
"""

import sys
from pathlib import Path

import streamlit as st

workspace_root = Path(__file__).resolve().parent.parent
frontend_dir = Path(__file__).resolve().parent

for candidate in (workspace_root, frontend_dir):
    candidate_str = str(candidate)
    if candidate_str not in sys.path:
        sys.path.insert(0, candidate_str)


def page_path(filename: str) -> str:
    return str((frontend_dir / filename).resolve())


home = st.Page(page_path("main_page.py"), title="Home", icon="🏠")
encrypt_page = st.Page(page_path("encrypt_page.py"),
                       title="Encrypt a file", icon="🔐")
decrypt_page = st.Page(page_path("decrypt_page.py"),
                       title="Decrypt a file", icon="🔓")
send_page = st.Page(page_path("send_page.py"),
                    title="Send file", icon="📤")
create_keys_page = st.Page(page_path("create_keys_page.py"),
                           title="Create PGP or SSH key pair", icon="🗝️")
schedule_page = st.Page(page_path("schedule_page.py"),
                        title="Schedule a transfer", icon="📅")
import_keys = st.Page(page_path("import_keys.py"),
                      title="Import PGP keys", icon="📥")

pg = st.navigation([
    home,
    create_keys_page,
    encrypt_page,
    decrypt_page,
    send_page,
    schedule_page,
    import_keys
])

pg.run()
