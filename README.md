# Why is my build so slow? Compilation Profiling and Visualization

## Prerequisites

All of these examples run on Linux.

| Tool  | Version   |
|-------|-----------|
| Ninja | \>=1.10*  |
| Clang | \>= 9.0** |
| CMake | \>=3.16   |

\* These techniques may work with older ninja versions (even all the way back to the 1.0). 1.10 is just the version I'm using.

\** It seems around clang-19 single file visualizations got harder to view in perfetto as includes got split into different "tracks"

## 