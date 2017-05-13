public class Jb07_IfDemo
{
	public static void main(String[] args) 
	{
	//	判断结构：
	//	当if else运算后，由具体结果时，可简化成三元运算符

		int x = 1;
		if (x>3)
		{
			System.out.println("yeah");
		}
		else if (x>2)
		{
			System.out.println("OK");
		}
		else
		{
			System.out.pintln("欧了");
		}
		//局部代码块可定义局部变量的生命周期。
		{
			int y = 3;
		}

		System.out.println("over"+y);	//y在局部代码块里，会出现错误。
	}
}
