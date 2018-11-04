import java.io.Serializable;

public class PatientInfo implements Serializable {
    private static final long serialVersionUID = 42;
    private final String name;
    private final int age;

    public PatientInfo(final String name, final int age) {
        this.name = name;
        this.age = age;
    }
}
