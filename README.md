# Assignment Junior Integration Engineer

## How to run this script
```sh
python ./src/main
```

## Design pattern
The configuration class is an example of a class that only needs 1 instance
of this application.

I've chosen the Singleton pattern because this creational pattern solves this problem in an easy elegant way.

I did not choose DI or dependency injection. For me it would be way to overkill for a project of this size. Complex mutable state that is hidden by a singleton is often something that you don't want but  this is not the case.

I made this implementation in a more 'Pythonic' way than a classic Singleton.


- The README.md should include:
    - Instructions on how to run the script(s).
    - A brief explanation of the implemented design pattern.
