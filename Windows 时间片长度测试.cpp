#include <stdio.h>
#include <windows.h>
#pragma comment(lib,"winmm.lib")	//for using timeGetTime() 使用winmm.lib库
void testCpuTimeSlice(unsigned long printTimes)
{
	unsigned long oldTick, newTick, times = 0, i = 0;
	oldTick = timeGetTime();
	while (true)
	{
		i++;
		newTick = timeGetTime();
		if (newTick - oldTick >= 2)
		{
			printf("[%d] %10d - %10d = %3d(ms), %10d\n", ++times, newTick, oldTick, newTick - oldTick, i);
			if (times >= printTimes)
				break;
		}
		oldTick = newTick;
	}
}

int main()
{
	testCpuTimeSlice(10);
	getchar(); getchar();
	return 0;
}
//CPU忙时
//[1]     482324 - 482309 = 15(ms), 25934153
//[2]     482340 - 482324 = 16(ms), 26756898
//[3]     482369 - 482353 = 16(ms), 28281567
//[4]     482385 - 482369 = 16(ms), 29083310
//[5]     482400 - 482385 = 15(ms), 29900180
//[6]     482416 - 482400 = 16(ms), 30724025
//[7]     482431 - 482416 = 15(ms), 31528360
//[8]     482447 - 482431 = 16(ms), 32350089
//[9]     482469 - 482454 = 15(ms), 33531031
//[10]     482485 - 482469 = 16(ms), 34355448
//CPU 不忙时
//[1]     560862 - 560860 = 2(ms), 7050376
//[2]     561130 - 561119 = 11(ms), 20504647
//[3]     561509 - 561507 = 2(ms), 39705320
//[4]     561688 - 561686 = 2(ms), 49016982
//[5]     562377 - 562375 = 2(ms), 84002186
//[6]     562381 - 562379 = 2(ms), 84187115
//[7]     563171 - 563169 = 2(ms), 123893707
//[8]     563176 - 563174 = 2(ms), 124119128
//[9]     563181 - 563179 = 2(ms), 124380511
//[10]     563330 - 563328 = 2(ms), 132116595

// 猜测：
//     对于多核，即使一个内核一直在运行while循环，也可能不会被打断，因为还有其他核去执行其他任务。 
//     如果CPU不忙，运行一个实例的话，会一直都没有输出，或是测出来的时间片很短，因为它可以独占一个内核，不需要给别人让出时间片。
