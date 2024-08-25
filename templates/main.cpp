#include <iostream>

#include "a.h"
#include "b.h"

int main() {
    // 8192 + 8191 + 8190 + ...
    std::cout << Sum<8192>::value << std::endl;

    std::cout << a::GetSum() << std::endl;
    std::cout << b::GetSum() << std::endl;
}
