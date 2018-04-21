public class Jb13_ForTest
{
	public static void main(String[] args) 
	{
		/*打印矩形,不成文规律：外循环控制行，内循环控制列
		for (int x=1;x<=4; x++)
		{
			for (int y=1;y<=4 ;y++ )
			{
				System.out.print("*");
			}
			System.out.println("*");
		}
		*/

		/*打印倒三角
		//int z = 5;
		for (int x=1;x<=5; x++)	//1-5 1-4 1-3	//1-5 2-5 3-5
		{
			for (int y=x;y<=5 ;y++ )
			{
				System.out.print("*");
			}
			System.out.println("*");
				//z--;
		}
		*/

		/*
		for (int x=1;x<=5; x++)
		{
			for (int y=5;y>=x ;y-- )
			{
				System.out.print(y);
			}
			System.out.println();
		}
		*/

		/*打印99乘法表 \n:回车 \t：制表符 \b：退格 \r：按下回车键
		for (int x=1;x<=9 ;x++ )
		{
			for (int y=1;y<=x ;y++ )
			{
				System.out.print(y+"*"+x+"="+x*y+"\t");
			}
			System.out.println();
		}
		*/
	}
}
