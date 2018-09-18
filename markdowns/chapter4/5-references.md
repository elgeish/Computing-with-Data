# References

```C++
int a = 2;
int c = 3;
int &refA = a; // refA is a reference to the variable a
int b = refA; // has same effect as b = a

refA = 5; // has same effect as a = 5 

int &refC1 = c;
int &refC2 = c;  // both refC1 and refC2 refer to c
```
