#include <iostream>
#include <Windows.h>
#include <ctime>
#include <sstream>
#include <string>
#include <set>

// Генерируем рандомное число между значениями min и max.
// Предполагается, что функцию srand() уже вызывали
int getRandomNumber(int min, int max)
{
	static const double fraction = 1.0 / (static_cast<double>(RAND_MAX) + 1.0);
	// Равномерно распределяем рандомное число в нашем диапазоне
	return static_cast<int>(rand() * fraction * (max - min + 1) + min);
}

int main()
{
	SetConsoleCP(1251);// установка кодовой страницы win-cp 1251 в поток ввода
	SetConsoleOutputCP(1251); // установка кодовой страницы win-cp 1251 в поток вывода
	srand(static_cast<unsigned int>(time(0))); // устанавливаем значение системных часов в качестве стартового числа

	int tryg;
	std::string try_guess;
	tryg = getRandomNumber(1000, 9999);
	// 
	std::cout << " rand " << tryg << "\n";
	// try_guess = ToString(tryg);
	try_guess = std::to_string(tryg);

	std::string from_user;

	int cow = 0;
	int bull = 0;
	std::string current = "nnnn";
	//std::set<char> set_tryg;
	while (cow != 4)
	{
		cow = 0;
		bull = 0;
		current = "nnnn";
		std::cout << "Введите число ";
		std::cin >> from_user;
		//std::cout << "Вы ввели " << from_user << "\n";
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				if (try_guess[i] == from_user[j])
				{
					if (i == j) { 
						cow++;
						if (current[i] == 'n') current[i] = 'c'; else 
						{
							std::cout << current[i] << " in i (" << i << ") in current cow " << std::endl;
							//cow--;
						}
							
					}
					else
					{
						bull++;
						if (current[i] == 'n') current[i] = 'b'; else
						{
							std::cout << current[i] << " in i (" << i << ") in current bull " << std::endl;
							bull--;
						}
					}
				}
			}
		}
		
		if (cow == 1)
		{
			std::cout << cow << " корова ";
		}
		else if (cow == 0)
			std::cout << cow << " коров ";
		else
		{
			std::cout << cow << " коровы ";
		}
		if (bull == 1)
		{
			std::cout << bull << " бык ";
		}
		else if (bull == 0)
			std::cout << bull << " быков ";
		else if (bull > 4)
			std::cout << " 4 быка ";
		else
		{
			std::cout << bull << " быка ";
		}
		std::cout << "current " << current << std::endl;
	}
	std::cout << " Поздравляем! Вы угадали число!! " << std::endl;
	return 0;

}

// Запуск программы: CTRL+F5 или меню "Отладка" > "Запуск без отладки"
// Отладка программы: F5 или меню "Отладка" > "Запустить отладку"

// Советы по началу работы 
//   1. В окне обозревателя решений можно добавлять файлы и управлять ими.
//   2. В окне Team Explorer можно подключиться к системе управления версиями.
//   3. В окне "Выходные данные" можно просматривать выходные данные сборки и другие сообщения.
//   4. В окне "Список ошибок" можно просматривать ошибки.
//   5. Последовательно выберите пункты меню "Проект" > "Добавить новый элемент", чтобы создать файлы кода, или "Проект" > "Добавить существующий элемент", чтобы добавить в проект существующие файлы кода.
//   6. Чтобы снова открыть этот проект позже, выберите пункты меню "Файл" > "Открыть" > "Проект" и выберите SLN-файл.
