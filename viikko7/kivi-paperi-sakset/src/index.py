from ui import UI
from konsoli_io import KonsoliIO


def main():
    io = KonsoliIO()
    kayttoliittyma = UI(io)
    kayttoliittyma.kaynnista()


if __name__ == "__main__":
    main()
