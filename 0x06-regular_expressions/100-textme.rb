#!/usr/bin/env ruby

regex = /\[from:(\+?\w+)\]|\[to:(\+?\d+)\]|\[flags:((\-?\d:){4}\-?\d)\]/
matchs = ARGV[0].scan(regex)
puts "#{matchs[0][0]},#{matchs[1][1]},#{matchs[2][2]}"
