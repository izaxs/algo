use rusty::mylib;
use crate::dirlib::get_result2;
use rusty::another;
use rusty::filelib;

mod dirlib {
    pub fn get_result2() -> i32 {
        return 2
    }
}

fn main() {
    let result = get_result2();
    let result2 = mylib::get_result();
    let result3 = another::get_result5();
    let result4 = filelib::get_inner();
    println!("Hello, world! {} and {} and {} and {}", result, result2, result3, result4);
}
