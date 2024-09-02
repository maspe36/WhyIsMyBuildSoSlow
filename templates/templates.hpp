#ifndef WHYISMYBUILDSOSLOW_TEMPLATES_HPP
#define WHYISMYBUILDSOSLOW_TEMPLATES_HPP

#include <iostream>

template <int N>
struct Sum {
    static const int value = N + Sum<N - 1>::value;
};

template <>
struct Sum<0>
{
    static const int value = 0;
};

#endif //`WHYISMYBUILDSOSLOW_TEMPLATES_HPP`
