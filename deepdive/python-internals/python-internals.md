# Python Code Flow.

Is python interpreted langauge? The answer is yes. but is python compiled langauge? answer is YES.

Python is compiled into bytecode and that bytecode is interpreted at run time. 

This is very similar to Java. Only difference is, in Java, java->bytecode is done by your compiler and bytecode to machinecode is done by JVM/JIT. This is 2 pass process. We first run `javac` command to create bytecode. and on this bytecode/`.class` file jvm operates when `java` command is run.

In python, the your `.py` code to `.pyc` and then this `.pyc` bytecode to execution happens in one pass. 

When you run `python test.py` 
