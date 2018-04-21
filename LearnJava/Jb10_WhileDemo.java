public class Jb10_WhileDemo
{
	public static void main(String[] args) 
	{
	//	循环结构
	/*
	while语句格式：
	while (条件表达式)
	{
		执行语句;
	}
	do
	{
		执行语句;
	}
	while (条件表达式);
	do while特点：
		无论条件是否满足，循环体至少执行一次
	*/
	/*
		int x = 1;
		do
		{	
			System.out.println("x="+x);
			x++;
		}
		while (x<2);

		int y = 1;
		while (y<2)
		{
			System.out.println("y="+y);
		}
		*/
		//获取1到100数字的和:————累加思想
		int x = 1;
		int sum = 0;
		while (x<=100)
		{
			sum+=x;
			x++;
		}
		System.out.println("sum="+sum);
	}
}
