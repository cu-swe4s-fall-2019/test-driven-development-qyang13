# test-driven-dev
This assignment covers components that process data from standard in and return
basic statistics along with data visualization using Python package matplotlib

# Environment
The program is based on python version 3.6.
The program uses python matplotlib for data visualization, to install matplotlib:
```
conda install matplotlib
```

# Unit Test
The program comes with detailed unit test that utilize the python library unittest. To run unittest, type the command:
```
python unit_test.py
```
The unit test will test for all the functions in all three libraries used by the program, including `math_lib`, `data_viz` and `get_data`.

# Usage
The program is executed through `viz.py`. For standard usage, try:
```
python viz.py -h
```
This program provides a simple shell script that generates two columns of random numbers. User can directly pipe those numbers to the program `viz.py` for processing:
```
bash gen_data.sh | python viz.py --out_file {your_file_name} --plot_type {your_plot_type}
```
For data visualization, three options are accepted:
- `box` for boxplot
- `hist` for histogram
- `combo` for both boxplot and histogram
