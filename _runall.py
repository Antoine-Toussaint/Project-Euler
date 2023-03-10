import importlib
import os
import inspect
import platform

if __name__ == "__main__":
    separator = "\\" if platform.system() == "Windows" else "/"

    dir = separator.join(inspect.getfile(lambda: None).split(separator)[:-1])

    files = [f.split('.')[0] for f in os.listdir(
        dir) if f.split('.')[0].isnumeric() and f.split('.')[1] == "py"]

    files.sort()

    for f in files:
        try:
            module = importlib.import_module(f"{f}")
            module.solve()
        except ModuleNotFoundError:
            print("Module not found: ", f)
            pass
        except Exception as e:
            print(f"Error in Project-Euler_{f}: {e}")
