if [ -d "generated/" ]; then
  echo "'generated/' already exists. Skipping this run."
  exit 1;
fi

for i in $(seq 1 100);
do
	mkdir -p generated/folder_$i
	echo "constexpr int kFile$i = $i;" >> generated/folder_$i/file_$i.hpp
done

exit 0;
