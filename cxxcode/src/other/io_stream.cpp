#include <iostream>
#include <string>
#include <sstream>

int read_integer() {
    std::string input_str;
    std::istringstream stream;
    int number;

    while (true) {
        std::cout << "Please enter an integer number: ";
        std::getline(std::cin, input_str); // Read the whole line into a string

        stream.clear(); // Clear any error state of the stream
        stream.str(input_str); // Set the contents of the stream to the new input

        // Attempt to read an integer from the stream
        stream >> number;

        // Check for extra non-whitespace characters after the number
        char hasExtraChar;
        if (stream.fail() || (stream >> hasExtraChar)) {
            // Input failure or extra non-whitespace characters after the number
            std::cout << "Invalid input. Try again.\n";
        } else {
            return number; // Valid integer entered
        }
    }
}

int main() {
    int input_number = read_integer();
    std::cout << "You entered the number: " << input_number << std::endl;
    return 0;
}
