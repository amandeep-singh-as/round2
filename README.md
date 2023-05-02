# Nordea Round 2 - Technical Assesment

Implement an application which calculates top-level operations from input files and store results in output
files in XML format. Use best programming practices based on your experience and note you can use external
libraries from common sources. We need to be able to build the application so please provide build instructions or
scripts. The solution size in ZIP archive should be reasonable. You can implement the solution with different level of completeness depending on the time which you spend for the solution. You can use the language of your choice, but
it needs to be built and run on Windows.

## Installation

Use [pip](https://pip.pypa.io/en/stable/) to install all the dependencies

```bash
pip install requirements.txt
```

## Usage

Open terminal in the project directory
```bash
python app.py <input_directory_path> <output_directory_path>
```

## Dependencies

* [lxml](https://lxml.de/) : Library for processing XML and HTML files effiecentlty. 

* [Progress Bar](https://stackoverflow.com/questions/3173320/text-progress-bar-in-terminal-with-block-characters) : Used this piece of code for visible progress over the files.

## File and Program Structure

* [app.py](./app.py) : This file contains the main code for the program, that reads the `XML` files and perform the operations and creats the resultant `XML` files.
* [operations.py](./operations.py) : `Operation class` contains all the valid operations that are described in the `XML` file. We can just add new operations and modify the how they operate.
* [fileOperations.py](./fileOperations.py) : `FileOperation class` contains method to read, write and process files based on the extension, (currently on `XML`). If wanted we can modify this class to add various methods to handle different kinds of file types.
* [util.py](./util.py) : `Util class` contains additional methods, such as printing progress bar.
* [requirements.txt](./requirements.txt) : `pip freeze` file that has all the dependencies.

<hr/>

## Assumptions
<hr/>

* For **subtraction** operation, I have considered there can only be two variables.
* For **division** operation, I have considered there can only be two variables.
* If there is problem with one of the `XML` file in the directory, that file will be skipped and program will move to the next file if avalable.
* If the `<output_dir_path>` does not exists it will be created along with resultant `XML`.
* All the values in `XML` are **int** and result values are also  **int**.
