Vistle Coding Guidelines
========================
Please follow the following guidelines.                                                                                         


Compiler Compatibility
----------------------

We use C++ 14, but we want to be able to compile Vistle with

* Visual Studio 2017
* GCC 5.3 and newer,
* Clang 3.0 and newer (Xcode 6 and newer).
* Intel ICC 10 and newer


Source Code Formatting
----------------------

* UNIX line-feeds
* no tabs
* avoid trailing spaces
* files have to end with a new-line
* only ASCII characters (no latin1 or unicode - their behaviour depends on character sets)
* indent by 4 spaces
* follow commas with a space, e.g.:

        printf("format: %s", parameter);

* put a space between keywords and opening parentheses, but not between function name and function arguments, e.g.:

        void recurse(int arg) {
            if (condition) {
                recurse(arg+1);
            }
        }

* put opening braces on same line as keyword introducing the block (except for constructors),
  follow closing braces with other keywords, e.g.:

        if (condition) {
        } else {
        }
    
        do {
        } while(true);

* put closing braces on 
* use `UPPER_CASE` for preprocessor `#define`s
* use `lowerCamelCase` for variables, functions, and methods
* use `CamelCase` for `class` names, `enum`s
* for easy reordering of initializers, format initializer lists like this:

        class SomeClass: public BaseClass {
            SomeClass()
            : BaseClass()
            , m_member(memberInit)
            , m_member2(memberInit2)
            {}
        };




If changing source code formatting, then do that as a separate commit:
this makes it easy to follow the actual code changes.


Coding Style
------------

* protect your headers with include guards like this:

        #ifndef MY_PRETTY_HEADER_H
        #define MY_PRETTY_HEADER_H
        ...
        #endif

* `#include` all necessary headers at the beginning of the file
* in order to reduce compile times (and recompilation) you should avoid
  including headers from headers, instead use forward declarations whenever possible:

        class MyPrettyClass;

* also in order to reduce compile times (and recompilation) you should try to restrict
  headers to declarations and avoid code within headers
* don't use `using namespace <my_namespace>` or `using ...` in global scope in header files
* include parameter names in function prototypes in headers - these serve as
  documentation
* think about variable names, don't name them just `tmp`
* the smaller the scope of a variable, the shorter can be its name
* documenting code helps understand it, therefore documenting code is a real benefit
* initialize variables as soon as you define them, e.g:

          int i = 0;

  instead of

          int i;

* make the scope of variables as small as possible - this makes it easy to see
  until which point the value of a variable has relevance - define another variable,
  perhaps even with identical name, if necessary for another
  independent purpose - the compiler will reuse space if possible, e.g.:

          if (something) {
              bool important_flag = false;
              // use important_flag
          } else {
              bool important_flag = false;
              // use important_flag
          }

  instead of:

          bool important_flag = false;
          if (something) {
              // use important_flag
          } else {
              // use important_flag for a different purpose
          }                                                                                                                                                                                                                                                                                           

* prefix class attributes with `m_`
