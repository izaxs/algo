pub mod inner;

pub fn get_inner() -> i32 {
    inner::get_inner_result()
}