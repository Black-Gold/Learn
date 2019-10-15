public class Jb14_Function
{
	public static void main(String[] args) 
	{
		/*函数格式：
		修饰符 返回值类型 函数名(参数类型 形式参数1,参数类型 形式参数2,.......)
			{
				执行语句;
				return返回值;
			}
		*/
		//定义一个功能，求两数之和
		int sum = add(6,2);
		System.out.println(sum);
	}
	public static int add(int a,int b)
		{
			int sum = a+b;
			return sum;
		}
}
