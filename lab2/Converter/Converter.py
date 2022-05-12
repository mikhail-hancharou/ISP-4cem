import argparse

from modules.JsonSerializerCreator import JsonSerializerCreator
from modules.TOMLSerializerCreator import TomlSerializerCreator
from modules.YAMLSerializerCreator import YamlSerializerCreator

parser = argparse.ArgumentParser(description='Process converting between formats.')
parser.add_argument('source', type=str,
                    help='source file path')
parser.add_argument('source_format', type=str,
                    help='source format')
parser.add_argument('destination', type=str,
                    help='destination file path')
parser.add_argument('format', type=str,
                    help='new format')

formats = {'JSON': JsonSerializerCreator(), 'YAML': YamlSerializerCreator(), 'TOML': TomlSerializerCreator()}


def setup():
    args = parser.parse_args()

    if args.format.upper() not in formats.keys():
        raise ValueError('Invalid format')

    serializer = formats[args.format.upper()].create_serializer()

    try:
        with open(args.source, 'r') as src:
            source_format = args.source_format
            if source_format.upper() not in formats.keys():
                raise ValueError(f'File should contain a format: {formats.keys()}')
            if source_format.upper() != args.format.upper():
                source_serializer = formats[source_format.upper()].create_serializer()
                with open(args.destination, 'w') as dst:
                    data = source_serializer.loads(src.read())
                    dst.write(serializer.dumps(data))
            else:
                raise ValueError(f'Source and destination format shouldn\'t be same')
    except IOError:
        print(f"Can't open file: {args.source}")


if __name__ == "__main__":
    setup()
