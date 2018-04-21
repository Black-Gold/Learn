public class Jb34_InnerClass2
{
	public static void main(String[] args) 
	{
		new Outer().method();
		new Outer2().method();
	}
}

/*
为什么内部类可以直接访问外部类中的成员
内部类持有外部类的引用。	外部类名.this
*/
class Outer
{
	int num = 1;
	class Inner
	{
		int num = 2;
		void show()
		{
			int num = 3;
			System.out.println(num);	//打印show方法内的成员
			System.out.println(this.num);	//打印内部中的成员
			System.out.println(Outer.this.num);	//打印外部类中的成员
		}
	}
	void method()
	{
		new Inner().show();
	}
}

//JDK1.7之前，内部类在局部位置上只能访问局部中被final修饰的局部变量
//JDK1.8时，内部类在局部位置上可以直接访问局部变量
class Outer2
{
	int num = 1;
	void method()
	{
		int x = 2;	//局部变量x
		class Inner2
		{
			void show()
			{
				System.out.println("show"+x);
			}
		}
		Inner2 in = new Inner2();
		in.show();
	}
	
}