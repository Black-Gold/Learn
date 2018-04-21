public class Jb27_AbstractClass
{
	public static void main(String[] args) 
	{
		/*
		抽象类特点：
		抽象方法只有声明没有具体的实现，此方法既是抽象方法，需要被abstract修饰
		抽象方法必须定义在抽象类中，该类必须被abstract修饰
		抽象类不能被实例化！因为调用抽象方法没意义。
		抽象类必须由其子类覆盖了所有的抽象方法后，该子类才可以实例化，否则子类还是抽象类

		抽象类有构造函数，用于给子类对象进行初始化
		抽象类可以不定义抽象方法，比较少见，目的就是不让该类创建对象，AWT适配器对象既是这种类
		通常这个类里的方法有方法体，但没有内容
		class Demo()
		{
			void show1()
			{}
		}
		
		抽象关键字不可以和private：因为抽象方法需要被子类需要覆盖，私有后无法覆盖
		不可以和static：因为抽象方法不需要运行，没有具体内容，运行没意义，直接调用类名就行
		不可以和final：因为不能被子类覆盖

		抽象类与一般类的共同点：都是用来描述事物，在内部定义了成员
		不同点：一般类有足够信息描述事物。抽象类描述事物的信息可能不足
		一般类中不能定义抽象方法，只能定义非抽象方法。抽象类中可以定义抽象方法，也可以定义非抽象方法
		一般类可以被实例化。抽象类不能被实例化。

		抽象类一定是父类。因为需要子类覆盖其方法后才能对子类进行实例化。
		*/
		System.out.println("Hello World!");
	}
}

abstract class Demo
{
	abstract void show();	
	//将DemoA和DemoB向上抽取共性方法，但是内容不同，具体不清楚，此时用abstract修饰
}

class DemoA
{
	void show()
	{
		System.out.println("show A");
	}
}

class DemoB
{
	void show()
	{
		System.out.println("show B");
	}
}
