import numpy as np


def run():
    x = [1,2,4]
    print(f"Mean   of {x}: {np.mean(x):.2f}")
    print(f"Median of {x}: {np.median(x):.2f}")

    return


if __name__ == "__main__":
    run()