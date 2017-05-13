public class Jb11_WhileTest
{
	public static void main(String[] args) 
	{
		//输出1到100之间里，2的倍数有几个。计数器思想
		int x = 1;
		int count = 0;
		while (x<=100)
		{
			if (x%2==0)
			{
				count++;
			}
			x++;
		}
		System.out.println("1~100之间2的倍数个数总共是"+count);
	}
}
