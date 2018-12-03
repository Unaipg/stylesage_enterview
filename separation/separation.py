"""Module to separate data on multiple formats """
import sys

def separate(data: any, step: int = 3, separator: str = ',') -> str:
    """Divide the input grouped in groups of `step` items separated by the `separator` string"""
    data = str(data)[::-1]
    return separator.join([data[n:n+step][::-1] for n in range(0, len(data), step)][::-1])

if __name__ == '__main__':
    try:
        print(separate(sys.argv[1]))
    except IndexError:
        print("Falta el parámetro de entrada")
