pub fn get_result5() -> i32 {
    return 4
}

pub fn get_something() -> i32 {
    super::nested::something::get_result()
}