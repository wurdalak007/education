#include "Skeleton.h"
#include <iostream>

void Skeleton::Who_are_you() const {
    std::cout << "Hey, I'm a skeleton" << std::endl;
}

Skeleton::Skeleton() : defence(40), attack(7) {}