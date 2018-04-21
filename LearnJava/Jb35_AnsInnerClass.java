public class Jb35_AnsInnerClass
{
	/*匿名内部类使用前提：内部类必须继承或者实现一个外部类或者接口
	匿名内部类，其实就是匿名子类对象
	*/
	public static void main(String[] args) 
	{
		new Outer().method();
	}
}

class Outer
{
	/*
	class Inner extends Demo
	{
		void show()
		{
			System.out.println("呵呵"+num);
		}
	}
	*/
	public void method()
	{
		//new Inner().show();
		new Demo()
		{
			void show()
			{
				System.out.println("呵呵呵呵"+num);
			}
		}.show();
	}
}

abstract class Demo
{
	abstract void show();
}
