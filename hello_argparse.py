import argparse

parser = argparse.ArgumentParser(description='Hola Mundo con argparse')
parser.add_argument('--nombre', type=str, help='Tu nombre')

args = parser.parse_args()

print(f"Hola {args.nombre} desde argparse!")
