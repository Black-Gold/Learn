public class Jb02_VarDemo1
{
	public static void main(String[] args) 
	{
		/*
		byte	1字节
		boolean 1字节
		short	2字节
		char	2字节
		int		4字节
		float	4字节
		long	8字节
		double	8字节
		*/
		//数据类型 变量名 = 初始化值;
		byte b = 1;	//定义变量b,初始化值为1
		short s = 2;
		int i = 3;
		long l = 4;
		float f = 5.5f;
		double d = 6.6;
		char c = 'c';
		boolean bo = true;
		bo = false;
		{
			int x = 9;
			System.out.println("x");	//局部变量x
		}
		System.out.println(c);
	}
}
