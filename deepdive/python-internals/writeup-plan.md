
# what should be the structure
- Introduction
- Overview python flow
- Quick overview 

- Simple flow 
    - How python code runs
    - bytecode
    - Similarity and diff with JAva
    **NOTE: Here will explain parser, compiler interpreter in brief not more than 5 lines for each but not any details**
    - basically explain two step complier - interpreter phase
    - Bytecode 
        - what is opcode
        - how to generate bytecode
        - some examples

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

    - parser
                - lexer
                - tokenizer
                - parser
                - grammer 
                - pgen
    - Compiler
        - control flow
        - assembler
    - Interpreter

    **Both of these will be in same thing.**

    3. Parser internals
        grammer 
        pgen
        what lexer does and how
        what tokenizer does and how
        what parser does and how
    4. bytecode Compiler internals
        what is ast?
        ast to instruction
    5. Interpreter internals -- how this is different from JVM.


## This is another plan

- Intro
    - python interpreted lang
    - machine independant
    - python implememtaions we only focus on cpython

- Simple flow 
    - How python code runs
    - bytecode
    - Similarity and diff with JAva
    **NOTE: Here will explain parser, compiler interpreter in brief not more than 5 lines for each but not any details**
    - Bytecode 
        - what is opcode
        - how to generate bytecode
        - some examples

- Flow
    - Theory How python runs
        - parser
            - lexer
            - tokenizer
            - parser
            - grammer 
            - pgen
        - Compiler
            - control flow
            - assembler
        - Interpreter
        
        **NOTE: Here we will explain how things happen. we will also give actual cod that run with function name but wont go deeper than that**

    - what happens when `python test.py` is run
    - show a generated opcode for `test.py` code