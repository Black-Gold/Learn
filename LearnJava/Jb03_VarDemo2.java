public class Jb03_VarDemo2
{
	public static void main(String[] args) 
	{
		/*
		int x = 1;
		x = x + 1;
		byte b = 2;
		x = x + b;	//自动类型转换
		b = (byte)(b + 2);	//强制类型转换
		System.out.println(b);	
		*/
		byte b = 1;
		byte b1 = 2;
		byte b2 = 3;
	//	b = b1 + b2;	b1与b2是变量，无法判断并赋值
		
		int x;
		int x1 = Integer.MAX_VALUE;
		int x2 = 2;
		x = x1 + x2;	//int是默认类型，自动强制转换
	}
}
