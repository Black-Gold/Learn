public class Jb25_ObjExtends
{
	public static void main(String[] args) 
	{
		Student a = new Student();
		a.name = "xiaoming";
		a.age = 17;
		a.study();
	}
}
/*
继承的优点:
提高代码复用性
类与类之间产生了关系，给第三个特征多态提供了前提
*/

class Person
{
	String name;
	int age;
}

class Student extends Person
{
	void study()
	{
		System.out.println(age+"岁的"+name+"正在学习");
	}
}