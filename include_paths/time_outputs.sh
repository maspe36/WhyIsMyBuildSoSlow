if [ $# -eq 0 ];
then
  echo "$0: Missing arguments, make sure to pass the directory to dump logs"
  exit 1
fi

# Run a build for the given target 50 times and output a log file.
build_log() {
  rm $2/$1.csv
  mkdir -p $2/
  touch $2/$1.csv

  echo "Working on $2/$1.csv"

  for i in $(seq 1 50);
  do
    rm -rf build
  	mkdir -p build
  	cmake -S . -B build -G Ninja &> /dev/null

    # We are looking for milliseconds, not seconds. So we can't use `time`
    start=$(date +%s%0N)
    cmake --build build --target $1 &> /dev/null
    end=$((($(date +%s%0N) - $start)/1000000))

    echo "$end" >> $2/$1.csv
  done
}

build_log one_include_path $1
build_log ten_include_paths $1
build_log hundred_include_paths $1
build_log thousand_include_paths $1
