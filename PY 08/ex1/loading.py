import sys
import importlib
from typing import Dict, Any

REQUIRED_PACKAGES = ["pandas", "numpy", "matplotlib", "requests"]

DESCRIPTIONS = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "requests": "Network access ready",
    "matplotlib": "Visualization ready",
}


def check_dependencies() -> Dict[str, Any]:
    print("LOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")
    installed: Dict[str, Any] = {}
    for pkg in REQUIRED_PACKAGES:
        try:
            module = importlib.import_module(pkg)
            version = getattr(module, "__version__", "unknown")
            desc = DESCRIPTIONS.get(pkg, "ready")
            print(f"[OK] {pkg} ({version}) - {desc}")
            installed[pkg] = module
        except ImportError:
            print(f"[MISSING] {pkg} - not installed")
    return installed


def show_install_help() -> None:
    print("\nInstall dependencies using pip:")
    print("pip install -r requirements.txt")
    print("\nOr using Poetry:")
    print("poetry install")


def analyze_data(mods: Dict[str, Any]) -> None:
    try:
        np = mods["numpy"]
        pd = mods["pandas"]
        plt = importlib.import_module("matplotlib.pyplot")
    except KeyError:
        print("Critical dependency missing.")
        return
    except ImportError:
        print("matplotlib.pyplot could not be loaded.")
        return
    print("\nAnalyzing Matrix data...")
    data = np.random.randn(1000)
    print("Processing 1000 data points...")
    df = pd.DataFrame({"matrix_signal": data})
    mean: float = float(df["matrix_signal"].mean())
    std: float = float(df["matrix_signal"].std())
    print("Generating visualization...")
    plt.hist(df["matrix_signal"], bins=30)
    plt.title(f"Matrix Data (mean={mean:.2f}, std={std:.2f})")
    plt.savefig("matrix_analysis.png")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    installed = check_dependencies()
    required = ["numpy", "pandas", "matplotlib"]
    if not all(pkg in installed for pkg in required):
        show_install_help()
        sys.exit(1)
    analyze_data(installed)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
