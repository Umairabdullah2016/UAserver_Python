import sysconfig
import subprocess
from pathlib import Path

def play(exe_args=None, create_missing_bin=False):
    """
    Runs BALDI.exe from the site-packages/BaldiWindows/bin folder via PowerShell.

    Parameters:
        exe_args (list of str): Optional arguments to pass to the executable.
        create_missing_bin (bool): If True, will create missing 'bin' folder.

    Returns:
        dict: {'stdout': ..., 'stderr': ..., 'returncode': ...}
    """
    if exe_args is None:
        exe_args = []

    # Get site-packages directory
    spd = Path(sysconfig.get_paths()["purelib"])

    # Define executable path
    exe_path = spd / "BaldiWindows" / "bin" / "BALDI.exe"

    # Check bin folder
    bin_folder = exe_path.parent
    if create_missing_bin and not bin_folder.exists():
        bin_folder.mkdir(parents=True, exist_ok=True)
        print(f"Created missing folder: {bin_folder}")

    # Check executable
    if not exe_path.is_file():
        raise FileNotFoundError(f"Executable not found: {exe_path}")

    # Build PowerShell command safely
    args_escaped = " ".join(f"'{a}'" for a in exe_args)
    command = f"& '{exe_path}' {args_escaped}".strip()

    # Run PowerShell command
    result = subprocess.run(
        ["powershell", "-ExecutionPolicy", "Bypass", "-Command", command],
        capture_output=True,
        text=True
    )

    # Print output (optional)
    print("STDOUT:\n", result.stdout)
    print("STDERR:\n", result.stderr)

    # Return output in dictionary
    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode
    }

# Example usage:
# play(["--help"])       # run with --help
# play([])               # run with no arguments
# play(["--help"], True) # create missing bin folder if needed
