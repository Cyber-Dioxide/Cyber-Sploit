require "colorize"

puts "Enter your gmail id:~ ".colorize(:color => "yellow")
id = gets
require 'io/console'
password = STDIN.getpass("Password:~ ")

system("python3 /Encryption-Decryption/encrypt.py #{id}")
system("python3 /Encryption-Decryption/encrypt.py #{password}")
