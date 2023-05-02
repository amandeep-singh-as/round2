from fileOperations import FileOperations
import sys

fileOperations = FileOperations()

def process_files(input_dir_path: str, output_dir_path: str) -> None:
    fileOperations.process_files(input_dir_path=input_dir_path, output_dir_path=output_dir_path)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python app.py <input_folder> <output_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    process_files(input_folder, output_folder)

