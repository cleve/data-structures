# Data Structure

Data structures are written in Python3. You can find the most common structures, 
with a friendly CLI for each one. The structures are separated into 
packages that allow you to use/include it for your particular purpose.

## Trees

The tree structures are under the **trees** directory. To use the interactive
CLI, you need to run:

```python
python3 cli_tree.py
```

## Linked list

The list structure is under the **linked_list** directory. To use the interactive
CLI, you need to run:

```python
python3 cli_list.py
```

## Hash Table

The hash structure is under the **hash** directory. To use the interactive
CLI, you need to run:

```python
python3 cli_hash.py
```

The current hash function is based in the simple length of the value provided. To solve collisions
a linked list is implemented for the hash involved.

## DEV

In every main class there is a DEBUG variable, setting it to True, you will be able to 
see extra information in the CLI.

## Unittest

Execute the next command in the root directory:

```sh
# -v to add more details, you can remove this arg
python -m unittest discover tests -v
```