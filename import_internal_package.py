from demo.utils import mean, median

def run():
    x = [1,2,4]
    print(f"Mean   of {x}: {mean(x):.2f}")
    print(f"Median of {x}: {median(x):.2f}")
    
    return


if __name__ == "__main__":
    run()