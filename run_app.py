import sys
from pathlib import Path

from streamlit.web import cli as stcli


def resolve_app_path():
    base_dir = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    frontend_dir = base_dir / "frontend"
    app_path = frontend_dir / "app.py"

    if not app_path.exists():
        app_path = base_dir / "app.py"

    if not app_path.exists():
        raise FileNotFoundError(
            f"Could not locate the Streamlit app. Checked: {frontend_dir / 'app.py'} and {base_dir / 'app.py'}"
        )

    return str(app_path)


if __name__ == "__main__":
    app_path = resolve_app_path()

    if str(Path(__file__).resolve().parent) not in sys.path:
        sys.path.insert(0, str(Path(__file__).resolve().parent))

    if str(Path(app_path).resolve().parent) not in sys.path:
        sys.path.insert(0, str(Path(app_path).resolve().parent))

    sys.argv = [
        "streamlit",
        "run",
        app_path,
        "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())
