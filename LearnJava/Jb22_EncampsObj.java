public class Jb22_EncampsObj
{
	//面向对象的封装
	public static void main(String[] args) 
	{
		Person xiaoMing = new Person();
		xiaoMing.getAge(21);
		xiaoMing.speak();
	}
}

class Person
{
	private int age;
	public void getAge(int num)
	{
		if(num>=0 && num<=150)
		{
			age = num;
		}
		else
			System.out.println("错误，输出年龄范围在0~150");
	}
	void speak()
	{
		System.out.println("年龄是"+age);
	}
}
