# includes
Including files is arguably the easiest and most expensive thing we can do in a single source file (or compilation unit).

This is because `#include` is a preprocessor directive that dumps the entire contents of the specified file into your source code. Even if no symbols from the included header are actually being used, we still pay the cost of copying the contents and parsing the source code.

Keep in mind, this added cost, will be paid for every single compilation unit that contains the unnecessary includes.

## Helpful Tools
Get the preprocessor output of any single source file
```bash
clang ./<file> -stdlib=libc++ -E &> <file>.txt
```

## Solutions
- Refactor massive header files
  - Having smaller header files gives consumers a better chance at including only whats strictly necessary for them
- Forward declarations
    - [Frowned upon for symbols defined in another project](https://google.github.io/styleguide/cppguide.html#Forward_Declarations)
    - Requires no external tooling 
    - Can obfuscate dependencies
- Include What You Use
  - [IWYU Project](https://github.com/include-what-you-use/include-what-you-use)
- Precompiled headers
  - Not a standard feature
  - Visual Studio projects autogenerate `stdafx.h` for new projects
- Modules
  - Standard feature (as of C++20)!
  - [Few compilers have full support](https://en.cppreference.com/w/cpp/compiler_support/20)
