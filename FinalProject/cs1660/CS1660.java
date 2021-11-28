
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import java.awt.Desktop;
import java.net.URI;
import java.util.Scanner;
/**
 *
 * @author JVMas
 */
public class CS1660 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        while(true){
            
            Scanner scan = new Scanner(System.in);
            System.out.println("\n");
            System.out.println("Welcome to big data processing toolbox");
            System.out.println("Make a selection");
            System.out.println("1: Apache Hadoop");
            System.out.println("2: Apache Spark");
            System.out.println("3: Jupyter Notebook");
            System.out.println("4: SonarQube");
            System.out.println("5: Exit");
            System.out.print("Selection : ");
            try {
                String input = scan.nextLine();
                //System.out.println(input);
                int intInput = Integer.parseInt(input);
                //System.out.println(intInput);
                switch (intInput) {
                    case 1: System.out.println("Go to http://35.203.97.144:9870");
                            //Desktop.getDesktop().browse(new URI("http://35.203.97.144:9870/"));
                            break;
                    case 2: System.out.println("Go to http://35.203.61.246:8080");
                            //Desktop.getDesktop().browse(new URI("http://35.203.61.246:8080/"));
                            break;
                    case 3: System.out.println("Go to http://34.95.6.176:8888");
                            //Desktop.getDesktop().browse(new URI("http://34.95.6.176:8888"));
                            break;
                    case 4: System.out.println("Go to http://34.95.8.228:9000");
                            //Desktop.getDesktop().browse(new URI("http://34.95.8.228:9000"));
                            break;
                    case 5: System.exit(0);
                            break;
                    default: System.out.println("Must enter integer 1-5");
                }
            } catch(Exception e) {
                //System.out.println(e);
                System.out.println("Must enter integer 1-5");
            }
        
        }
        
        
        //#TODO Make it actually do something
        
    }
    
}
