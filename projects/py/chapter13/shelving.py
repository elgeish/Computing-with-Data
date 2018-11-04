import shelve

# Example 1 - store
patients_df = {
  "age" : [25.2, 35.4, 52.1],
  "height" : [68.1, 62.5, 60.5],
  "weight" : [170.2, 160.7, 185.5]
}
records = shelve.open('patients')
records['patients'] = patients_df 
records.close()

# Example 2 - load and manipulate
records = shelve.open('patients')
patients_reconstructed = records['patients']
del records['patients']  # delete value from disk
records.close()
