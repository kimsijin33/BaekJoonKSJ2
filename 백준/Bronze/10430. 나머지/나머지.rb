num1, num2, num3 = gets.split.map(&:to_i)
plus = (num1 + num2)%num3
substraction = ((num1 % num3) + (num2%num3)) %num3
product = (num1 * num2)%num3
divide = ((num1 % num3) * (num2%num3))%num3
#remainder_operater = num1 % num2
puts "#{plus}"
puts "#{substraction}"
puts "#{product}"
puts "#{divide}"
#puts "#{remainder_operater}"

    #console.log((num1+num2)%num3);
    #console.log(((num1%num3) + (num2%num3))%num3);
    #console.log((num1*num2)%num3);
    #console.log(((num1%num3) * (num2%num3))%num3);