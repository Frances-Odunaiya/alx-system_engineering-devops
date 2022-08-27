#!/usr/bin/env ruby
# Match "hbtn, htn" not "hbbtn or hbbbtn"

puts ARGV[0].scan(/hb?tn/).join
