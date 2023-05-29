import math
from lab_serializer.serializers.json_serializer import Json
from lab_serializer.serializers.xml_serializer import Xml


def main():
    serializer = Json()
    serializer.dumps("Hello")


if __name__ == "__main__":
    main()
