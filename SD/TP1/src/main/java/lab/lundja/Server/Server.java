package lab.lundja.Server;

import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;


public class Server
    extends UnicastRemoteObject {

    protected Server() throws RemoteException {
        super();
    }



    public static void main(String[] args) {
        try{
            // Instantiate a message
            MessagImpl msg = new MessagImpl();

            // create registry
            Registry registry = LocateRegistry.createRegistry(2020);

            // register that object
            registry.rebind("Hello",msg);

            System.out.println("Server is ready ...");
        } catch(Exception e){
            System.err.println("Exception server says : " + e);
        }

    }
}
