public class Jb30_Interface2
{
	//实现电脑USB接口功能
	public static void main(String[] args) 
	{
		useUSB(new Upan());
	}
	public static void useUSB(USB u)	//接口类型的引用，用于接收（指向）接口的子类对象
	{
		u.open();
		u.close();
	}
}

interface USB
{
	public void open();
	public void close();
}

class Upan implements USB
{
	public void open()
	{
		System.out.println("开启");
	}
	public void close()
	{
		System.out.println("关闭");
	}
}