//
#include <iostream>
#include <Windows.h>
#include <ctime>
#include <sstream>
#include <string>
#include <set>
/**
 * Интерфейс Субъекта объявляет общие операции как для Реального Субъекта, так и
 * для Заместителя. Пока клиент работает с Реальным Субъектом, используя этот
 * интерфейс, вы сможете передать ему заместителя вместо реального субъекта.
 */
class Subject {
public:
	virtual void Request() const = 0;
};
/**
 * Реальный Субъект содержит некоторую базовую бизнес-логику. Как правило,
 * Реальные Субъекты способны выполнять некоторую полезную работу, которая к
 * тому же может быть очень медленной или точной – например, коррекция входных
 * данных. Заместитель может решить эти задачи без каких-либо изменений в коде
 * Реального Субъекта.
 */
class RealSubject : public Subject {
public:
	void Request() const override {
		std::cout << "RealSubject: Handling request.\n";
	}
};
/**
 * Интерфейс Заместителя идентичен интерфейсу Реального Субъекта.
 */
class Proxy : public Subject {
	/**
	 * @var RealSubject
	 */
private:
	RealSubject *real_subject_;

	bool CheckAccess() const {
		// Некоторые реальные проверки должны проходить здесь.
		std::cout << "Proxy: Checking access prior to firing a real request.\n";
		return true;
	}
	void LogAccess() const {
		std::cout << "Proxy: Logging the time of request.\n";
	}
	/**
	  * Заместитель хранит ссылку на объект класса РеальныйСубъект. Клиент может
	  * либо лениво загрузить его, либо передать Заместителю.
	  */
public:
	Proxy(RealSubject *real_subject) : real_subject_(new RealSubject(*real_subject)) {
	}

	~Proxy() {
		delete real_subject_;
	}
	/**
	 * Наиболее распространёнными областями применения паттерна Заместитель
	 * являются ленивая загрузка, кэширование, контроль доступа, ведение журнала и
	 * т.д. Заместитель может выполнить одну из этих задач, а затем, в зависимости
	 * от результата, передать выполнение одноимённому методу в связанном объекте
	 * класса Реального Субъект.
	 */
	void Request() const override {
		if (this->CheckAccess()) {
			this->real_subject_->Request();
			this->LogAccess();
		}
	}
};
/**
 * Клиентский код должен работать со всеми объектами (как с реальными, так и
 * заместителями) через интерфейс Субъекта, чтобы поддерживать как реальные
 * субъекты, так и заместителей. В реальной жизни, однако, клиенты в основном
 * работают с реальными субъектами напрямую. В этом случае, для более простой
 * реализации паттерна, можно расширить заместителя из класса реального
 * субъекта.
 */
void ClientCode(const Subject &subject) {
	// ...
	subject.Request();
	// ...
}
template <typename T>
inline std::string ToString(T tX)
{
	std::ostringstream oStream;
	oStream << tX;
	return oStream.str();
}
// Генерируем рандомное число между значениями min и max.
// Предполагается, что функцию srand() уже вызывали
int getRandomNumber(int min, int max)
{
	static const double fraction = 1.0 / (static_cast<double>(RAND_MAX) + 1.0);
	// Равномерно распределяем рандомное число в нашем диапазоне
	return static_cast<int>(rand() * fraction * (max - min + 1) + min);
}
int main() {
	std::cout << "Client: Executing the client code with a real subject:\n";
	RealSubject *real_subject = new RealSubject;
	ClientCode(*real_subject);
	std::cout << "\n";
	std::cout << "Client: Executing the same client code with a proxy:\n";
	Proxy *proxy = new Proxy(real_subject);
	ClientCode(*proxy);

	delete real_subject;
	delete proxy;
	// https://ravesli.com/praktika-chast-22/
	// http://www.papg.com/number-bullcow.html
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
	//std::set<char> set_tryg;
	while (cow != 4)
	{
		cow = 0;
		bull = 0;
		std::cout << "Введите число ";
		std::cin >> from_user;
		//std::cout << "Вы ввели " << from_user << "\n";
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				if (try_guess[i] == from_user[j])
				{
					if (i == j) cow++;
					else
					{
						bull++;
					}
				}
			}
		}
		//std::cout << " set is done." << std::endl;
		//char ch;
		//for (int i = 0; i < 4; ++i)
		//{
		//	ch = from_user[i];
		//	if (try_guess[i] == ch)
		//	{
		//		cow++;
		//		continue;
		//	}
		//		
		//	//std::cout << *set_tryg.find(ch) << std::endl;
		//	std::cout << " current ch " << std::endl;
		//	std::cout << ch << std::endl;
		//	if (set_tryg.find(ch) == set_tryg.end())
		//	{
		//		std::cout << " not found " << std::endl;
		//	}
		//	else
		//	{
		//		bull++;
		//	}
				
			//if (try_guess.find(ch))
				//bull++;
			//std::cout << std::count(try_guess.begin(), try_guess.end(), ch) << std::endl;
		//}
		/*std::cout << " Begin unique set " << std::endl;
		for (auto item : set_tryg)
		{
			std::cout << item << std::endl;
		}
		std::cout << " .. end. " << std::endl;*/
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
	}
	std::cout << " Поздравляем! Вы угадали число!! " << std::endl;

	return 0;
}
