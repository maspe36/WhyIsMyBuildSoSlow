# Output to log.csv the following

# one,ten,hundrend
# <ms>,<ms>,<ms>
# ...

rm log.csv
echo "one,ten,hundred" >> log.csv

for i in $(seq 1 10);
do
  rm -rf build
	mkdir -p build
	cmake -S . -B build -G Ninja &> /dev/null

  # We are looking for milliseconds, not seconds. So we can't use `time`
  ts=$(date +%s%0N)
  cmake --build build --target one_include_path &> /dev/null
  one_end=$((($(date +%s%0N) - $ts)/1000000))

  rm -rf build
  mkdir -p build
  cmake -S . -B build -G Ninja &> /dev/null

  ts=$(date +%s%0N)
  cmake --build build --target ten_include_paths &> /dev/null
  ten_end=$((($(date +%s%0N) - $ts)/1000000))

  rm -rf build
  mkdir -p build
  cmake -S . -B build -G Ninja &> /dev/null

  ts=$(date +%s%0N)
  cmake --build build --target hundred_include_paths &> /dev/null
  hundred_end=$((($(date +%s%0N) - $ts)/1000000))

  echo "$one_end,$ten_end,$hundred_end" >> log.csv
done
