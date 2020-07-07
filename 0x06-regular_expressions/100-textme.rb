#!/usr/bin/env ruby
from = ARGV[0].scan(/from:(.\w+)/).join
flags = ARGV[0].scan(/flags:(.+\-\d)/).join
to = ARGV[0].scan(/to:(.\d+[\d])/).join

puts "#{from},#{to},#{flags}\n"