#!/bin/bash

# create a venv in the lessfilter directory and activate it
python3 -m venv lessfilter_env
LESSENV_ACTIVATE_PATH=$(realpath lessfilter_env/bin/activate)
echo $LESSENV_ACTIVATE_PATH

# activate the new environment
. $LESSENV_ACTIVATE_PATH

# install the python preprocessors into the venv
python setup.py install >/dev/null 

# activate the venv in the .lessfilter script
sed "s|<LESSENV_ACTIVATE_PATH>|$LESSENV_ACTIVATE_PATH|" lessfilter_template > lessfilter
chmod +x lessfilter

# try linking the lessfilter into the home directory
if [[ -e $HOME/.lessfilter ]]; then
    echo ".lessfilter already exists."
else
    echo "Linking .lessfilter into your home directory."
    ln -s $(realpath lessfilter) $HOME/.lessfilter
fi

if [[ -z "${LESSOPEN}" ]]; then
    echo -e "\n"
    echo "LESSOPEN is not set in your shell. Add something like "
    echo "'export LESSOPEN=\"| /usr/bin/lesspipe %s\""
    echo "to your bashrc/zshrc.'"
fi
