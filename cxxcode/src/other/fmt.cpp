#include <vector>

#define FMT_HEADER_ONLY
#include "fmt/core.h"
#include "fmt/chrono.h"
#include "fmt/ranges.h"
#include "fmt/color.h"

void run_fmt()
{
    fmt::print("Hello, world!\n");
    fmt::print("The answer is {}.\n", 42);
    fmt::print("I'd rather be {1} than {0}.\n", "right", "happy");

    using namespace std::literals::chrono_literals;
    fmt::print("Default format: {} {}\n", 42s, 100ms);
    fmt::print("strftime-like format: {:%H:%M:%S}\n", 3h + 15min + 30s);

    std::vector<int> v = {1, 2, 3};
    fmt::print("{}\n", v);

    fmt::print(fg(fmt::color::crimson) | fmt::emphasis::bold,
                "Hello, {}!\n", "world");
    fmt::print(fg(fmt::color::floral_white) | bg(fmt::color::slate_gray) |
                fmt::emphasis::underline, "Olá, {}!\n", "Mundo");
    fmt::print(fg(fmt::color::steel_blue) | fmt::emphasis::italic,
                "你好{}！\n", "世界");
}



int main()
{
    run_fmt();

    return 0;
}