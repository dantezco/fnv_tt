import re


class LatexTable:
    def __init__(self, name: str, path: str, regex: str) -> None:
        self._name = name
        self._data = []
        self._index = 0
        self._path = path
        self._regex = regex
        self.parse()

    def parse(self) -> None:
        with open(self._path, 'r') as file:
            for line in file.readlines():
                line_parsed = re.match(self._regex, line)
                if line_parsed:
                    self._data.append(line_parsed.groups())

    def print(self) -> None:
        for line in self._data:
            print(line)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._data):
            result = self._data[self._index]
            self._index += 1
            return result
        raise StopIteration

    def __str__(self):
        return f'Table {self._name} with {len(self._data)} lines of data'
