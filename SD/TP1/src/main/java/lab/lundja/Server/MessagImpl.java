package lab.lundja.Server;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class MessagImpl
        extends UnicastRemoteObject
        implements Message {

    protected MessagImpl() throws RemoteException {
        //
    }

    @Override
    public String helloWorld() throws RemoteException {
        return ("Hello World!");
    }

    @Override
    public long add(long a, long b) throws RemoteException {
        return a+b;
    }

    @Override
    public long sub(long a, long b) throws RemoteException {
        return a-b;
    }

    @Override
    public long mul(long a, long b) throws RemoteException {
        return a*b;
    }

    @Override
    public long div(long a, long b) throws RemoteException {
        return a/b;
    }
}
