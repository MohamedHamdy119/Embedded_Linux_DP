//RIGHT angle triangle

#include <iostream>

int rows;

int main() {
    std::cout << "Enter The Number of Rows: ";
    std::cin >> rows;

    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= i; j++) {
            std::cout << "* ";
        }
        std::cout << std::endl;
    }

    return 0;
}