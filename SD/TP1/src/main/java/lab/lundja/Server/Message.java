package lab.lundja.Server;

import java.rmi.Remote;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public interface Message
        extends Remote {
    String helloWorld() throws RemoteException;
    long add(long a, long b) throws java.rmi.RemoteException;
    long sub(long a, long b) throws java.rmi.RemoteException;
    long mul(long a, long b) throws java.rmi.RemoteException;
    long div(long a, long b) throws java.rmi.RemoteException;
}
