import argparse

class PrintName:
    def get_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-n', '--name', dest="print_names", help="Takes the name and prints it")
        options = parser.parse_args()
        if not options.print_names:
            parser.error("Please specify the name to print it on the console")

        return options

    def print_name(self, name):
        print(f'Hey there: {name}')

def main():
     pn = PrintName()
     options = pn.get_args()
     pn.print_name(options.print_names)

if __name__ == '__main__':
    main()