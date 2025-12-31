import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        
        long num1, num2, num3;
        Scanner sc = new Scanner(System.in);
        num1 = sc.nextLong();
        num2 = sc.nextLong();
        num3 = sc.nextLong();

        System.out.println(num1 + num2 + num3);

        sc.close();
    }
}