# Pochecker

a tool to rename outdated documents' `po` files (Originally it is not removed outdated `po` files, just rename them to `.po.outdated` )

## install

via pip:

```sh
pip install Pochecker
```

via pipx: (recommended)

```sh
pipx install Pochecker
```

or install from source:

```sh
git clone https://github.com/mmdbalkhi/Pochecker.git
cd Pochecker && python3 setup.py install
```

## usage

- help

```sh
pochecker --help
```

```sh
pochecker -p docs/ -e rst
```
