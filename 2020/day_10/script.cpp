#include <iostream>
#include <fstream>
#include <list>
#include <unordered_map>
#include <tuple>
#include <sstream>
#include <string>

std::unordered_map<std::string, long> part_2_cache =  {};


std::list<int> get_lines() {
    std::ifstream input_stream("input");
    if(!input_stream) {
        std::cout << "Error opening input file" << std::endl ;
        exit(-1);
    }

    std::string line;
    std::list<int> ints_list = {};
    while (std::getline(input_stream, line)) {
        ints_list.push_back(std::stoi(line));
    }

    ints_list.sort();
    return ints_list;
}

void part_1(std::list<int> ints_list) {
    int previous = 0;
    int diffs_one = 0;
    int diffs_three = 1; // for our device end
    for (int n : ints_list) {
        if (n - previous == 1) {
            diffs_one++;
        }
        if (n - previous == 3) {
            diffs_three++;
        }
        previous = n;
    }

    std::cout << "Part 1: " << diffs_one << " diffs of 1 and "
        << diffs_three << " diffs of three. Result is: " << diffs_one * diffs_three << std::endl;
}

std::string part_2_make_cache_key(int previous, std::list<int> adapters) {
  std::ostringstream string_stream;
  string_stream << previous;
  for (int adapter : adapters) {
      string_stream << adapter;
  }
  return string_stream.str();
}

long part_2_rec(int previous, std::list<int> adapters) {
    // Stop case
    if (adapters.size() == 0) {
        return 1;
    }

    // Memoization
    std::string cache_key = part_2_make_cache_key(previous, adapters);
    auto cache_search = part_2_cache.find(cache_key);
    if (cache_search != part_2_cache.end()) {
        return cache_search->second;
    }

    // Compute next possible adapters
    int current = adapters.front();
    adapters.pop_front();
    int next = adapters.front();
    std::list<int> adapters_after = std::list<int>(adapters);

    long next_possibles = part_2_rec(current, adapters_after);

    // Check if current one could be skipped
    int diff = next - previous;
    if(adapters.size() != 0 && diff >= 1 && diff <= 3) {
        next_possibles += part_2_rec(previous, adapters_after);
    }

    part_2_cache.insert({cache_key, next_possibles});
    return next_possibles;
}

void part_2(std::list<int> ints_list) {
    std::cout << "Part 2: " << part_2_rec(0, ints_list) << std::endl;
}

int main() {
    std::list<int> ints_list = get_lines();

    part_1(ints_list);
    part_2(ints_list);

    return 0;
}
