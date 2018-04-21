#[macro_use]
extern crate cpython;

use cpython::{Python, PyResult};

fn count_doubles(_py: Python, val: &str) -> PyResult<u64> {
    let mut total = 0;

    for (c1, c2) in val.chars().zip(val.chars().skip(1)) {
        if c1 == c2 {
            total += 1;
        }
    }

    Ok(total)
}

fn fizz_buzz_sum(_py: Python, limit: u64) -> PyResult<u64> {
    Ok((1..limit)
        .filter(|x| x % 3 == 0 || x % 5 == 0)
        .sum())
}

py_module_initializer!(example, initexample, PyInit_example, |py, m| {
    m.add(py, "count_doubles", py_fn!(py, count_doubles(val: &str)))?;
    m.add(py, "fizz_buzz_sum", py_fn!(py, fizz_buzz_sum(limit: u64)))?;

    Ok(())
});
