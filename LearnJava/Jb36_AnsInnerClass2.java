public class Jb36_AnsInnerClass2
{
	/*
	匿名内部类使用场景之一：当函数参数是接口类型，而且接口中的方法不超过三个
	可以作为匿名内部类作为实际参数传递
	*/
	public static void main(String[] args) 
	{
		show(new Inf()
		{
			public void show1()
			{}
			public void show2()
			{}
		});
	}

	public static void show(Inf in)
	{
		in.show1();
		in.show2();
	}
}

interface Inf
{
	void show1();
	void show2();
}

//匿名内部类的使用
class Outer
{
	public void method()
	{
		Inf in = new Inf()
		{
			public void show1()
			{}
			public void show2()
			{}
		};
		in.show1();
		in.show2();
	}
}