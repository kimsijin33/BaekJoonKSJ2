num1 = gets.to_i
num2 = gets.to_s

three = num2[2].to_i
second = num2[1].to_i
first = num2[0].to_i
#puts "#{three}"
#puts "#{second}"
#puts "#{first}"
num1_3=num1*three
num1_2=num1*second
num1_1=num1*first

puts "#{num1_3}"
puts "#{num1_2}"
puts "#{num1_1}"

num3 = num1_3
num4 = num1_2 * 10
num5 = num1_1 * 100
puts "#{num3+num4+num5}"