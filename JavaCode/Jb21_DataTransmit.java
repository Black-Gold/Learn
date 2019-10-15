public class Jb21_DataTransmit
{
	//基本数据类型参数传递
	public static void main(String[] args) 
	{
		int x = 1;
		show(x);
		System.out.println(x);	//输出1
	}
	public static void show(int x)
	{
		x = 2;
	}
}
//引用数据类型参数传递
class Demo
{
	int x = 1;
	public static void main(String[] args) 
	{
		Demo data = new Demo();
		data.x = 3;
		show(data);
		System.out.println(data.x);	//输出为2
	}
	public static void show(Demo data)
	{
		data.x = 2;
	}
}