# Why is my build so slow? Compilation Profiling and Visualization

## Prerequisites

All of these examples run on Linux.

| Tool  | Version     |
|-------|-------------|
| Ninja | \>=1.10*    |
| Clang | \>= 9.0**   |
| CMake | \>=3.16     |
| ninjatracing | \>=0.1.0*** | 

\* These techniques may work with older ninja versions (even all the way back to the 1.0). 1.10 is just the version I'm using.

\** It seems around clang-19 single file visualizations got harder to view in perfetto as includes got split into different "tracks"

\*** This actually isn't released on PyPI yet. The PR to add the infrastructure is [here](https://github.com/nico/ninjatracing/pull/36).

## Tools Used
For my talk, I am primarily using these 3 tools, in order of usage. 

### [perfetto](https://ui.perfetto.dev/)
> System profiling, app tracing and trace analysis

Slick trace viewer. Compatabile with many different tracing formats, but primarily used in this talk 
for the chrome tracing format. Also, converts any loaded trace into a SQL DB that can be queried to answer specific questions.


### [ninjatracing](https://github.com/nico/ninjatracing)
> Converts one (or several) .ninja_log files into chrome's about:tracing format.
>
> If clang -ftime-trace .json files are found adjacent to generated files they
are embedded.

The "missing link" between visualizing `.ninja_log`s directly in perfetto and individual translation unit `.json`s coming out of clang's `-ftime-trace`. 

Also needed to visualize newer `.ninja_log` version (v6) that come out of the latest ninja releases.

### [ClangBuildAnalyzer](https://github.com/aras-p/ClangBuildAnalyzer)
>  output "what took the most time" summary

Extremely useful tool when just beginning to investigate build times. Helps identify trouble areas quickly.

## Running Examples
All of the examples in this repo are self contained and can be built like so
```bash
cd <example>
mkdir -p build
cmake -S . -B build -G Ninja 
cmake --build build --target <target>
```

To analyze the output, generate a combined trace using `ninjatracing`

```bash
ninjatracing -e build/.ninja_log > combined_trace.json
```

Then open the trace file in perfetto. Happy profiling.

## Other Useful Tools
These are tools that I didn't use for one reason or another, but I came across while doing research for this talk

### [CompileScore](https://github.com/Viladoman/CompileScore)
> VisualStudio extension and utilities used to display and highlight compilation profiling data. Know the real compilation cost of your code directly inside Visual Studio. Keep the compile times in check.

Requires Visual Studio and MSVC. I build on Linux primarily.