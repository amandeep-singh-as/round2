from lxml import etree
import os
from operations import Operations
import sys
from util import Util

util = Util()
operations = Operations()

class FileOperations:
    def process_files(self, input_dir_path: str, output_dir_path: str) -> None:
        if not os.path.exists(input_dir_path):
            print("Invalid dir path")
            sys.exit(1)

        if not os.path.exists(output_dir_path):
            os.makedirs(output_dir_path)

        completed_files, total_files = 0, len(os.listdir(input_dir_path))

        if total_files > 0:
            for filename in os.listdir(input_dir_path):
                util.printProgressBar(completed_files, total_files)
                if filename.endswith(".xml"):
                    input_file_path = os.path.join(input_dir_path, filename)
                    output_file_path = os.path.join(output_dir_path, filename.split('.')[0] + '_result.xml')

                    self.__process_xml_file(input_file_path, output_file_path)
                else:
                    print(f"{filename} will not be processed.")
                completed_files += 1
                util.printProgressBar(completed_files, total_files)
        else :
            print("No files exists in the given directory")
            sys.exit(1)

    def __process_xml_file(self, input_file_path: str, output_file_path: str) -> None:
        try:
            tree = etree.parse(input_file_path)

            root = tree.getroot()
            results = []

            for child in root:

                op_id = child.attrib.get('id')
                operation = child.tag

                if operation == 'addition':
                    result = operations.addition(child)
                elif operation == 'subtraction':
                    result = operations.subtraction(child)
                elif operation == 'division':
                    result = operations.division(child)
                elif operation == 'multiplication':
                    result = operations.multiplication(child)
                else:
                    continue

                results.append((op_id, result))

            self.__write_xml_file(output_file_path, results)
        except etree.XMLSyntaxError:
            print(f"Error while parsing {input_file_path}")
        except Exception as e:
            print(f"Some error occured while processing file : {input_file_path}.")
            print(e)
            print("Continuing to next file.")
    def __write_xml_file(self, output_file_path: str, results: list[tuple[str, int]]) -> None:
        root = etree.Element("expressions")
        for op_id, result in results:
            result_element = etree.SubElement(root, "result", id=str(op_id))
            result_element.text = str(result)

        tree = etree.ElementTree(root)
        try:
            tree.write(output_file_path, pretty_print=True, xml_declaration=True, encoding="UTF-8", method="xml")
        except Exception as e:
            print(f"Some error occured while writing file : {output_file_path}")
            print(e)
            print("Continuing to next file")