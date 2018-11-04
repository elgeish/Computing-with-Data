# Example 1 - the pickle module
import pickle

patients = {
  "age" : [25.2, 35.4, 52.1],
  "height" : [68.1, 62.5, 60.5],
  "weight" : [170.2, 160.7, 185.5]
}
# binary serialization
serialized_patients = pickle.dumps(patients)  
# deserialization
patients_reconstructed = pickle.loads(serialized_patients)


# Example 2 - pickling using pandas
import pandas as pd

patients = {
  "age" : [25.2, 35.4, 52.1],
  "height" : [68.1, 62.5, 60.5],
  "weight" : [170.2, 160.7, 185.5]
}
patients_df = pd.DataFrame(patients)
# serialize and save to binary disk
patients_df.to_pickle('patients.txt')  
# read binary serialization to Python object
patients_reconstructed = pd.read_pickle('patients.txt')   
print(patients_reconstructed)
