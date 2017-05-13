public class Jb20_Object
{
	public static void main(String[] args) 
	{
		Car benz = new Car();	//通过new关键字创建一个Car的实例
		benz.wheel = 4;
		benz.color = "green";
		benz.run();	//调用对象中的run功能

		Car gtr1 = new Car();
		Car gtr2 = new Car();
		show(gtr1);
		show(gtr2);
	}
	/*
	匿名对象
	Car benz = new Car();
	benz.run();
	匿名对象写法：
	new Car().run();

	对象对方法只有一次调用的时候，可简化为匿名对象
	匿名对象可以作为实际参数进行传递
	Car gtr1 = new Car();
	show(gtr1);
	show(new new Car());
	*/

	public static void show(Car car)	//类类型的变量一定指向对象，否则就为null
	{
		car.wheel = 6;
		car.color = "red";
		System.out.println(car.wheel+"\t"+car.color);
	}
}

class Car
{
	int wheel;	//int wheel = 4;显示初始化值为4
	String color;
	void run()
	{
		//int num = 6;	局部变量，打印num为6
		System.out.println(wheel+"\t"+color);
	}
}
/*
类是对象的实例化体现
定义类：定义类中的成员
成员：成员变量>>:属性，成员函数>>:行为

成员变量与局部变量的区别：
成员变量定义在类中，所在类中都可以访问
局部变量定义在函数、语句和局部代码块中，只在所属区域有效

成员变量存在堆内存的对象里
局部变量存在栈内存的方法里

成员变量：对象创建而存在，对象消失而消失
局部变量：所属区域执行而存在，所属区域结束而消失

成员变量都有默认初始化值
局部变量没有默认初始化值

*/
