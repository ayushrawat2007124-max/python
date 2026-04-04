'''
5.   Create multiple suitable exceptions for a file handling program.
'''
# Custom Exceptions
class FileEmptyError(Exception):
    pass

class InvalidFileTypeError(Exception):
    pass

class TooManyLinesError(Exception):
    pass


def process_file(filename):
    try:
        # Check file extension
        if not filename.endswith(".txt"):
            raise InvalidFileTypeError("Only .txt files are allowed")

        with open(filename, "r") as file:
            content = file.readlines()

            # Check if file is empty
            if len(content) == 0:
                raise FileEmptyError("File is empty")

            # Check if file has too many lines
            if len(content) > 10:
                raise TooManyLinesError("File has more than 10 lines")

            print("File processed successfully!")
            print("Content:")
            for line in content:
                print(line.strip())

    except FileNotFoundError:
        print("Error: File not found")

    except InvalidFileTypeError as e:
        print("Error:", e)

    except FileEmptyError as e:
        print("Error:", e)

    except TooManyLinesError as e:
        print("Error:", e)

    except Exception as e:
        print("Unexpected Error:", e)


# Example usage
filename = input("Enter file name: ")
process_file(filename)