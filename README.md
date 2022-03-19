# Mediantor-cpp
 
Mediantor is a container that stores a collection of integers and provides only two operations:

* `insert(x)` - adds _x_ to collection;
* `take()` - returns the value of the median element in the collection and removes this element.

This project provides three implementations of Mediantor:

1. As a sorted list, with complexity _O(N)_ for each operation;
2. As sqrt decomposition, with complexity _O(sqrt(N))_ for each operation;
3. As two heaps, with complexity _O(log(N))_ for each operation.

## Setting up

Make sure you have Python 3.10 or newer.

Install pipenv, if you don't have it already:

```
$ pip install pipenv
```

Install dependencies:

```
$ pipenv sync
```

## Running

Run `$ pipenv run python demo.py` to manually test the project. See the section below about the structure of a test input.

Run `$ pipenv run pytest` to get results of automated testing.

## Structure of a test input

The first line of input should contain one single integer _n_ (1 ≤ _n_ ≤ 10<sup>5</sup>) - a number of operations with Mediantor.

The following _n_ lines should contain descriptions of these operations. If the line reads like

`1 x`,

it means that `insert(x)` will be performed (-10<sup>9</sup> ≤ _x_ ≤ 10<sup>9</sup>). If the line contains one single zero, it means that `take()` performed.

It is granted that `take()` will not be called when Mediantor is empty.

Manual tests should follow the same rules.

## Structure of a test output

For each called `take()`, output will contain a line with a returned number.

## Example

| Input       | Output      |
| ----------- | ----------- |
| 10<br>1 1<br>1 2<br>1 5<br>1 3<br>1 9<br>0<br>0<br>0<br>1 -3<br>0<br> | 3<br>2<br>5<br>1<br><br><br><br><br><br><br><br> |
