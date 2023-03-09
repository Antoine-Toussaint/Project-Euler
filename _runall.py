import importlib
import os
import inspect

if __name__ == "__main__":
    dir = "\\".join(inspect.getfile(lambda: None).split("\\")[:-1])
    max_problem = max([int(f.split('.')[0]) for f in os.listdir(
        dir) if f.split('.')[0].isnumeric()])

    for i in range(1, max_problem+1):
        i_str = str(i)
        if len(i_str) < 3:
            i_str = "0" * (3 - len(i_str)) + i_str
        try:
            module = importlib.import_module(f"{i_str}")
            module.solve()
        except ModuleNotFoundError:
            print("Module not found: ", i)
            pass
        except Exception as e:
            print(f"Error in Project-Euler_{i}: {e}")
