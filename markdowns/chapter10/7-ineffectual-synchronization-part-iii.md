# Ineffectual Synchronization - Part III

Another example of ineffectual synchronization, that's not applicable in Java
but can happen in C#, is demonstrated below:

```C# runnable
using System;
using System.Threading;

class Program
{
  static int sum = 0;
  
  static void DoWork()
  {
    lock ((object) 0)
    {
      for (int i = 0; i < 10000; i++) 
      {
        ++sum;
      }
    }
  }
  
  static void Main()
  {
    for (int i = 0; i < 4; i++)
    {
      new Thread(DoWork).Start();
    }
    
    Thread.Sleep(1000); // ad-hoc wait till threads finish
    Console.WriteLine("C# sum: " + sum);
  }
}
```
