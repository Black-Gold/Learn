public class Jb33_InnerClass
{
	public static void main(String[] args) 
	{
		//Outer out = new Outer();
		//out.method();

		//直接访问外部类中的内部类中的成员,内部类共有时
		//Outer.Inner in = new Outer().new Inner();
		//in.show();
		
		//如果内部类是静态的，相当于一个外部类
		//Ouer.Inner in = new Outer.Inner();
		//in.show();

		//如果内部类是静态的，成员是静态的
		Ouer.Inner.fun();
	}
}

/*
内部类访问特点：
内部类可以直接访问外部类中的成员，包括私有成员
而外部类要访问内部类中的成员必须要建立内部类的对象
*/
class Outer
{
	private static int num = 1;

	class Inner	//内部类
	{
		void show()
		{
			System.out.println("嘿嘿"+num);
		}
		/*
		static void fun()	//如果内部类中定义了静态方法，该内部类必须是静态的
		{
			System.out.println("fun 嘿嘿"+num);
		}
		*/
	}
	public void method()	//外部类访问内部类方法
	{
		Inner in = new Inner();
		in.show();
	}
}
/*
内部类一般用于类的设计
分析事物时，发现该事物描述里还有事物，这个事物仍访问被描述事物的内容
这时就将还有的事物定义为内部类描述

*/