# templates
Having deeply nested templates can have a sizeable impact on your compilation times. This is because compilers employ a 
technique formerly known as "_monomorphization_" when parsing generic code (namely, templates). In short, this means that 
the compiler pastes all the template specializations of a compilation unit into the source code. This is in fact helpful, 
as it allows us to write powerful generic code without taking any run-time performance hits (zero cost abstractions).

Keep in mind, that monomorphization costs are paid per compilation unit. So poor abstractions can balloon compilation 
times disproportionately to their equivalent run-time savings.

## Helpful Tools

### [cppinsights](https://cppinsights.io/)
"See your source code through the eyes of a compiler."

## Solutions
- Consider whether you actually need to use TMP (Template Meta Programming) for your use case
  - `constexpr` and `consteval` can go a long way 
- Re-evaluate your API. 
  - Do you need to be generic over that extra type? 
  - Can you eliminate recursion?
- Explicit template instantiation in a precompiled header or module
  - When you explicitly instantiate a template, you'll always pay the compilation cost, even if that instantiation is no longer used elsewhere in the project.
