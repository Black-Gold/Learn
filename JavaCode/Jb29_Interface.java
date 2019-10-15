/*
当一个类中的方法都是抽象时，可以将该抽象类用接口的形式定义和表示。
abstract class Demo
{
	abstract void show1();
	abstract void show2();
}

定义接口的关键是interface
接口常见的成员：成员都有固定的修饰符
全局常量：public static final
抽象方法：public abstract
固接口中的成员都是public（公共）权限
*/
interface Demo
{
	public static final int NUM = 4;
	public abstract void show1();
	public abstract void show2();
}

/*类与类之间继承关系。类与接口之间实现关系。接口与接口之间继承关系，且接口可以多继承
接口不能实例化，只能由实现接口的子类并覆盖了接口所有抽象方法后，该子类才能实例化
否则，该子类是一个抽象类
*/
class DemoImpl implements Demo
{
	public void show1()
	{}
	public void show2()
	{}
}

/*
Java中不支持多继承，因为会出现调用的不确定性
用多实现来替代。一个类可以实现多个接口

*/

interface A
{
	public void show1();
}

interface B
{
	public void show2();
}

class Test implements A,B	//多实现
{
	public void show()
	{
		System.out.println("OK");
	}
}

//一个类继承另一个类的同时，还可实现多个接口
class C
{
	public void method()
	{}
}

abstract class Test2 extends C implements A,B
{
	
}

public class Jb29_Interface
{
	public static void main(String[] args) 
	{
		/*DemoImpl inf = new DemoImpl();
		System.out.println(inf.NUM);
		System.out.println(DemoImpl.NUM);
		System.out.println(Demo.NUM);*/

	}
}
/*
接口和抽象类的相同点：都是不断向上抽取而来
不同点：抽象类需要被继承，而且只能单继承。接口需要被实现，可以多继承
抽象类中可以定义抽象方法和非抽象方法，子类继承后，可以直接使用非抽象方法
接口只能定义抽象方法，必须由子类实现
抽象类的继承，定义该体系的基本共性内容
接口的实现，定义该体系的额外功能
*/