public class Jb26_Final
{
	public static void main(String[] args) 
	{
		
		System.out.println("Hello World!");
	}
}
//继承的弊端:打破了封装性，会覆盖父类方法
		/*
		final关键字可以修饰类、方法和变量
		修饰的类不能被继承继承
		修饰的方法不可以被覆盖
		修饰的变量是个常量，只能被赋值一次
		内部类只能访问被final修饰的局部变量
		常量所有字母都要大写，多个单词用_连接
		*/
class Fu
{
	void method()
	{
		//调用底层系统资源	
	}
}

class Zi extends Fu
{
	void method()
	{
		//	final int x = 1;
		//	x = 2;	此会提示出错，变量x为最终变量，无法赋值
		System.out.println("OK");
	}
}
