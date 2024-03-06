sudo perf record -F 99 -a -g -- sleep 60 
sudo perf script | FlameGraph/stackcollapse-perf.pl | FlameGraph/flamegraph.pl > out.svg
