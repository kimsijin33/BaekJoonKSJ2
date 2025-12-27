//import java.util.*;
//import java.lang.*;
//import java.io.*;
import java.util.Scanner;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        
        int num1, num2;
        Scanner sc = new Scanner(System.in);
        //Scanner scanner = new Scanner(System.in);
        num1 = sc.nextInt();
        num2 = sc.nextInt();
        //int num1 = scanner.nextInt();
        //int num2 = scanner.nextInt();
        //scanf("%d %d", num1, num2);
        //System.out.println("Hello world!");
        System.out.println(num1 + num2);
        System.out.println(num1 - num2);
        System.out.println(num1 * num2);
        System.out.println(num1 / num2);
        System.out.println(num1 % num2);

        sc.close();
    }
}