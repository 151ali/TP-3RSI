package lab.lundja.Client;

import com.sun.xml.internal.messaging.saaj.soap.MessageImpl;
import lab.lundja.Server.Message;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Client {
    //

    public static void main(String[] args){
        try{
            // get the registry
            Registry registry  = LocateRegistry.getRegistry(2020);
            System.out.println(registry.toString());

            // Looking for the remote object
            Message stub = (Message) registry.lookup("Hello");
            System.out.println(stub.toString());
            // invoke the methode
            String s = stub.helloWorld();


            System.out.println(s);
            System.out.println("Do you know that 5 + 4 = " +  stub.add(5,4));

        }catch(Exception e){
            System.err.println("Exception client says : " + e);
        }
    }
}
