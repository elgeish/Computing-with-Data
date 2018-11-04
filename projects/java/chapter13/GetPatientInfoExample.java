import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.ArrayList;
import java.util.List;

public class GetPatientInfoExample {
    public static void main(final String[] args) {
        try {
            final FileInputStream fis = new FileInputStream("patients");
            final ObjectInputStream in = new ObjectInputStream(fis);
            final List patientsInfo = (ArrayList) in.readObject();
            
            in.close();
            System.out.println(patientsInfo.size() + " patients found");
        } catch (IOException ex) {
            ex.printStackTrace();
        } catch (ClassNotFoundException ex) {
            ex.printStackTrace();
        }
    }
}
