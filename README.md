README.md

# Biomhandler

## About

A python script to convert hdf5 biom files to json. Used in [Phinch](https://github.com/PhinchApp/Phinch). We use PyInstaller to package that script into a standablone executable. Follow these steps to generate the executable:

## Requirements

- Python 2
- Pip
- Virtualenv

## Install

First, clone the repo via git:

```bash
git clone https://github.com/PhinchApp/biomhandler.git
```

Then, create and active a python virtual environment:

```bash
cd biomhandler
virtualenv ./virtualenv
source ./virtualenv/bin/activate
```

Finally, install dependencies:

```bash
cat requirements.txt | xargs -n 1 -L 1 pip install
```

## Packaging

The repository includes a pyinstaller specfile which tells pyinstaller how to create a standalone executable from the script. The resulting executable will be output at `/dist/biomhandler`. [More information on pyinstaller](http://pyinstaller.org/).

```bash
pyinstaller biomhandler.spec
```

## Usage

Using Python:

```bash
python biomhandler.py path-to-hdf5-biom-file
```

Using the standablone executable:

```bash
./dist/biomhandler path-to-hdf5-biom-file
```

## License
The BSD 2-Clause License
