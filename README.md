# Shopping Cart Project [![Build Status](https://travis-ci.com/kmalhotra13/shopping-cart-project.svg?branch=master)](https://travis-ci.com/kmalhotra13/shopping-cart-project)
<i><h3>Created by Kuran P. Malhotra</h3></i>
<i><p>Original commit Jan. 28 2018</p></i>

## Introduction

The purpose of this project is to allow the user to scan in and create a receipt for products within a predefined inventory list. 

## Technical Prerequisites

<b>Software Requirements</b>
- Git
- Anaconda 3.7
- Python 3.7
- Pip
- Packages listed in `/requirements.txt`

## Installation

In order to set up this applet, please download install the source code:

```sh
git clone git@github.com:kmalhotra/shopping-cart-project
cd shopping-cart-project/
```

Install the package dependencies:

```sh
pip install -r requirements.txt
```

## Usage

To use the application, just run the script using the following command:

```sh
python app/shopping_cart.py
```

From there, you will be prompted to select product items via their ID number. You can also look up a product by its ID number by typing "lookup" into the ID field. When you type "exit" in that field, a receipt will be generated by the system.

## Testing

From within the virtual environment, install the `pytest` package (first time only):

```sh
pip install pytest
```

Run tests:

```sh
pytest
```