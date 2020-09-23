#include <iostream>
#include <cstdlib>   // для функций выбора случайного числа srand() и rand()
#include <ctime>     // чтобы в randomize опираться на время запуска программы
#include <vector>    // для разложения на цифры числа любой длины
#include <cmath>     // для степени

//функция выбора случайного числа между двумя заданными значениями
static unsigned short getRandomNumber(unsigned short min, unsigned short max)
{
	static const double fraction = 1.0 / static_cast<double>(RAND_MAX + 1.0);
	return static_cast<unsigned short>(rand() * fraction * (max - min + 1) + min);
}
// получаем от пользователя натуральное число
unsigned getNumber(const unsigned min, const unsigned max)
{
	int answer;
	std::cin >> answer;
	while (std::cin.fail() || (answer < min) || (answer > max))
	{
		std::cin.clear();
		std::cin.ignore(1000, '\n');
		std::cout << "Нужно ввести число от " << min << " до " << max << ", повторите ввод: ";
		std::cin >> answer;
	}
	std::cin.ignore(1000, '\n');
	return static_cast<unsigned>(answer);
}
// раскладываем число на цифры в векторе
std::vector<unsigned short> getFiguresByNumber(const unsigned number)
{
	unsigned short numberLength{ 0 };       // количество знаков в числе
	while (number >= pow(10, numberLength))
		++numberLength;

	std::vector<unsigned short> figures{};
	for (short digits_counter = (numberLength - 1); digits_counter >= 0; --digits_counter)
		figures.push_back((number / static_cast<unsigned>(pow(10, digits_counter))) % 10);
	return figures;
}
// возвращает истину, если число угадано, выводит количество коров и быков, если нет
bool compareNumbersByDigits(const unsigned generatedNumber, const unsigned usersTry)
{
	if (generatedNumber == usersTry)
	{
		std::cout << "Вы угадали число " << generatedNumber << "!\n";
		return true;
	}
	else
	{
		// раскладываем на цифры загаданное число:
		static std::vector<unsigned short> numberToGuessFigures = getFiguresByNumber(generatedNumber);
		const unsigned length = numberToGuessFigures.size();

		// нам понадобится отмечать уже посчитанные числа:
		std::vector<bool> busy_figures{};
		busy_figures.resize(length);

		// раскладываем на цифры число от пользователя:
		std::vector<unsigned short> usersNumberFigures = getFiguresByNumber(usersTry);

		unsigned short cows{ 0 }, bulls{ 0 };
		// идём по цифрам из числа, полученного от пользователя:
		for (auto i = 0; i < length; ++i)
		{
			// идём по цифрам из угадываемого числа:
			for (auto j = 0; j < length; ++j)
				// цифра из угадываемого числа ещё "не занята" и совпадает с рассматриваемой цифрой из числа от пользователя:
				if ((busy_figures[j] == false) && (numberToGuessFigures[j] == usersNumberFigures[i]))
				{
					busy_figures[j] = true; // помечаем её как "занятую"
					// если для этой цифры есть полное совпадение, то считаем корову:
					if (numberToGuessFigures[j] == usersNumberFigures[j])
					{
						++cows;
						if (j == i) break;  // корова для рассматриваемой цифры числа от пользователя => переходим к следующей цифре из числа пользователя
					}
					else  // иначе - это бык и переходим к следующей цифре из числа пользователя
					{
						++bulls;
						break;
					}
				}
		}
		// даём подсказку результата сравнения:
		std::cout << cows << " коров(a/ы), " << bulls << " бык(а/ов)\n";
		return false;
	}
}

int main()
{
	setlocale(LC_CTYPE, "rus");                // для кириллицы
	srand(static_cast<unsigned int>(time(0))); // аналог randomize с привязкой ко времени запуска

	// будем работать с 4-значными числами:
	const unsigned short numberSize{ 4 };
	const unsigned minNumber{ static_cast<unsigned>(pow(10, numberSize - 1)) };
	const unsigned maxNumber{ static_cast<unsigned>(pow(10, numberSize) - 1) };

	// генерируем случайное четырёхзначное число:
	unsigned numberToGuess = getRandomNumber(minNumber, maxNumber);
	std::cout << "Добро пожаловать в игру <<Коровы и быки>>!\nКомпьютер загадал " << numberSize
		<< "-значное число, попробуйте его угадать\n"
		<< "за каждую угаданную цифру на своём месте Вы получите корову, за угаданную цифру на другом месте - быка.\n\n";

	// пока пользователь не угадает число, будем запрашивать его предположение:
	unsigned usersNumber{ 0 };
	do
	{
		std::cout << "Ваше предположение: ";
		usersNumber = getNumber(minNumber, maxNumber);
	} while (!compareNumbersByDigits(numberToGuess, usersNumber));

	return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
