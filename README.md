# file-type-converters
A collection of scripts to convert files into different formats

### json2yaml
Convert a json file into a yaml file. 

`python json2yaml.py <inputfile> <outputfile>`

Output file parameter is optional. If no output file is provided, the yaml file will be created with the same name as the original json.

##### Example:
An example input file is provided in the `/examples` directory.  
To run the example:

`python json2yaml.py examples/j2y_example.json`

You will notice that a file `examples/j2y_example.yml` is created when the script has finished. Additionally, a log file `logs/json2yaml.log` has been created. If there are errors running the script, check this log file.


### yaml2json
Convert a json file into a yaml file.

`python yaml2json.py <inputfile> <outputfile>`

Output file parameter is optional. If no output file is provided, the json file will be created with the same name as the original yaml.

##### Example:
An example input file is provided in the `/examples` directory.  
To run the example:

`python yaml2json.py examples/y2j_example.yml`

You will notice that a file `examples/y2j_example.json` is created when the script has finished. Additionally, a log file `logs/yaml2json.log` has been created. If there are errors running the script, check this log file.