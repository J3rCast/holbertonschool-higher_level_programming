# 0x0C. Python - Almost a circle

![Image](https://d138zd1ktt9iqe.cloudfront.net/media/seo_landing_files/visalakshi-difference-between-square-and-rectangle-01-1618193998.png)

<code><strong>tests/</strong></code> Unittest for all classes and methods.

<code><strong>models/base.py:</strong></code> This is the base class for every other class, and they inherit from this class.

<code><strong>models/rectangle.py:</strong></code> This is the rectangle class and inherits from base. Methods:

	- area(self): Return the area of the rectangle.

	- display(self): Prints a representation of the rectangle using "#" character, in the stdout.

	- update(*args, **kwargs): Update the attributes of the  rectangle.

		1. argument should be the id attribute
		2. argument should be the width attribute
		3. argument should be the height attribute
		4. argument should be the x attribute
		5. argument should be the y attribute

	You can also specify the argument that you want to change by using, example: update(width=2)

<code><strong>models/square.py:</strong></code> This is the square class that inherits from reclangle and has the same methos as rectangle, except that there is no width or height, now it is only named size.
