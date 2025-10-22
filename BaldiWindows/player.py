    import sysconfig
    import subprocess
    from pathlib import Path

    # get site-packages directory into a variable
    spd = sysconfig.get_paths()["purelib"]

    # build the executable path (Path makes this cross-platform-safe)
    exfd = Path(spd) / "BaldiwINDOWS" / "bin" / "MDM" / "BALDI.exe"

    # PowerShell invocation must quote the path if it contains spaces; use & 'path'
    # If you need to pass arguments to the exe, put them in exe_args
    exe_args = ["--help"]  # example args, make empty list [] if none
    args_escaped = " ".join(f"'{a}'" for a in exe_args)
    command = f"& '{exfd}' {args_escaped}".strip()

    def play():
        # sanity check
        if not exfd.is_file():
            raise FileNotFoundError(f"Executable not found: {exfd}")

        result = subprocess.run(
            ["powershell", "-ExecutionPolicy", "Bypass", "-Command", command],
            capture_output=True, text=True
        )
