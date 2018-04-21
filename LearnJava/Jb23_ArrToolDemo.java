public class Jb23_ArrToolDemo
{
	public static void main(String[] args) 
	{
		int[] arr = {0,1,32,5,8,4,9};
		int index = Jb23_ArrTool.getIndex(arr,43);	//获取数字43在数组中的角标
		System.out.println(index);

		int max = getMax(arr);
        System.out.println("数组最大值是"+max);
	}
}
