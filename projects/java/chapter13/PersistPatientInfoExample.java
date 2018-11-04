import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.util.ArrayList;
import java.util.List;

public class PersistPatientInfoExample {
    public static void main(final String[] args) {
        final String filename = "patients";
        final PatientInfo patient1 = new PatientInfo("John Smith", 33);
        final PatientInfo patient2 = new PatientInfo("Jane Doe", 30);
        final List<PatientInfo> PatientList = new ArrayList<>();

        PatientList.add(patient1);
        PatientList.add(patient2);

        try {
            final FileOutputStream fos = new FileOutputStream(filename);
            final ObjectOutputStream out = new ObjectOutputStream(fos);

            out.writeObject(PatientList);
            out.close();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}
