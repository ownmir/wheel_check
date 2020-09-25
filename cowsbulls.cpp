#include <iostream>
#include <cstdlib>   // ��� ������� ������ ���������� ����� srand() � rand()
#include <ctime>     // ����� � randomize ��������� �� ����� ������� ���������
#include <vector>    // ��� ���������� �� ����� ����� ����� �����
#include <cmath>     // ��� �������

//������� ������ ���������� ����� ����� ����� ��������� ����������
static unsigned short getRandomNumber(unsigned short min, unsigned short max)
{
	static const double fraction = 1.0 / static_cast<double>(RAND_MAX + 1.0);
	return static_cast<unsigned short>(rand() * fraction * (max - min + 1) + min);
}
// �������� �� ������������ ����������� �����
unsigned getNumber(const unsigned min, const unsigned max)
{
	int answer;
	std::cin >> answer;
	while (std::cin.fail() || (answer < min) || (answer > max))
	{
		std::cin.clear();
		std::cin.ignore(1000, '\n');
		std::cout << "����� ������ ����� �� " << min << " �� " << max << ", ��������� ����: ";
		std::cin >> answer;
	}
	std::cin.ignore(1000, '\n');
	return static_cast<unsigned>(answer);
}
// ������������ ����� �� ����� � �������
std::vector<unsigned short> getFiguresByNumber(const unsigned number)
{
	unsigned short numberLength{ 0 };       // ���������� ������ � �����
	while (number >= pow(10, numberLength))
		++numberLength;

	std::vector<unsigned short> figures{};
	for (short digits_counter = (numberLength - 1); digits_counter >= 0; --digits_counter)
		figures.push_back((number / static_cast<unsigned>(pow(10, digits_counter))) % 10);
	return figures;
}
// ���������� ������, ���� ����� �������, ������� ���������� ����� � �����, ���� ���
bool compareNumbersByDigits(const unsigned generatedNumber, const unsigned usersTry)
{
	if (generatedNumber == usersTry)
	{
		std::cout << "�� ������� ����� " << generatedNumber << "!\n";
		return true;
	}
	else
	{
		// ������������ �� ����� ���������� �����:
		static std::vector<unsigned short> numberToGuessFigures = getFiguresByNumber(generatedNumber);
		const unsigned length = numberToGuessFigures.size();

		// ��� ����������� �������� ��� ����������� �����:
		std::vector<bool> busy_figures{};
		busy_figures.resize(length);

		// ������������ �� ����� ����� �� ������������:
		std::vector<unsigned short> usersNumberFigures = getFiguresByNumber(usersTry);

		unsigned short cows{ 0 }, bulls{ 0 };
		// ��� �� ������ �� �����, ����������� �� ������������:
		for (auto i = 0; i < length; ++i)
		{
			// ��� �� ������ �� ������������ �����:
			for (auto j = 0; j < length; ++j)
				// ����� �� ������������ ����� ��� "�� ������" � ��������� � ��������������� ������ �� ����� �� ������������:
				if ((busy_figures[j] == false) && (numberToGuessFigures[j] == usersNumberFigures[i]))
				{
					busy_figures[j] = true; // �������� � ��� "�������"
					// ���� ��� ���� ����� ���� ������ ����������, �� ������� ������:
					if (numberToGuessFigures[j] == usersNumberFigures[j])
					{
						++cows;
						if (j == i) break;  // ������ ��� ��������������� ����� ����� �� ������������ => ��������� � ��������� ����� �� ����� ������������
					}
					else  // ����� - ��� ��� � ��������� � ��������� ����� �� ����� ������������
					{
						++bulls;
						break;
					}
				}
		}
		// ��� ��������� ���������� ���������:
		std::cout << cows << " �����(a/�), " << bulls << " ���(�/��)\n";
		return false;
	}
}

int main()
{
	setlocale(LC_CTYPE, "rus");                // ��� ���������
	srand(static_cast<unsigned int>(time(0))); // ������ randomize � ��������� �� ������� �������

	// ����� �������� � 4-�������� �������:
	const unsigned short numberSize{ 4 };
	const unsigned minNumber{ static_cast<unsigned>(pow(10, numberSize - 1)) };
	const unsigned maxNumber{ static_cast<unsigned>(pow(10, numberSize) - 1) };

	// ���������� ��������� ������������� �����:
	unsigned numberToGuess = getRandomNumber(minNumber, maxNumber);
	std::cout << "����� ���������� � ���� <<������ � ����>>!\n��������� ������� " << numberSize
		<< "-������� �����, ���������� ��� �������\n"
		<< "�� ������ ��������� ����� �� ���� ����� �� �������� ������, �� ��������� ����� �� ������ ����� - ����.\n\n";

	// ���� ������������ �� ������� �����, ����� ����������� ��� �������������:
	unsigned usersNumber{ 0 };
	do
	{
		std::cout << "���� �������������: ";
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
