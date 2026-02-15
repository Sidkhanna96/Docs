NDJSON -

- new line deliminated json files - collection of JSON objects are separated by lines (\n)
- Logs - fetch last n items quickly - insert or read a record from file need to parse the entire file

Objective:

- Write a program to read the format of the DB (spec/) files
- use it to parse the data/ files into NDJSON files

Requirements:

- spec files - have a name .csv

  - Are there any other formats for spec files apart from .csv
  - trusting the format is always - the spec files could be anything - YES
    - column name - name of keys in JSON object
    - width - Helps to track how many characters we need to parse
    - datatype - interpretting the data in the data files

- data files - have an associated name same as spec files but - date and .txt

  - Are there any other formats for spec files apart from .txt
  - Are dates always going to be YYYY-MM-DD format ?

- Convert all this data into NDJSON format

  - Each line in the file is a JSON object
  - output file name should input file name and inside the output/ directory

- Using Javascript (Not Typescript)

Task:

- Generate different test scenarios afterwards of data files
  - unit tests
  - functional ?
- OOP
- error handling
- Do ESLint
- think about edge cases
  - See if data files are there
  - Different structures of the spec files
  - Duplicate input ?
  - UTF-8 ?

Assumptions:

- Broke the task down into 2 steps

  - Fetching the files (SpecParser)
    - Fetches the files themselves
      - fetch file method - Gets a list of files
      - Constructs the data structure of the columns present in order
  - Outputting the data in NDJson format
    - outputs the data in NDJson format
    - Essentially just checks if the file format has

- Testing:

  - unit test
    - smallest component
  - functional test
    - for the whole interaction
  - integration test
    - for testing the whole different data sources

- Assumptions:
  - Assumes that specs folder already has the file and thats the datasource - can be modified further without impacting other parts of application to read from other datasources
  - Gets a list of files
  - Assumes that the data is in column order
    - if we have column name width datatype - the data below is represented of that and use the same deliminator
  - Assumes the data is present in the specs file though
  - If data
