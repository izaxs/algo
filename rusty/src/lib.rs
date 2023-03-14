pub mod another;
pub mod nested;
pub mod filelib;

pub mod mylib {
    pub fn get_result() -> i32 {
        return 2
    }
}

pub fn run_something() -> i32 {
    nested::something::get_result()
}

#[test]
fn it_works() {
    assert_eq!(2 + 2, 4);
}

#[cfg(test)]
mod tests {
    use crate::mylib::get_result;

    #[test]
    fn it_works_too() {
        let result = get_result() + 2;
        assert_eq!(result, 4);
    }

    #[test]
    #[ignore = "always fail"]
    fn it_doesnt_work() {
        let result = get_result() + 3;
        assert_eq!(result, 4);
    }
}
