## Abstract Data Types
It's a collection of axioms and operations
Operations
	what actions can be performed on the data type. For each operation we know:
		name
		arguments
		return type

Axioms are rules between operations
We do not know the information about the implementation of operations
Similar to Java interfaces

### Examples
* Stack
	* Operations: push, pop, peek, isEmpty


# Introduction to C/C++
* Similar to Java
* The basic structure of a C program
Inclusion of headers
```c++
#include <stuff>
int a,b,c;
int main(){
	a=10;
	scanf("%d",&b);
	c=a+b;
	printf("%d\n",c);
	return 0;
}
```
Definition of types/classes
Declaration of global variables
Definition of functions
The main functions
