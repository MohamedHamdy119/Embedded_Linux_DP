//Create a table for AscII code
#include <iostream>

int main() {
    std::cout << "+------+-------+" << std::endl;
    std::cout << "| Char | ASCII |" << std::endl;
    std::cout << "+------+-------+" << std::endl;
    for (int i = 0; i <= 127; i++) {
        std::cout << "|   " << static_cast<char>(i) << "   |   " << i << "   |" << std::endl;
    }
    std::cout << "+------+-------+" << std::endl;
    return 0;
}
