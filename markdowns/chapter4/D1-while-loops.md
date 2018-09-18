# While-Loops

```C++
// Example 1
// Assigns 4! = 4 * 3 * 2 = 24 to the variable fac_val
// 3 loop iterations will be executed (on fourth iteration the
// condition 1 > 1 fails).
int val = 4;
int fac_val = 1;

while (val > 1) {
  fac_val = fac_val * val;
  val = val - 1;
}

// Example 2
// similar to previous example with break statement
int val = 4;
int fac_val = 1;

while (1) { 
  if (val <= 1) {
    break;
  }
  
  fac_val = fac_val * val;
  val = val - 1;
}

// Example 3
// computes = 4 * 2 (iteration that multiplies by 3 is skipped)
int val = 4;
int fac_val_mod = 1;

while (1) {
  if (val == 3) { 
    val = val - 1;
    continue;
  }
  
  if (val <= 1) {
    break;
  }
  
  fac_val_mod = fac_val_mod * val;
  val = val - 1;
}
```
