#!/usr/bin/env ruby
# script that output: [SENDER],[RECEIVER],[FLAGS] from a log file
#   The sender phone number or name (including country code if present)
#   The receiver phone number or name (including country code if present)
#   The flags that were used

from = ARGV[0].scan(/from:(.*?)\]/)
to = ARGV[0].scan(/to:(.*?)\]/)
flags = ARGV[0].scan(/flags:(.*?)\]/)
puts [from, to, flags].join(',')
