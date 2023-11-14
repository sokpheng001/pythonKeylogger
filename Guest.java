
import java.util.Scanner;

class Napoleon{
    public void guessingName(){
        System.out.print("Insert your name: ");
        String name  = new Scanner(System.in).nextLine();
        int sum  = 0;
        String name1 = name.toUpperCase();
        for (int i = 0; i <name1.length();i++){
            if(name1.charAt(i) == 'A' || name1.charAt(i) == 'J' || name1.charAt(i) == 'S'){
                sum += 1;
            }else if(name1.charAt(i) == 'B' || name1.charAt(i) == 'K' || name1.charAt(i) == 'T'){
                sum += 2;
            }else if(name1.charAt(i) == 'C' || name1.charAt(i)=='L' || name1.charAt(i)=='U'){
                sum += 3;
            }else if(name1.charAt(i) == 'D' || name1.charAt(i)=='V' || name1.charAt(i)=='M'){
                sum += 4;
            }else if (name1.charAt(i)=='E' || name1.charAt(i)== 'N' || name1.charAt(i)=='W'){
                sum+=5;
            }else if (name1.charAt(i) == 'F' || name1.charAt(i)=='O' || name1.charAt(i) == 'X'){
                sum+=6;
            }else if (name1.charAt(i)=='G' || name1.charAt(i)=='P' || name1.charAt(i)=='Y'){
                sum+=7;
            }else if(name1.charAt(i)=='H' || name1.charAt(i)=='Q' || name1.charAt(i) =='Z' ) {
                sum+=8;
            }else{
                sum+=9;
            }
        }
        int result = 0;
        if(sum >= 10){
            result = sum / 10;
            result+=sum % 10;
            while(result>=10){
                int k = result;
                result = result/10;
                result+=k%10;
            }
        }
        System.out.println("You are a person in number: " + result);
    }
}


public class Guest{
    public static void main(String[] args) {
        Napoleon napolaoang  = new Napoleon();
        napolaoang.guessingName();   
    }
}