# Gendiff (Hexlet Python Project Level 2)

[![Actions Status](https://github.com/neihaoo/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/neihaoo/python-project-lvl2/actions)
[![Actions Status](https://github.com/neihaoo/python-project-lvl2/workflows/Python%20CI/badge.svg)](https://github.com/neihaoo/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/2ffa639f6c265e8b3d62/maintainability)](https://codeclimate.com/github/neihaoo/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/2ffa639f6c265e8b3d62/test_coverage)](https://codeclimate.com/github/neihaoo/python-project-lvl2/test_coverage)

## Table of Contents

- [Install](#Install)
- [Usage](#Usage)
  - [JSON](#JSON)
  - [YAML](#YAML)

## Install

```sh
$ make package-install
```

[![asciicast](https://asciinema.org/a/9tQrRPZ4SQb8SxwvO52SOMGg4.svg)](https://asciinema.org/a/9tQrRPZ4SQb8SxwvO52SOMGg4)

## Usage

### JSON

```sh
$ gendiff first_file.json second_file.json
```

[![asciicast](https://asciinema.org/a/dsiDkKVqfohcQAL5QnNY9RzX0.svg)](https://asciinema.org/a/dsiDkKVqfohcQAL5QnNY9RzX0)
[![asciicast](https://asciinema.org/a/4UE3uDyVcVLGNZ6IHnzJ3K7bA.svg)](https://asciinema.org/a/4UE3uDyVcVLGNZ6IHnzJ3K7bA)

```sh
$ gendiff --format plain first_file.json second_file.json
```

[![asciicast](https://asciinema.org/a/iWbqam1l9FpIswBo3fX3kB0DQ.svg)](https://asciinema.org/a/iWbqam1l9FpIswBo3fX3kB0DQ)

### YAML

```sh
$ gendiff first_file.yaml second_file.yaml
```

[![asciicast](https://asciinema.org/a/oI4d51XCk4P7ayh6dWZsKe6LR.svg)](https://asciinema.org/a/oI4d51XCk4P7ayh6dWZsKe6LR)
[![asciicast](https://asciinema.org/a/9rFcqs8AdE2PovjloanxXoofA.svg)](https://asciinema.org/a/9rFcqs8AdE2PovjloanxXoofA)

```sh
$ gendiff --format plain first_file.yaml second_file.yaml
```

[![asciicast](https://asciinema.org/a/g4yVKBwzuVQexJnZCSUPELdcd.svg)](https://asciinema.org/a/g4yVKBwzuVQexJnZCSUPELdcd)
