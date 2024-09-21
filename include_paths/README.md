**Please note, this readme needs to be updated to fully reflect the content covered in the talk. It is quite close in but the takeaway is different.**

# include paths
When we give our compilers include paths (`-I`), we are giving them supplemental folders to search for our headers. 
Searching these folders requires our compilers to interact with our filesystem which is not free. 

I have observed a multi-million line project save ~2 minutes on a CI build by just removing two unnecessary include 
paths from all targets.

It is difficult to produce data on the impact of extraneous include directories on build times. This is because you need
a sufficiently large project and the patience to build it a number of times with and without your changes.

However, based on my observation and measuring from this small example, I purpose the following theory.
When you pass many include directories to a translation unit, each include directive has a slightly higher build 
time cost. This is because the compiler needs to first search the system include paths, and then search the include 
paths of all user defined include directories, in order.

## Study

In this example, on my system, I observed an average increase of **+0.7ms** per include directive between the 
`no_include_paths` and `lots_of_include_paths` targets with an additional `#include <memory>` in `main.cpp`.

All times in the tables are in ms. Data was collected using this bash script run from `WhyIsMyBuildSoSlow/include_paths`
and analyzed by viewing the output traces in perfetto.

```bash
for i in $(seq 1 10);
do
    rm -rf build && 
	mkdir -p build && 
	cmake -S . -B build -G Ninja && 
	cmake --build build --target no_include_paths && 
	ninjatracing -e build/.ninja_log > no_include_paths_$i.json
	
	rm -rf build && 
	mkdir -p build && 
	cmake -S . -B build -G Ninja && 
	cmake --build build --target lots_of_include_paths && 
	ninjatracing -e build/.ninja_log > lots_include_paths_$i.json
done
```

### Single Angle Include
```c++
#include <iostream>
```

| no_includes | lots_of_includes | Delta |
| ----------- | ---------------- | ----- |
| 512         | 514              | +2ms  |
| 508         | 517              | +9ms  |
| 507         | 513              | +6ms  |
| 515         | 514              | -1ms  |
| 508         | 512              | +4ms  |
| 508         | 513              | +5ms  |
| 521         | 513              | -8ms  |
| 510         | 514              | +4ms  |
| 510         | 512              | +2ms  |
| 510         | 512              | +2ms  |
Averages: +2.5ms in build time when additional include directories are defined

### Double Angle Includes
```c++
#include <iostream>
#include <memory>
```

| no_includes | lots_of_includes | Delta |
| ----------- | ---------------- | ----- |
| 515         | 513              | -2ms  |
| 511         | 515              | +4ms  |
| 514         | 517              | +3ms  |
| 511         | 515              | +4ms  |
| 513         | 514              | +1ms  |
| 514         | 515              | +1ms  |
| 510         | 520              | +10ms |
| 511         | 515              | +4ms  |
| 511         | 516              | +5ms  |
| 512         | 514              | +2ms  |
Averages: +3.2ms in build time when additional include directories are defined
