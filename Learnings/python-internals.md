# Python Code Flow.

Is python interpreted langauge? The answer is yes. but is python compiled langauge? answer is YES.

Python is compiled into bytecode and that bytecode is interpreted at run time. 

This is very similar to Java. Only difference is, in Java, java->bytecode is done by your compiler and bytecode to machinecode is done by JVM/JIT. This is 2 pass process. We first run `javac` command to create bytecode. and on this bytecode/`.class` file jvm operates when `java` command is run.

In python, the your `.py` code to `.pyc` and then this `.pyc` bytecode to execution happens in one pass. 

When you run `python test.py` 

# what should be the structure
1. java - python similarities and differences
2. python steps to interpretation
    1. parser
        lexer
        tokenizer
        parser
    2. Compiler
        control flow
        assembler
    3. Interpreter
        Line by line go through each bytecode instruction
3. What is bytecode/opcode instruction?
3. Parser internals
4. Compiler internals
5. Interpreter internals