public class Jb39_Multithread
{
	/*
	进程：真正运行的程序，是系统进行资源分配和调度的基本单位
	线程：进程中一个负责程序执行的控制单元，一个进程中可多执行路径
	一个进程至少一个线程。
	创建线程方式之一：继承Thread类
	步骤：
	1、定义一个类继承Thread类
	2、覆盖Thread类中的run方法
	3、直接创建Thread的子类对象创建线程
	4、调用start方法开启线程并调用run方法开始执行
	*/
	public static void main(String[] args) 
	{
		Thread t1 = new Thread();
		Thread t2 = new Thread();
		
		Demo d1 = new Demo("线程1");
		Demo d2 = new Demo("线程......二");
		d1.start();	//开启线程1,调用run方法
		d2.start();
		System.out.println("Hello World!");	//线程三
	}
}

class Demo extends Thread
{
	private String name;
	Demo(String name)
	{
		this.name = name;
	}
	public void run()
	{
		for (int x=0;x<9 ;x++)
		{
			for (int y=0; y<27; y++)
			{
			}
			System.out.println(name+Thread.currentThread().getName()+"..."+x);	//通过Thread的getName方法获取对象的名称
		}
	}

/*	public void show()
	{
		for (int x=0;x<10 ;x++ )
		{
			for (int y=0;y<100 ;y++ )
			{
				System.out.println(name+"x="+x);
			}
		}		
	}*/
}