import os
class FileProcessor:
    def count_words(self, filepath):
        words = 0
        if not os.path.exists(filepath):
            raise FileNotFoundError
        with open(filepath, 'r') as fp:
            for line in fp.readlines():
                if bool(line.strip()):
                    words += len(line.strip().split(" "))
        return words