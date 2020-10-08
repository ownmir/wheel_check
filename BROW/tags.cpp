bool is_tag(const std::string &sour)
{
	int len_sour = sour.length();
	if (len_sour < 3)
	{
		// ваш tag не может быть менее 3 - х символов
		// std::cout << ":( ваш tag не может быть менее 3 - х символов!";
		return false;
	}
	char first = sour[0];            char last = sour[len_sour - 1];
	if (first != '<') return false;  if (last != '>') return false;
	return true;
}
int main()
{
	SetConsoleCP(1251);// установка кодовой страницы win-cp 1251 в поток ввода
	SetConsoleOutputCP(1251); // установка кодовой страницы win-cp 1251 в поток вывода
	
	if (is_tag("<b>"))
		std::cout << "This is tag!";

	return 0;
}