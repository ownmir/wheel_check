#include <iostream>
#include <Windows.h>
#include <ctime>
#include <sstream>
#include <string>
#include <set>
#include <cmath>
#include <iomanip> // для std::setprecision()

// Генерируем рандомное число между значениями min и max.
// Предполагается, что функцию srand() уже вызывали
int getRandomNumber(int min, int max)
{
	static const double fraction = 1.0 / (static_cast<double>(RAND_MAX) + 1.0);
	// Равномерно распределяем рандомное число в нашем диапазоне
	return static_cast<int>(rand() * fraction * (max - min + 1) + min);
}

void init_array()
{
	double array[365] = { 0.0 };
	// http://www.c-cpp.ru/books/formatirovanie-s-pomoshchyu-funkciy-chlenov-ios
	std::cout.setf(std::ios::showpoint);
	std::cout << "array 1 " << std::setprecision(1) << array[1] << std::endl;
	double value = 0.0;
	int i;
	for (i = 1; i < 7; i++) {
		std::cout << "Точность " << i << ": ";
		std::cout << std::setprecision(i) << value << std::endl;
		value += 0.11111;
	}
}
// количество вхождений символа ch в str
int count(char ch, std::string str)
{
	int coun_ch = 0;
	for (auto cch : str)
	{
		if (cch == ch)
			coun_ch++;
	}
	return coun_ch;
}

void cowsbulls()
{
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
	std::set<char> set_tryg;
	std::set<char> set_from_user;
	int bovine;
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
			set_tryg.emplace(try_guess[i]);
			set_from_user.emplace(from_user[i]);
			for (int j = 0; j < 4; ++j)
			{

				if (try_guess[i] == from_user[j])
				{
					if (i == j) {
						cow++;
					}
					else
					{
						//bull++;
					}
				}
			}
		}
		bovine = 0;
		for (auto digit : set_tryg)
		{
			bovine += min(count(digit, try_guess), count(digit, from_user));
		}

		bull = bovine - cow;
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
}
namespace animals
{
	enum animals
	{
		CHICKEN, //    0
		LION, //       1
		GIRAFFE, //    2
		ELEPHANT, //   3
		DUCK, //       4
		SNAKE, //      5
		MAX_ANIMALS // 6
	};
}
void a()
{
	
	int pows[animals::MAX_ANIMALS];
	pows[animals::CHICKEN] = 2;
	pows[animals::LION] = 4;
	pows[animals::GIRAFFE] = 2;
	pows[animals::ELEPHANT] = 4;
	pows[animals::DUCK] = 2;
	pows[animals::SNAKE] = 0;
	std::cout << "An elephant has " << pows[animals::ELEPHANT] << " pows.\n";

}
int main()
{
	SetConsoleCP(1251);// установка кодовой страницы win-cp 1251 в поток ввода
	SetConsoleOutputCP(1251); // установка кодовой страницы win-cp 1251 в поток вывода
	
	//cowsbulls();
	//init_array();
	a();

	return 0;

}

