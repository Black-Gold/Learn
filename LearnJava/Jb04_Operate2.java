public class Jb04_Operate2
{
	public static void main(String[] args) 
	{
		short s = 1;
		s+=2;	//自动转换 相当于s = (short)(s+2);
	//	s = s+2;	右边s是变量，可能会出现精度丢失。
		System.out.println(s);
	}
}
