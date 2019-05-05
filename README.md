Some simple lessfilter scripts in Python.

The `setup_lessfilters.sh` bash script must be run in the root directory of 
the repository and will set up a venv for the Python less preprocessors to 
run in. The preprocessors will be installed in the venv along with their 
dependencies. The path the the venv is then added to `.lessfilter`.

If no `.lessfilter` exists in `$HOME` yet, it will be automatically linked
there. Otherwise we have to merge the lessfilters manually.
