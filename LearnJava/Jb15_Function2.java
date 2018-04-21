public class Jb15_Function2
{
	public static void main(String[] args) 
	{
		//draw(7,8);
		getLevel(99);
	}
	/*定义输出矩形函数功能
	public static void draw(int row,int col)
	{
		for (int x=1;x<=row ;x++ )
		{
			for (int y=1;y<=col ;y++ )
			{
				System.out.print("*");
			}
			System.out.println();
		}
		return;	//此处return可省略，即返回值具体类型不确定，使用void时，可省略return
	}
	*/
	//根据分数输出对应等级
	public static void getLevel(int grade)
	{
		if (grade<0 || grade>100)
		{
			System.out.println("错误");
		}
		else if (grade>=90 && grade<=100)
		{
			System.out.println("A");
		}
		else if (grade>=60 && grade<=89)
		{
			System.out.println("B");
		}
		else
			System.out.println("C");
		return;
	}
}
