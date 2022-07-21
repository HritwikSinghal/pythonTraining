# file based key value store

## Installation.

1. #### Clone this repo

```sh
git clone --depth=1 -b master https://github.com/HritwikSinghal/pythonTraining
```

2. #### Install requirements.

```sh
pip3 install -r requirements.txt
``` 

#### Running.

- Make sure the file is executable.

```sh
./start.py --help

./start.py --p "X=10"
./start.py --put "X=10"

./start.py -g "X"
./start.py --get "X"

./start.py -d "X"
./start.py --delete "X"
```

## License

[GPLv3](/LICENSE)