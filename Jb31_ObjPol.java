public class Jb31_ObjPol
{
	//对象的多态性;代码中的体现就是父类或接口的引用指向其子类的对象
	public static void main(String[] args) 
	{
		/*自动类型提升(向上转型)，猫对象提升为动物类型.但特有功能无法访问
		作用是限制对特有功能的访问*/
		Animal a = new Cat();	
		a.eat();
		//如果仍要使用猫的特用功能，可将对象向下转型
		//自始至终都是子类对象进行类型的变换
		Cat c = (Cat)a;	//向下转型目的是为了使用子类的特用方法
		c.eat();
		c.catch();
		/*
		Cat c = new Cat();
		//Dog d = new Dog();
		//c.eat();
		method(c);
		method(new Dog());
		*/
		method(new Cat());
	}
	/*多态好处：提高代码的扩展性，前面定义的代码可使用后期的内容
	弊端：前期定义的内容不能使用（调用）后期子类的特有内容
	使用多态前提：必须有关系、继承、实现
	要有方法覆盖
	
	*/
	public static void method(Animal a)
	{
		a.eat();
		if (a instanceof Cat)
		//instanceof 用于判断对象的具体类型，只能用于引用数据类型判断
		//通常在向下转型前用于健壮性的判断
		{
			Cat c2 = (Cat)a;
			c2.catch();
		}
		else if (a instanceof Dog)
		{
			Dog d2 = (Dog)a;
			d2.watchHome();
		}
		
	}
}

abstract class Animal
{
	abstract void eat();
}

class Dog extends Animal
{
	public void eat()
	{
		System.out.println("吃屎");
	}
	public void watchHome()
	{
		System.out.println("看家");
	}
}

class Cat extends Animal
{
	public void eat()
	{
		System.out.println("吃鱼");
	}
	public void catch()
	{
		System.out.println("捉老鼠");
	}
}
