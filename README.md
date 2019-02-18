README.md

# Biomhandler

## About

A python script to convert hdf5 biom files to json. Used in [Phinch](https://github.com/PhinchApp/Phinch). We use PyInstaller to package that script into a standablone executable. Follow these steps to generate the executable:

## Requirements

- Python 2 ([installation])(https://wiki.python.org/moin/BeginnersGuide/Download)
- Pip ([installation])(https://pip.pypa.io/en/stable/installing/)
- Virtualenv ([installation])(https://virtualenv.pypa.io/en/stable/installation/)

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

Or, on Windows:

```bash
cd biomhandler
virtualenv ./virtualenv
./virtualenv/Scripts/activate
```

Finally, install dependencies:

```bash
cat requirements.txt | xargs -n 1 -L 1 pip install
```

Or, on Windows:
```bash
cat requirements.txt | %{pip install $_}
```

## Packaging

The repository includes a pyinstaller specfile which tells pyinstaller how to create a standalone executable from the script. The resulting executable will be output at `/dist/biomhandler`. [More information on pyinstaller](http://pyinstaller.org/).

If you're on a windows system edit `biomhandler.spec` before packaging so that the `pathex` argument to the Analysis function points to scipy's `extra-dll` folder. It should look something like this:
```python
pathex=['C:/Users/pitch/Documents/biomhandler/virtualenv/Lib/site-packages/scipy/extra-dll']
```

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
