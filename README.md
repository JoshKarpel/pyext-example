# What?

This is an example of using Rust to write a CPython extension module via [rust-cpython](https://github.com/dgrunwald/rust-cpython).
It exposes three functions:
* `count_doubles`, which determines the number of pairs of matching characters in a string.
* `fizz_buzz_sum`, which determines the sum of all numbers smaller than a given number that are divisible by 3 or 5.
* `prime_factorization`, which determines the prime factors of a number.

It includes some simple benchmark tests against equivalent Python and NumPy functions.

# How?

## Compiling and Importing the Extension Module

1. [Install Rust](https://www.rust-lang.org/install.html).
1. Clone the repository (`git clone https://github.com/JoshKarpel/pyext-example`) and enter the repository directory (`cd pyext-exmaple`).
1. Compile the Rust code using either `cargo build` or `cargo build --release`.
1. Look in `target/` for either a `debug/` or `release/` directory.
   Take the `example.dll` file from that directory, move it up to the base directory of the repository (next to this readme), and rename it `example.pyd`.
1. You can now import `example` as if it was a Python module (`import example`).

## Running Benchmarks

This project includes some benchmarking tests against Python and NumPy versions of the functions implemented in Rust.
To run them, first install the extra Python dependencies: from the repository directory, run `pip install -r requirements.txt`.

There are four groups of benchmarks.
The `pytest` commands (run from the repository directory) to look at them individually are

* `pytest -k "on_prime"` - prime factorization, on a prime number.
* `pytest -k "on_composite"` - prime factorization, on a composite number.
* `pytest -k "fizz"` - the FizzBuzz sum.
* `pytest -k "doubles"` - the doubled-character counter.

On my desktop, with a release build (`cargo build --release`), the Rust functions typically run 10-50 times faster than the Python or NumPy functions.
Of course, these functions are not representative of any real workflow, so those numbers don't really mean anything.
The important thing is that writing Rust extensions clearly provides solid performance with a reasonable inter-operation syntax.
