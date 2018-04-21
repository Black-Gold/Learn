public class Jb32_PolMember
{
    /*
    多态时，成员的特点
    成员变量：
    编译时：参考引用型变量所属的类中是否有调用的成员变量，有则编译通过，否则编译失败
    运行时：参考引用型变量所属的类中是否有调用的成员变量，并运行该所属类型的成员变量
    通俗的讲：编译和运行都参考等号左边！Fu f = new Zi();

    成员函数(非静态)：
    编译时：参考引用型变量所属的类中是否有调用的函数，有则编译通过，否则编译失败
    编译时：参考的是对象所属的类中是否有调用的函数
    通俗的讲：编译参考等号左边，运行参考等号右边

    静态函数：
	编译时：参考引用型变量所属的类中是否有调用的静态方法
	运行时：参考引用型变量所属的类中是否有调用的静态方法
	通俗的讲：编译和运行都参考等号左边
	静态方法，不需要对象也行，直接用类名调用
    */
    public static void main(String[] args)
    {
        Fu f = new Zi();
        f.method();	//可以不需要对象来调用，等同于直接用类名调用Fu.method();,
        //f.show();
        //System.out.println(f.num);
    }
}

class Fu
{
    int num = 1;
    void show()
    {
        System.out.println("FU");
    }
    static void method()
    {
        System.out.println("FU static");
    }
}

class Zi extends Fu
{
    int num = 2;
    void show()
    {
        System.out.println("ZI");
    }
    static void method()
    {
        System.out.println("ZI static");
    }
}