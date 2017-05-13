public class Jb08_IfTest
{
	public static void main(String[] args) 
	{
	//	需求：用户输入具体数值，判断出对应的星期
		int week = 3;
		if (week==1)
		{
			System.out.println(week+"是星期一");
		}
		else if (week==2)
		{
			System.out.println(week+"是星期二");
		}
		else if (week==3)
		{
			System.out.println(week+"是星期三");
		}else
		{
			System.out.println("输入错误，请输入1-3的数字");
		}
	
	//	需求：根据用户输入数值，输出对应的季度。
		int month = 3;
		if (month<1 || month>12)
		{
			System.out.println("没有此季节");
		}
		else if (month>=3 && month<=5)
		{
			System.out.println(month+"月是春季");
		}
		else if (month>=6 && month<=8)
		{
			System.out.println(month+"月是夏季");
		}
		else
		{
			System.out.println(month+"月是冬季");
		}
	}
}
