public class Jb16_Function3
{
	public static void main(String[] args) 
	{
	/*函数的重载概念：在同一类中，允许一个以上的同名函数，只要它们的参数个数或参数类型不同即可。
	重载特点：与返回值类型无关，只看参数列表*/
	}
	//两小数之和
	public static double add(double a,double b)
	{
		return a+b;
	}
	//三整数之和
	public static double add(int a,int b,int c)
	{
		return a+b+c;
	}
}
